import cv2 as cv 
import numpy as np 
from matplotlib import pyplot as plt 
from sightengine.client import SightengineClient

def enhance_contrast (pathtofile):
	client = SightengineClient('1809910925', 'uYAfi34tLkxCpTY2c4Ge')
	output = client.check('properties').set_file(pathtofile)
	if output['contrast'] < 0.8:
		orig_img = cv.imread(pathtofile, 1)
		ycrcb_convert = cv.cvtColor(orig_img, cv.COLOR_BGR2YCrCb)
		y, cr, cb = cv.split(ycrcb_convert)
		new_y = cv.equalizeHist(y)
		clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
		new_y = clahe.apply(new_y)
		merged_channels = cv.merge((new_y, cr, cb))
		final_image = cv.cvtColor(merged_channels, cv.COLOR_YCrCb2BGR)
		cv.imwrite('enhanced.jpg', final_image)





