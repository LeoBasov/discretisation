''' 
=============================================================================================
descrete-pack

A tool for 3-D space discritisation
---------------------------------------------------------------------------------------------
Copyright (C) 2018  Leo Basov

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public Licens
along with this program. If not, see <http://www.gnu.org/licenses/>.
=============================================================================================
'''

import math

class Cuboid:
	"""Cuboid shaped domain"""
	def __init__(self, xmin = 0.0, xmax = 1.0, ymin = 0.0, ymax = 1.0, zmin = 0.0, zmax = 1.0):
		self.xmin = xmin
		self.xmax = xmax
		self.ymin = ymin
		self.ymax = ymax
		self.zmin = zmin
		self.zmax = zmax

		self.volume = (self.xmax - self.xmin)*(self.ymax - self.ymin)*(self.zmax - self.zmin)
		self.diagonal = math.sqrt((self.xmax - self.xmin)**2 + (self.ymax - self.ymin)**2 + (self.zmax - self.zmin)**2)

		self.barycentre = (0.5*(self.xmax + self.xmin), 0.5*(self.ymax + self.ymin), 0.5*(self.zmax + self.zmin))

	def check_if_inside(self, position):
		"""Function used to check if position lies inside of domain"""
		inx = (position[0] <= self.xmax) and (position[0] >= self.xmin)
		iny = (position[1] <= self.ymax) and (position[1] >= self.ymin)
		inz = (position[2] <= self.zmax) and (position[2] >= self.zmin)

		return inx and iny and inz

	def subdivide(self, pivot_point):
		ret_cuboids = [None]*8

		ret_cuboids[0] = Cuboid(self.xmin     , pivot_point[0], self.ymin     , pivot_point[1], self.zmin     , pivot_point[2])
		ret_cuboids[1] = Cuboid(pivot_point[0], self.xmax     , self.ymin     , pivot_point[1], self.zmin     , pivot_point[2])
		ret_cuboids[2] = Cuboid(pivot_point[0], self.xmax     , pivot_point[1], self.ymax     , self.zmin     , pivot_point[2])
		ret_cuboids[3] = Cuboid(self.xmin     , pivot_point[0], pivot_point[1], self.ymax     , self.zmin     , pivot_point[2])
		ret_cuboids[4] = Cuboid(self.xmin     , pivot_point[0], self.ymin     , pivot_point[1], pivot_point[2], self.zmax)
		ret_cuboids[5] = Cuboid(pivot_point[0], self.xmax     , self.ymin     , pivot_point[1], pivot_point[2], self.zmax)
		ret_cuboids[6] = Cuboid(pivot_point[0], self.xmax     , pivot_point[1], self.ymax     , pivot_point[2], self.zmax)
		ret_cuboids[7] = Cuboid(self.xmin     , pivot_point[0], pivot_point[1], self.ymax     , pivot_point[2], self.zmax)

		return ret_cuboids