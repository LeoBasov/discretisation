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

from discrete_pack.common.geometry import Cuboid

class Octree:
	def __init__(self):
		self.main_leaf = Leaf()

class Leaf:
	def __init__(self, parent = None, geometry = Cuboid()):
		self.parent = parent
		self.children = None
		self.geometry = geometry
		self.elements = []

	def built_next_level(self, pivot_point = None):
		if self.children is not None:
			raise Exception('Leaf.built_next_level', 'Leaf allready has children')
		elif pivot_point is None:
			pivot_point = self.geometry.barycentre

		sub_geometries = self.geometry.subdivide(pivot_point)
		self.children = []

		for geo in sub_geometries:
			self.children.append(Leaf(self, geo))
