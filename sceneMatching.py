import cv2 
import numpy as np
import matplotlib.pyplot as plt

from constants import sceneMatchingAlgorithm, minMatchCount

# https://pysource.com/2018/03/21/feature-detection-sift-surf-obr-opencv-3-4-with-python-3-tutorial-25/

class SceneMatching:
	def __init__(self, templateImageName):
		self.matchingAlgorithm = self.getAlgorithm()
		self.templateImage = cv2.imread(templateImageName)
		self.templateImageGrayScale = cv2.cvtColor(self.templateImage, cv2.COLOR_BGR2GRAY)
		self.templateKeyPoints, self.templateDescriptors = self.matchingAlgorithm.detectAndCompute(self.templateImageGrayScale,None)

	def getAlgorithm(self):
		print('Using the ', sceneMatchingAlgorithm, ' algorithm')
		if(sceneMatchingAlgorithm == 'SURF'):
			return cv2.xfeatures2d.SURF_create()
		if(sceneMatchingAlgorithm == 'SIFT'):
			return cv2.xfeatures2d.SIFT_create()
		if(sceneMatchingAlgorithm == 'ORB'):
			return cv2.ORB_create(nfeatures=1700)
		print(sceneMatchingAlgorithm, ' is not a valid option. Exiting...')
		exit()

	def match(self, image):
		img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		keypoints, descriptors = self.matchingAlgorithm.detectAndCompute(img,None)
		bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

		matches = bf.match(descriptors, self.templateDescriptors)
		matches = sorted(matches, key = lambda x:x.distance)

		resultImg = cv2.drawMatches(image, keypoints, self.templateImage, self.templateKeyPoints, matches[:50], self.templateImage, flags=2)
		return resultImg

	def matchWithFlann(self, image):
		img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		keypoints, descriptors = self.matchingAlgorithm.detectAndCompute(img,None)

		FLANN_INDEX_KDTREE = 0
		index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
		search_params = dict(checks = 50)

		flann = cv2.FlannBasedMatcher(index_params, search_params)

		matches = flann.knnMatch(descriptors,self.templateDescriptors,k=2)
		good = []
		for m,n in matches:
			if m.distance < 0.7*n.distance:
				good.append(m)

		img2 = self.templateImage
		imageCenter = np.float32([0,0]).reshape(-1,1,2)

		if len(good)>minMatchCount:
			src_pts = np.float32([ keypoints[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
			dst_pts = np.float32([ self.templateKeyPoints[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

			M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
			matchesMask = mask.ravel().tolist()

			h,w,x = image.shape
			imageCenter = np.float32([w/2, h/2]).reshape(-1,1,2)
			imageCenter = cv2.perspectiveTransform(imageCenter,M)

			# Draw path
			img2 = cv2.circle(img2, (imageCenter[0][0][0], imageCenter[0][0][1]), 10, 255, 3)

		else:
			# print("Not enough matches are found - %d/%d" % (len(good),minMatchCount) )
			matchesMask = None

		draw_params = dict(matchColor = (0,255,0), # draw matches in green color
			singlePointColor = None,
			matchesMask = matchesMask, # draw only inliers
			flags = 2)

		img3 = cv2.drawMatches(image,keypoints,img2,self.templateKeyPoints,good,None,**draw_params)
		return img3, imageCenter
