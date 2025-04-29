import pandas as pd

# Charger avec les bons paramètres
df = pd.read_csv(
    "DS_RP_LOGEMENT_PRINC_data.csv",
    sep=";",
    quotechar='"',
    dtype=str
)

# Convertir TSH et TIME_PERIOD en numériques
df["TSH"] = pd.to_numeric(df["TSH"], errors="coerce")
df["TIME_PERIOD"] = pd.to_numeric(df["TIME_PERIOD"], errors="coerce")

# Appliquer les 4 filtres
df_filtre = df[
    (df["TSH"] == 221) &
    (df["RP_MEASURE"] == "DWELLINGS") &
    (df["GEO_OBJECT"].str.startswith("AAV2020")) &
    (df["TIME_PERIOD"] == 2021)
]

# Trier par GEO en ordre croissant
df_filtre = df_filtre.sort_values(by="GEO").reset_index(drop=True)

# Sauvegarder directement dans input/
df_filtre.to_csv("../input/logements_sociaux.csv", sep=";", index=False)

print(f"✅ Fichier 'logements_sociaux.csv' créé directement dans le dossier 'input/' avec {len(df_filtre)} lignes, trié par GEO.")



