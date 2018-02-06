# import the necessary packages
import pytesseract
import numpy as np
import random
import cv2
from ocrCNN import ocrCNN

import pytesseract


class imageReader:
    def __init__(self,args):
        self.args = args
        self.cnn = ocrCNN()

    @staticmethod
    def generateImage(numImages=1):
        images = []
        labels = []
        size = 100

        pageSize = (1000, 1000)

        for i in range(numImages):
            page = np.full(pageSize, 255, dtype=np.uint8)

            location = (100+int(random.random()*(pageSize[1]-200)), 100+int(random.random()*(pageSize[0]-200)))
            cv2.circle(page, location,size, (0, 0, 255))

            images.append(page)
            labels.append(location)
        return images, labels

    def train(self):
        grayImages, labels = self.generateImage(numImages=10000)
        self.cnn.train(grayImages, labels)


    def processImage(self,image):

        labels = []

        labels.append(("a",0,0,200,200))

        return