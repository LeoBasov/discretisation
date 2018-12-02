import unittest
import sys

sys.path.append('../discrete_pack')

from common.geometry import Cuboid

class CuboidTest(unittest.TestCase):
    def test_volume(self):
        cube = Cuboid()

        self.assertEqual(cube.volume, 1.0)

        cube.set(-1.0, 7.0, -13.0, 5.0, 8.0, 11.0)
        ref_vol = 8.0*18*3

        self.assertEqual(cube.volume, ref_vol)

    def test_value_checks(self):
        cube = Cuboid()
        
        with self.assertRaises(Exception):
            cube.set(cube.xmin, -7.0, cube.ymin, cube.ymax, cube.zmin, cube.zmax)

        with self.assertRaises(Exception):
            cube = Cuboid(-1.0, 7.0, -13.0, 5.0, 8.0, -15.0)