from Terrain import Terrain, Case

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        noeuds = {}
        arcs = []
        entree = t.get_entree()
        noeuds[0] = entree
        print(f"Entrée électrique détectée à la position {entree}")

        while True:
            print("\nOptions :")
            print("1. Ajouter un nœud")
            print("2. Ajouter un arc")
            print("3. Afficher le réseau")
            print("4. Terminer la configuration")

            choix = input("Faites un choix : ")
            if choix == "1":
                x = int(input("Coordonnée X du nœud : "))
                y = int(input("Coordonnée Y du nœud : "))
                identifiant = len(noeuds)
                noeuds[identifiant] = (x, y)
                print(f"Nœud ajouté : {identifiant} à la position {(x, y)}")

            elif choix == "2":
                n1 = int(input("ID du premier nœud : "))
                n2 = int(input("ID du second nœud : "))
                if n1 in noeuds and n2 in noeuds:
                    arcs.append((n1, n2))
                    print(f"Arc ajouté entre {n1} et {n2}")
                else:
                    print("Un ou les deux nœuds n'existent pas.")

            elif choix == "3":
                print("\nNœuds :")
                for nid, coord in noeuds.items():
                    print(f"  {nid}: {coord}")
                print("\nArcs :")
                for arc in arcs:
                    print(f"  {arc}")

            elif choix == "4":
                print("Configuration terminée.")
                break

            else:
                print("Choix invalide. Veuillez réessayer.")

        return 0, noeuds, arcs

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        # Configuration automatique simplifiée
        noeuds = {}
        arcs = []
        clients = t.get_clients()
        entree = t.get_entree()

        noeuds[0] = entree

        for i, client in enumerate(clients, start=1):
            noeuds[i] = client
            arcs.append((0, i))

        return 0, noeuds, arcs