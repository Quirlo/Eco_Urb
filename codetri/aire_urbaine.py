import pandas as pd

def nettoyer_aire_urbaine(fichier_source, fichier_destination):
    # Lire tout le fichier sans sauter de lignes
    df_brut = pd.read_csv(fichier_source, sep=";", header=None, dtype=str)

    # Chercher la ligne où il y a 'AAV2020'
    idx_header = df_brut.apply(lambda row: row.astype(str).str.contains("AAV2020").any(), axis=1)
    header_row = df_brut[idx_header].index[0]

    # Lire à nouveau, en indiquant que c'est cette ligne le header
    df = pd.read_csv(fichier_source, sep=";", skiprows=header_row, dtype=str)

    # La première ligne devient l'en-tête
    df.columns = [col.strip() for col in df.columns]
    df = df.drop(0)  # Supprimer la ligne d'en-tête qui était aussi présente

    # Nettoyer les espaces dans AAV2020
    if "AAV2020" in df.columns:
        df["AAV2020"] = df["AAV2020"].str.strip()

    # Supprimer les lignes où AAV2020 est vide
    df = df.dropna(subset=["AAV2020"])

    # Sauvegarder
    df.to_csv(fichier_destination, sep=";", index=False, encoding="utf-8")

    print(f"✅ Fichier nettoyé '{fichier_destination}' créé avec {len(df)} lignes.")

if __name__ == "__main__":
    nettoyer_aire_urbaine("aire_urbaine1.csv", "../input/aire_urbaine.csv")
