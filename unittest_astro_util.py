#!/usr/bin/python

import astro_util as AU
import unittest

def CheckTwilightValue(inputString):
	isValid = True if inputString in ["Daylight", "Civil", "Nautical", "Astronomical", "Night"] else False
	
	return isValid

class AstroTest(unittest.TestCase):
	def test_Azimuth_North(self):
		self.assertEqual(AU.AzimuthToCompassDirection(AU.DegreesToRadians(0)), "North")

	def test_Azimuth_East(self):
		self.assertEqual(AU.AzimuthToCompassDirection(AU.DegreesToRadians(90)), "East")

	def test_Azimuth_South(self):
		self.assertEqual(AU.AzimuthToCompassDirection(AU.DegreesToRadians(180)), "South")

	def test_Azimuth_West(self):
		self.assertEqual(AU.AzimuthToCompassDirection(AU.DegreesToRadians(270)), "West")

if __name__ == '__main__':
	unittest.main()
