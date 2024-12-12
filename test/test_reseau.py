import unittest
import xmlrunner

from Reseau import Reseau
from Terrain import Terrain, Case

class TestReseau(unittest.TestCase):

    def test_definition_entree(self):
        r = Reseau()
        r.noeuds[1] = (0, 0)
        r.definir_entree(1)
        self.assertEqual(r.noeud_entree, 1)

    def test_ajout_noeud(self):
        r = Reseau()
        r.ajouter_noeud(1, (0, 0))
        self.assertIn(1, r.noeuds)

    def test_ajout_arc(self):
        r = Reseau()
        r.ajouter_noeud(1, (0, 0))
        r.ajouter_noeud(2, (1, 0))
        r.ajouter_arc(1, 2)
        self.assertIn((1, 2), r.arcs)

# Les autres tests restent inchangés.
