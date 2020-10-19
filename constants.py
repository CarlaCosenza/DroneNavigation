import numpy as np

from enums import ImageInput

# MAIN CONSTANTS
isSingleTest = False

# CAPTURADOR CONSTANTS
inputType = ImageInput.VIDEO
videoFile = 'imagensTeste/teste4.mp4'

# ESTIMADOR CONSTANTS
templateImage = 'imagensTeste/experimento1Referencial25.jpg'
singleImageTest = 'golden.jpeg'
mapTemplatePoints = np.float32([[ 103 , 387 ],[ 521 , 377 ], [ 51 , 121 ], [ 766 , 700 ], [ 900 , 363 ]]).reshape(-1,1,2)
mapRealPoints = np.float32([[0,0], [77,0], [-11,50], [136,-46], [150, 0]]).reshape(-1,1,2)

# SCENE MATCHING CONSTANTS
sceneMatchingAlgorithm = 'SIFT'
minMatchCount = 8