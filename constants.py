import numpy as np

from enums import ImageInput

# MAIN CONSTANTS
isSingleTest = False

# CAPTURADOR CONSTANTS
inputType = ImageInput.VIDEO
videoFile = 'imagensTeste/teste4.mp4'

# ESTIMADOR CONSTANTS
templateImage = 'imagensTeste/25_2.jpg'
singleImageTest = 'golden.jpeg'
mapTemplatePoints = np.float32([[289,208], [ 198 , 207 ], [ 366 , 66 ], [694,296], [867,200]]).reshape(-1,1,2)
mapRealPoints = np.float32([[0,0], [-20,0], [22,35],[101, -25], [150, 0]]).reshape(-1,1,2)

# SCENE MATCHING CONSTANTS
sceneMatchingAlgorithm = 'SIFT'
minMatchCount = 10