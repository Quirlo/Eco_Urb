import pandas as pd

def nettoyer_composition_commune(fichier_source, fichier_destination):
    # Charger directement en considérant que la 1ère ligne est l'en-tête
    df = pd.read_csv(fichier_source, sep=";", header=0, dtype=str)

    # Nettoyer les colonnes (enlever espaces autour des noms de colonnes)
    df.columns = [col.strip() for col in df.columns]

    # Vérification de sécurité : est-ce que 'CODEGEO' existe ?
    if "CODGEO" not in df.columns:
        raise ValueError("Erreur : colonne 'CODEGEO' non trouvée dans le fichier.")

    # Nettoyer les contenus (enlever espaces dans toutes les cellules)
    for col in df.columns:
        df[col] = df[col].str.strip()

    # Supprimer les lignes où CODEGEO est vide
    df = df.dropna(subset=["CODGEO"])

    # Sauvegarder proprement
    df.to_csv(fichier_destination, sep=";", index=False, encoding="utf-8")

    print(f"✅ Fichier nettoyé '{fichier_destination}' créé avec {len(df)} lignes.")

if __name__ == "__main__":
    nettoyer_composition_commune("composition_communial1.csv", "../input/composition_commune.csv")

