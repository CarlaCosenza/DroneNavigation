import cv2
import numpy as np

from constants import inputType, videoFile
from enums import ImageInput

def noDrone():
	printf("Did not implement drone feature yet. Exiting...")
	exit()

class Capturador:
	def __init__(self):
		if(inputType == ImageInput.VIDEO):
			print('The selected input type is video')
			self.cap = cv2.VideoCapture(videoFile)
		if(inputType == ImageInput.COMPUTER_CAMERA):
			print('The selected input type is computer camera')
			self.cap = cv2.VideoCapture(0)
			if(not self.cap.isOpened()):
				cap.open()
		if(inputType == ImageInput.DRONE_CAMERA):
			print('The selected input type is drone camera')
			noDrone()

	def frameExists(self):
		if(inputType == ImageInput.VIDEO):
			return self.cap.isOpened()
		if(inputType == ImageInput.COMPUTER_CAMERA):
			return True
		if(inputType == ImageInput.DRONE_CAMERA):
			return noDrone()

	def getFrame(self):
		ret, frame = self.cap.read()
		if(not ret):
			print('There was an error in getting the frame. Exiting...')
			exit()
		return frame

	def releaseCapture(self):
		self.cap.release()
