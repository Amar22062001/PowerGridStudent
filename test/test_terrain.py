import unittest
import xmlrunner

from Terrain import Terrain, Case

class TestTerrain(unittest.TestCase):

    def test_chargement(self):
        t = Terrain()
        t.charger("terrain.txt")
        self.assertIsNotNone(t.cases)

# Autres tests restent inchangés.
