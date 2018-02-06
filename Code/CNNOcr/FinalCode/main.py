from imageReader import imageReader
import cv2

args = []

ir = imageReader(args)

images, labels = ir.generateImage(numImages=1000)
size = 100
for i in range(len(images)):
    image = images[i]
    label = labels[i]
    print label
    cv2.rectangle(image, (int(label[0])-size, int(label[1])-size), (int(label[0])+size, int(label[1])+size), (0, 0, 0), 1)

        #location = (200,200)
        #cv2.putText(image, str(label[0]), location, font, fondSize, (0, 0, 255))

    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Image", image)
    cv2.waitKey(0)

