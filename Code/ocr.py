# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os

def orientationScore(image,skipStep = 10):
    totValue = 0
    for row in range(len(image)):
        rowVal = 0
        for col in range(0,len(image[0]),skipStep):
            rowVal += image[row][col]
        totValue += rowVal*rowVal
    return totValue

def findOrient(image,angleRange = 5,skipStep = 10):
    maxValue = -1
    maxRot  = 0
    imageRows, imageCols = image.shape
    accuracy = 0.1



    for i in range(-1, angleRange*2*int(1/accuracy)):
        #rot = i
        rot = (round(i / 2 - 0.4) + 1) * ((-1) * (i % 2) + ((i + 1) % 2)) * 0.1
        #print rot
        # print("Rotation: ",rot,". i: ",i)
        M = cv2.getRotationMatrix2D((imageCols / 2, imageRows / 2), rot, 1)
        dst = cv2.warpAffine(image, M, (imageCols, imageRows), borderValue=(255, 255, 255))

        value = orientationScore(255-dst,skipStep = 10)
        if value>maxValue:
            maxValue = value
            maxRot = rot
        print "Current angle: ",rot,". Current value: ", value,". Max value: ",maxValue,". Max rot: ",maxRot
        #cv2.imshow("Rotated Image: ",dst)
        #cv2.waitKey(0)

    M = cv2.getRotationMatrix2D((imageCols / 2, imageRows / 2), maxRot, 1)
    dst = cv2.warpAffine(image, M, (imageCols, imageRows), borderValue=(255, 255, 255))
    #cv2.imshow("Rotated Image: ", dst)
    #cv2.waitKey(0)
    return dst

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,help="path to input image to be OCR'd")
# ap.add_argument("-p", "--preprocess", type=str, default="thresh",	help="type of preprocessing to be done")
# args = vars(ap.parse_args())s
args = {}
args["image"] = "/home/dries/devel/PraelexisOCR/Code/RealScan.jpg"
args["preprocess"] = ""

# load the example image and convert it to grayscale
image = cv2.imread(args["image"])

# cv2.imshow("Image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# check to see if we should apply thresholding to preprocess the
# image
if args["preprocess"] == "thresh":
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# make a check to see if median blurring should be done to remove
# noise
elif args["preprocess"] == "blur":
    gray = cv2.medianBlur(gray, 1)

gray = findOrient(gray,angleRange = 0,skipStep = 10)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename))
#os.remove(filename)
print "Text found:\n",text

# show the output images
cv2.namedWindow('Input', cv2.WINDOW_NORMAL)
cv2.imshow("Input", image)
cv2.namedWindow('Output', cv2.WINDOW_NORMAL)
cv2.imshow("Output", gray)
cv2.waitKey(0)