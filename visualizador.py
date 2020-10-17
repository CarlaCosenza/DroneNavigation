import asyncio
import cv2

async def printImage(image):
	cv2.imshow('Matching', image)

async def printFPS(startTime, endTime):
	print('FPS: ', 1/(endTime-startTime))