
import unittest
import xmlrunner

from Terrain import Terrain, Case

class TestTerrain(unittest.TestCase):

    def test_chargement(self):
        t = Terrain()
        t.charger("terrains/t1.txt")

        self.assertEqual(t.largeur, 21)
        self.assertEqual(t.hauteur, 10)
        self.assertEqual(t.cases[0][0], Case.VIDE)
        self.assertEqual(t.cases[2][10], Case.CLIENT)
        self.assertEqual(t.cases[4][17], Case.CLIENT)
        self.assertEqual(t.cases[7][6], Case.CLIENT)
        self.assertEqual(t.cases[9][17], Case.ENTREE)

    def test_chargement_t2(self):
        t = Terrain()
        t.charger("terrains/t2.txt")

        self.assertEqual(t.largeur, 21)
        self.assertEqual(t.hauteur, 10)
        self.assertEqual(t.cases[0][0], Case.VIDE)
        self.assertEqual(t.cases[5][4], Case.ENTREE)
        self.assertEqual(t.cases[1][3], Case.CLIENT)
        self.assertEqual(t.cases[1][20], Case.CLIENT)
        self.assertEqual(t.cases[3][9], Case.CLIENT)
        self.assertEqual(t.cases[6][19], Case.CLIENT)
        self.assertEqual(t.cases[8][7], Case.CLIENT)
        self.assertEqual(t.cases[8][19], Case.CLIENT)
        self.assertEqual(t.cases[9][3], Case.CLIENT)

    def test_accesseur(self):
        t = Terrain()
        t.cases = [
            [Case.ENTREE, Case.VIDE, Case.VIDE],
            [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]
        self.assertEqual(t[0][0], Case.ENTREE)
        self.assertEqual(t[0][1], Case.VIDE)
        self.assertEqual(t[1][2], Case.CLIENT)

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))
