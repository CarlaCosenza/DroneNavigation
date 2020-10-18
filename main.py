import cv2
import numpy as np
import time

from capturador import Capturador
from estimador import Estimador
from constants import isSingleTest

if __name__ == '__main__':

	estimador = Estimador()
	currentHeight = 1.28
	numberOfFrames = 0
	Found = 0

	if(isSingleTest):
		estimador.testSingleImage()
		exit()

	# position = np.float32([345.5698, 499.8454]).reshape(-1,1,2)
	# position = estimador.transformPoint(position)
	# print(position)

	capturador = Capturador()

	while(capturador.frameExists()):
		startTime = time.time()
		frame = capturador.getFrame()
		result, position = estimador.match(frame, currentHeight)

		cv2.imshow('Matching',result)
		endTime = time.time()
		# print('FPS: ', 1/(endTime-startTime))
		print('Position:', position)

		numberOfFrames += 1
		if isinstance(position, type(None)):
			Found += 1

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cv2.destroyAllWindows()
	capturador.releaseCapture()

	print('total amount of frames:', numberOfFrames)
	print('times position was found:', Found)

	exit()