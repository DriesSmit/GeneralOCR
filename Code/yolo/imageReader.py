# import the necessary packages
import pytesseract
import numpy as np
import random
import cv2
from ocrCNN import ocrCNN

class imageReader:
    def __init__(self,args):
        self.args = args
        self.cnn = ocrCNN()

    @staticmethod
    def generateImage(numImages=1,numCharacters=1):
        images = []
        allLabels = []

        for i in range(numImages):
            page = np.full((2000, 1000), 255, dtype=np.uint8)

            labels = []
            for i in range(numCharacters):
                #Random paramaters
                fondSize = 10
                char = unichr(ord('A') + int(random.random() * 26))
                font = cv2.FONT_HERSHEY_PLAIN

                location = (100+int(random.random()*800), 100+int(random.random()*1800))
                cv2.putText(page, char, location, font, fondSize, (0, 0, 255))
                labels.append((char,location[0],location[1]-100,location[0]+fondSize*10,location[1]+fondSize*10-100))

            images.append(page)
            allLabels.append(labels)
        return images, allLabels

    def train(self):
        grayImages, labels = self.generateImage(numImages=10000)
        self.cnn.train(grayImages, labels)


    def processImage(self,image):

        labels = []

        labels.append(("a",0,0,200,200))

        return