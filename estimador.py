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

	def match(self, frame):
		resultImage, point = self.sceneMatching.matchWithFlann(frame)
		point = self.transformPoint(point)
		return resultImage, point

	def testSingleImage(self):
		image = cv2.imread(singleImageTest)
		result = self.sceneMatching.match(image)
		cv2.imshow(sceneMatchingAlgorithm, result)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	def transformPoint(self, point):
		transformedPoint = cv2.perspectiveTransform(point, self.matrizTransformacao)
		return transformedPoint