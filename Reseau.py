from Terrain import Terrain, Case
from StrategieReseau import StrategieReseau, StrategieReseauAuto

class Reseau:
    def __init__(self):
        self.strat = StrategieReseauAuto()
        self.noeuds = {}
        self.arcs = []

        self.noeud_entree = -1

    def definir_entree(self, n: int) -> None:
        if n in self.noeuds.keys():
            self.noeud_entree = n
        else:
            self.noeud_entree = -1

    def ajouter_noeud(self, n: int, coords: tuple[int, int]):
        if n >= 0:
            self.noeuds[n] = coords

    def ajouter_arc(self, n1: int, n2: int) -> None:
        if n1 > n2:
            tmp = n2
            n2 = n1
            n1 = tmp
        if n1 not in self.noeuds.keys() or n2 not in self.noeuds.keys():
            return
        if (n1, n2) not in self.arcs:
            self.arcs.append((n1, n2))

    def set_strategie(self, strat: StrategieReseau):
        self.strat = strat

    def valider_reseau(self) -> bool:
        # Valider si tous les noeuds sont connectés à l'entrée
        visites = set()

        def dfs(noeud):
            visites.add(noeud)
            for n1, n2 in self.arcs:
                if n1 == noeud and n2 not in visites:
                    dfs(n2)
                elif n2 == noeud and n1 not in visites:
                    dfs(n1)

        if self.noeud_entree != -1:
            dfs(self.noeud_entree)

        return len(visites) == len(self.noeuds)

    def valider_distribution(self, t: Terrain) -> bool:
        # Valider si tous les clients sont connectés à l'entrée
        for n, coord in self.noeuds.items():
            if t.cases[coord[0]][coord[1]] == Case.CLIENT:
                if not any(n == arc[1] or n == arc[0] for arc in self.arcs):
                    return False
        return True

    def configurer(self, t: Terrain):
        self.noeud_entree, self.noeuds, self.arcs = self.strat.configurer(t)

    def afficher(self) -> None:
        # Afficher les noeuds et les arcs
        print(f"Noeuds : {self.noeuds}")
        print(f"Arcs : {self.arcs}")

    def afficher_avec_terrain(self, t: Terrain) -> None:
        for ligne, l in enumerate(t.cases):
            for colonne, c in enumerate(l):
                if (ligne, colonne) not in self.noeuds.values():
                    if c == Case.OBSTACLE:
                        print("X", end="")
                    elif c == Case.CLIENT:
                        print("C", end="")
                    elif c == Case.VIDE:
                        print("~", end="")
                    elif c == Case.ENTREE:
                        print("E", end="")
                else:
                    print("N", end="")
            print()

    def calculer_cout(self, t: Terrain) -> float:
        cout = 0
        for _ in self.arcs:
            cout += 1.5
        for n in self.noeuds.values():
            if t.cases[n[0]][n[1]] == Case.OBSTACLE:
                cout += 2
            else:
                cout += 1
        return cout
