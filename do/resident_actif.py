import pandas as pd

# Charger les deux fichiers
df_base = pd.read_csv("../codetri/base_filtrée_sommée.csv", sep=";")
df_compo = pd.read_csv("../input/composition_commune.csv", sep=";")

# Assurer que les colonnes COM et CODGEO sont bien des chaînes de caractères
df_base["COM"] = df_base["COM"].astype(str)
df_compo["CODGEO"] = df_compo["CODGEO"].astype(str)

# Fusionner les deux sur COM = CODGEO
df_merge = df_base.merge(df_compo[["CODGEO", "AAV2020"]], left_on="COM", right_on="CODGEO", how="left")

# Vérifier si des correspondances sont manquantes
if df_merge["AAV2020"].isnull().any():
    print("⚠️ Attention : certaines COM n'ont pas de correspondance CODGEO -> AAV2020 !")

# Grouper par AAV2020 et additionner CS2, CS3, CS5, CS6
df_result = df_merge.groupby("AAV2020")[["CS2", "CS3", "CS5", "CS6"]].sum().reset_index()

# Sauvegarder dans un nouveau fichier
df_result.to_csv("../input/resident_actif.csv", sep=";", index=False, encoding="utf-8")

print("✅ Fichier généré : '../output/aav2020_somme_cs.csv'")
