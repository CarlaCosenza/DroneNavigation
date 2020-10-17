import numpy as np

from enums import ImageInput

# MAIN CONSTANTS
isSingleTest = False

# CAPTURADOR CONSTANTS
inputType = ImageInput.VIDEO
videoFile = 'imagensTeste/teste2.mp4'

# ESTIMADOR CONSTANTS
templateImage = 'imagensTeste/teste2Referencial.jpg'
singleImageTest = 'golden.jpeg'
mapTemplatePoints = np.float32([[788,992], [459, 2214], [739, 2967]]).reshape(-1,1,2)
mapRealPoints = np.float32([[0,0], [86, -34], [150, 0]]).reshape(-1,1,2)

# SCENE MATCHING CONSTANTS
sceneMatchingAlgorithm = 'SIFT'
minMatchCount = 10