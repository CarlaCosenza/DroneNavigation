import numpy as np

from enums import ImageInput

# MAIN CONSTANTS
isSingleTest = False

# CAPTURADOR CONSTANTS
inputType = ImageInput.VIDEO
videoFile = 'imagensTeste/teste4.mp4'

# ESTIMADOR CONSTANTS
templateImage = 'imagensTeste/teste4Referencial4.jpg'
singleImageTest = 'golden.jpeg'
mapTemplatePoints = np.float32([[ 777 , 753 ], [ 416 , 2389 ], [ 844 , 2818 ]]).reshape(-1,1,2)
mapRealPoints = np.float32([[0,0], [112, -30], [150, 0]]).reshape(-1,1,2)

# SCENE MATCHING CONSTANTS
sceneMatchingAlgorithm = 'SIFT'
minMatchCount = 10