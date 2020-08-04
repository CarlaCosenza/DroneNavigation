import cv2

from capturador import Capturador

if __name__ == '__main__':
	capturador = Capturador()

	while(capturador.frameExists()):
		frame = capturador.getFrame()
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
    
	cv2.destroyAllWindows()
	capturador.releaseCapture