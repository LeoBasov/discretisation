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

		if parent is not None:
			self.level = parent.level + 1
		else:
			self.level =  0

	def __iter__(self):
		self.child_no = 0
		self.number_of_children = 8

		return self

	def __next__(self):
		if self.child_no < self.number_of_children:
			ret_child = self.children[self.child_no]
			self.child_no += 1

			return ret_child
		else:
			del(self.child_no)
			del(self.number_of_children)

			raise StopIteration

	def build_next_level(self, pivot_point = None):
		if self.children is not None:
			raise Exception('Leaf.built_next_level', 'Leaf allready has children')
		elif pivot_point is None:
			pivot_point = self.geometry.barycentre

		sub_geometries = self.geometry.subdivide(pivot_point)
		self.children = []

		for geo in sub_geometries:
			self.children.append(Leaf(self, geo))

	def sort_objects(self, objects_value_pairs):
		rest_objects_value_pairs = []

		for pair in objects_value_pairs:
			if self.geometry.check_if_inside(pair[1]):
				self.elements.append(pair[0])
			else:
				rest_objects_value_pairs.append(pair)

		return rest_objects_value_pairs