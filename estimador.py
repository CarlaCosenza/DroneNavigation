import cv2
import numpy as np

from constants import templateImage, sceneMatchingAlgorithm, singleImageTest, mapTemplatePoints, mapRealPoints
from matplotlib import pyplot as plt
from sceneMatching import SceneMatching

class Estimador:
	def __init__(self):
		self.templateImageName = templateImage
		self.sceneMatching = SceneMatching(templateImage)
		
		H, mask = cv2.findHomography(mapTemplatePoints, mapRealPoints)
		self.matrizTransformacao = H

	def cropImage(self, frame, currentHeight):
		h,w,x = frame.shape
		delta = int(200*currentHeight/1.28)
		frame = frame[delta:h, 0:w-1]
		return frame

	def match(self, frame, currentHeight):
		croppedFrame= self.cropImage(frame, currentHeight)
		resultImage, point = self.sceneMatching.matchWithFlann(frame, croppedFrame)
		point = self.transformPoint(point)
		return resultImage, point

	def testSingleImage(self):
		image = cv2.imread(singleImageTest)
		result = self.sceneMatching.match(image)
		cv2.imshow(sceneMatchingAlgorithm, result)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	def transformPoint(self, point):
		# print("point in image", point)
		if point[0][0][0] == -1000 and point[0][0][1] == -1000:
			return None
		point[0][0][0], point[0][0][1] = point[0][0][1], point[0][0][0]
		transformedPoint = cv2.perspectiveTransform(point, self.matrizTransformacao)
		# print('real point', transformedPoint)
		return transformedPoint