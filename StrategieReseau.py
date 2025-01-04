from Terrain import Terrain

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        print("Configuration manuelle :")

        noeuds = {}
        arcs = []

        from Reseau import Reseau

        entree = t.get_entree()
        if entree == (-1, -1):
            print("Pas d'entrée électrique trouvée !")
            return -1, {}, []

        noeud_entree = 0
        noeuds[noeud_entree] = entree
        print(f"Entrée définie en position : {entree}")

        # partie ou on ajoute des nœuds et arcs
        while True:
            print("Terrain actuel :")
            t.afficher()
            print("Configuration actuelle du réseau :")
            for n, coord in noeuds.items():
                print(f"Noeud {n}: {coord}")
            for arc in arcs:
                print(f"Arc: {arc}")

            action = input("Voulez-vous ajouter un noeud (n), un arc (a) ou terminer (q) ? : ").strip()
            if action == "q":
               
                reseau = Reseau()  
                reseau.noeuds = noeuds  
                reseau.arcs = arcs 
                reseau.noeud_entree = noeud_entree 

                if reseau.valider_reseau() and reseau.valider_distribution(t):
                    print("Configuration valide optimale trouvée")
                    print("Cout : {}M€".format(reseau.calculer_cout(t)))
                    reseau.afficher_avec_terrain(t)
                else:
                    print("Pas de configuration valide trouvée.")
                break
            elif action == "n":
                x, y = map(int, input("Coordonnées du nouveau noeud (x, y) : ").split())
                noeud_id = len(noeuds)
                noeuds[noeud_id] = (x, y)
            elif action == "a":
                n1, n2 = map(int, input("Noeuds à relier (n1 n2) : ").split())
                if n1 in noeuds and n2 in noeuds:
                    arcs.append((n1, n2))
                else:
                    print("Noeuds invalides.")

        return noeud_entree, noeuds, arcs
class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        print("Configuration automatique :")

        noeuds = {}
        arcs = []

        entree = t.get_entree()
        if entree == (-1, -1):
            print("Pas d'entrée électrique trouvée !")
            return -1, {}, []

        noeud_entree = 0
        noeuds[noeud_entree] = entree

        clients = t.get_clients()
        for i, client in enumerate(clients):
            noeuds[i + 1] = client
            arcs.append((noeud_entree, i + 1))

        return noeud_entree, noeuds, arcs
