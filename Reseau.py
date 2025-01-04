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
        # Implémentation : Vérifier que chaque noeud est relié directement ou indirectement à l'entrée
        if self.noeud_entree == -1:
            return False

        visited = set()
        stack = [self.noeud_entree]

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                for arc in self.arcs:
                    if arc[0] == current and arc[1] not in visited:
                        stack.append(arc[1])
                    elif arc[1] == current and arc[0] not in visited:
                        stack.append(arc[0])

        return len(visited) == len(self.noeuds)

    def valider_distribution(self, t: Terrain) -> bool:
     
        clients = t.get_clients()
        client_positions = set(clients)
        connected_positions = {self.noeuds[n] for n in self.noeuds}

        return client_positions.issubset(connected_positions)

    def configurer(self, t: Terrain):
        self.noeud_entree, self.noeuds, self.arcs  = self.strat.configurer(t)

    def afficher(self) -> None:
        # Implémentation d'un affichage ASCII simple
        for n, coords in self.noeuds.items():
            print(f"Noeud {n}: {coords}")
        for arc in self.arcs:
            print(f"Arc: {arc}")

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
                        print(" ", end="")
                else:
                    if c == Case.OBSTACLE:
                        print("T", end="")
                    elif c == Case.CLIENT:
                        print("C", end="")
                    elif c == Case.VIDE:
                        print("+", end="")
                    elif c == Case.ENTREE:
                        print("E", end="")
                    else:
                        print(" ", end="")
            print()

    def calculer_cout(self, t: Terrain) -> float:
        cout = 0
        for _ in self.arcs:
            cout += 1.5
        for n in self.noeuds.values():
            if t[n[0]][n[1]] == Case.OBSTACLE:
                cout += 2
            else:
                cout += 1
        return cout
