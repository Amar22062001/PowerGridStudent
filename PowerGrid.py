from Terrain import Terrain
from Reseau import Reseau

from StrategieReseau import StrategieReseauManuelle

if __name__ == "__main__":
    # Demande à l'utilisateur de choisir un terrain
    choix_terrain = input("Choisissez un terrain (t1 ou t2) : ").strip()
    fichier_terrain = "terrains/t1.txt" if choix_terrain == "t1" else "terrains/t2.txt"

    reseau = Reseau()

    terrain = Terrain()
    terrain.charger(fichier_terrain)
    print("Terrain chargé :")
    terrain.afficher()

    print("======= Configuration Automatique")
    reseau.configurer(terrain)
    if reseau.valider_reseau() and reseau.valider_distribution(terrain):
        print("Configuration valide simple trouvée")
        print("Cout : {}M€".format(reseau.calculer_cout(terrain)))
        reseau.afficher_avec_terrain(terrain)
    else:
        print("Pas de configuration valide trouvée.")

    print("======= Configuration Manuelle")
    reseau.set_strategie(StrategieReseauManuelle())
    reseau.configurer(terrain)
    if reseau.valider_reseau() and reseau.valider_distribution(terrain):
        print("Configuration valide optimale trouvée")
        print("Cout : {}M€".format(reseau.calculer_cout(terrain)))
        reseau.afficher_avec_terrain(terrain)
    else:
        print("Pas de configuration valide optimale trouvée.")
