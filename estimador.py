import cv2
import numpy as np

from constants import templateImage, sceneMatchingAlgorithm, singleImageTest
from matplotlib import pyplot as plt
from sceneMatching import SceneMatching

class Estimador:
	def __init__(self):
		self.templateImageName = templateImage
		self.sceneMatching = SceneMatching(templateImage)

	def match(self, frame):
		return self.sceneMatching.matchWithFlann(frame)

	def testSingleImage(self):
		image = cv2.imread(singleImageTest)
		result = self.sceneMatching.match(image)
		cv2.imshow(sceneMatchingAlgorithm, result)
		cv2.waitKey(0)
		cv2.destroyAllWindows()