from imageReader import imageReader
import cv2

args = []

ir = imageReader(args)

images, allLabels = ir.generateImage(numImages=10,numCharacters=20)
font = cv2.FONT_HERSHEY_PLAIN
fondSize = 10

for i in range(len(images)):
    image = images[i]
    for label in allLabels[i]:
        print label
        cv2.rectangle(image, (int(label[1]), int(label[2])), (int(label[3]), int(label[4])), (0, 0, 0), 1)

        #location = (200,200)
        #cv2.putText(image, str(label[0]), location, font, fondSize, (0, 0, 255))

    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Image", image)
    cv2.waitKey(0)

