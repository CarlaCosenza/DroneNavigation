import cv2
import time

from capturador import Capturador
from estimador import Estimador
from constants import isSingleTest

if __name__ == '__main__':

	estimador = Estimador()

	if(isSingleTest):
		estimador.testSingleImage()
		exit()

	capturador = Capturador()

	while(capturador.frameExists()):
		startTime = time.time()
		frame = capturador.getFrame()
		result = estimador.match(frame)
		cv2.imshow('Matching',result)
		endTime = time.time()
		print('FPS: ', 1/(endTime-startTime))
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cv2.destroyAllWindows()
	capturador.releaseCapture()
	exit()