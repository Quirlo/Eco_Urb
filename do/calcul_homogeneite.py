import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

def calculer_indice_homogeneite_entropie(fichier_entree, fichier_sortie, fichier_pct_sociaux):
    df = pd.read_csv(fichier_entree, sep=';')
    df_pct = pd.read_csv(fichier_pct_sociaux, sep=';')

    cols = ['CS2', 'CS3', 'CS5', 'CS6']

    def indice_homogeneite(row):
        total = row[cols].sum()
        if total == 0:
            return np.nan
        parts = row[cols] / total
        entropie = -np.sum([p * np.log(p) for p in parts if p > 0])
        max_entropie = np.log(len(cols))
        indice = (1 - entropie / max_entropie) * 100
        return round(indice, 2)

    df['Indice_Homogeneite'] = df.apply(indice_homogeneite, axis=1)

    df_merged = pd.merge(df, df_pct[['AAV2020', 'PCT_SOCIAUX']], on='AAV2020', how='left')

    # ➕ Sélection uniquement des colonnes : AAV2020, Indice_Homogeneite, PCT_SOCIAUX
    colonnes_a_garder = ['AAV2020', 'Indice_Homogeneite', 'PCT_SOCIAUX']
    df_final = df_merged[colonnes_a_garder]

    # ➕ Trier par la colonne PCT_SOCIAUX en ordre croissant
    df_final_sorted = df_final.sort_values(by='PCT_SOCIAUX', ascending=True)

    # Sauvegarde du fichier trié dans le même dossier que les inputs
    df_final_sorted.to_csv(fichier_sortie, sep=';', index=False)
    print(f"✅ Fichier final trié et enregistré dans 'input/' ici : {fichier_sortie}")

# 🔁 Exécution directe
if __name__ == "__main__":
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "input"))

    fichier_entree = os.path.join(base_path, "resident_actif.csv")
    fichier_sortie = os.path.join(base_path, "indice_homogeneite.csv")
    fichier_pct = os.path.join(base_path, "taux_logementsoc.csv")

    calculer_indice_homogeneite_entropie(fichier_entree, fichier_sortie, fichier_pct)

