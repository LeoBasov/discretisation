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

class Octree:
	def __init__(self):
		self.main_leaf = None

	def built_next_level(self):
		pass

class Leaf:
	def __init__(self, parent = None):
		self.parent = parent
		self.children = [None]*8