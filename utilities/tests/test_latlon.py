import unittest
import utilities.src.latlon as latlon

class LatLonTest(unittest.TestCase):
    p1: latlon.Point
    p2: latlon.Point

    def setUp(self):
        self.p1 = latlon.Point(1.14, 1.21)
        self.p2 = latlon.Point(1.52, 1.35)

    def test_distance(self):
        self.assertAlmostEqual(45.03, latlon.distance(self.p1, self.p2), delta=0.6)

    def get_lanlonkey(self):
        expected = [self.p1, self.p2]
        keyfunction = latlon.get_lanlonkey(latlon.Point(1, 1))
        res = sorted([self.p2, self.p1], key=keyfunction)
        self.assertEqual(expected, res)

if __name__ == "__main__":
    unittest.main()
