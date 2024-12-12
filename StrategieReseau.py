from Terrain import Terrain, Case

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        # Configuration manuelle : suppose qu'il y a une entrée à (0,0) et des clients dans les cases adjacentes.
        noeuds = {0: (0, 0)}
        arcs = []
        for i, ligne in enumerate(t.cases):
            for j, case in enumerate(ligne):
                if case == Case.CLIENT:
                    noeuds[len(noeuds)] = (i, j)
                    arcs.append((0, len(noeuds) - 1))
        return 0, noeuds, arcs

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        # Configuration automatique : suppose qu'il connecte tous les clients à la première entrée trouvée.
        noeuds = {}
        arcs = []
        entree = None
        for i, ligne in enumerate(t.cases):
            for j, case in enumerate(ligne):
                if case == Case.ENTREE and entree is None:
                    entree = len(noeuds)
                    noeuds[entree] = (i, j)
                elif case == Case.CLIENT:
                    noeuds[len(noeuds)] = (i, j)
                    arcs.append((entree, len(noeuds) - 1))
        return entree if entree is not None else -1, noeuds, arcs
