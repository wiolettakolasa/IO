# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:30:55 2018

@author: Wioletta
"""
import cv2
from localbinarypatterns import LocalBinaryPatterns


img = cv2.imread('yaleB01_P00A+000E+00.pgm')

cv2.imshow('Image',img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

desc = LocalBinaryPatterns(24, 8)

hist = desc.describe(gray)

cv2.imshow('Histogram', hist)