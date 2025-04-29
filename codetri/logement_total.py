import pandas as pd

# Charger le CSV
df = pd.read_csv(
    "DS_RP_LOGEMENT_PRINC_data.csv",
    sep=";",
    quotechar='"',
    dtype=str
)

# Conversion du TIME_PERIOD en numérique
df["TIME_PERIOD"] = pd.to_numeric(df["TIME_PERIOD"], errors="coerce")

# Appliquer les filtres
df_filtre = df[
    (df["GEO_OBJECT"].str.startswith("AAV2020")) &
    (df["TIME_PERIOD"] == 2021) &
    (df["RP_MEASURE"] == "DWELLINGS") &  # DWELLINGS obligatoire
    (df["OCS"] == "_T") &
    (df["L_STAY"] == "_T") &
    (df["TDW"] == "_T") &
    (df["TOH"] == "_T") &
    (df["CARS"] == "_T") &
    (df["TSH"] == "_T")
]

# Trier par GEO
df_filtre = df_filtre.sort_values(by="GEO").reset_index(drop=True)

# Sauvegarder dans le dossier ../input/
df_filtre.to_csv("../input/logements_total.csv", sep=";", index=False)

print(f"✅ Fichier 'logements_total.csv' créé dans '../input/' avec {len(df_filtre)} lignes, trié par GEO.")


