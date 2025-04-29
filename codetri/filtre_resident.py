import pandas as pd

def filtrer_et_sommer_colonnes(input_csv, output_csv):
    # Charger le fichier
    df = pd.read_csv(input_csv, sep=";", dtype=str)

    # Convertir toutes les colonnes en numériques sauf les 4 premières (au cas où il y a des erreurs)
    for col in df.columns[4:]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # Sélectionner les 4 premières colonnes
    colonnes_quatre_premieres = df.columns[:4].tolist()

    # Créer les nouvelles colonnes sommées
    df_resultat = df[colonnes_quatre_premieres].copy()

    for code in ['CS2', 'CS3', 'CS5', 'CS6']:
        colonnes_cs = [col for col in df.columns if code in col]
        if colonnes_cs:
            df_resultat[code] = df[colonnes_cs].sum(axis=1)

    # Sauvegarder
    df_resultat.to_csv(output_csv, sep=";", index=False, encoding="utf-8")
    print(f"✅ Fichier créé : {output_csv} avec colonnes {colonnes_quatre_premieres + ['CS2', 'CS3', 'CS5', 'CS6']}.")

if __name__ == "__main__":
    filtrer_et_sommer_colonnes("base-ic-activite-residents-2021.CSV", "../input/base_filtrée_sommée.csv")


