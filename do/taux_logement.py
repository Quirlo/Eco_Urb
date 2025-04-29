import pandas as pd

def charger_donnees(chemin):
    """
    Charge un fichier CSV et retourne un DataFrame avec GEO et OBS_VALUE seulement.
    """
    df = pd.read_csv(chemin, sep=";", usecols=["GEO", "OBS_VALUE"], dtype=str)
    df["OBS_VALUE"] = pd.to_numeric(df["OBS_VALUE"], errors="coerce")
    return df.dropna()

def calculer_taux(df_total, df_sociaux):
    """
    Fusionne les deux DataFrames et calcule le taux de logements sociaux.
    """
    df = pd.merge(df_total, df_sociaux, on="GEO", suffixes=('_TOTAL', '_SOCIAUX'))
    df["PCT_SOCIAUX"] = round((df["OBS_VALUE_SOCIAUX"] / df["OBS_VALUE_TOTAL"]) * 100, 2)
    return df

def sauvegarder(df, chemin_sortie):
    """
    Sauvegarde les résultats avec renommage de colonnes.
    """
    df_final = df.rename(columns={
        "GEO": "AAV2020",
        "OBS_VALUE_SOCIAUX": "LOG_SOCIAUX",
        "OBS_VALUE_TOTAL": "LOG_TOTAL"
    })[["AAV2020", "LOG_SOCIAUX", "LOG_TOTAL", "PCT_SOCIAUX"]]
    
    df_final = df_final.sort_values(by="PCT_SOCIAUX", ascending=False)
    df_final.to_csv(chemin_sortie, sep=";", index=False)

def main():
    fichier_total = "../input/logements_total.csv"
    fichier_sociaux = "../input/logements_sociaux.csv"
    fichier_resultat = "../input/taux_logementsoc.csv"

    # Chargement
    df_total = charger_donnees(fichier_total)
    df_sociaux = charger_donnees(fichier_sociaux)

    # Calcul
    df_resultat = calculer_taux(df_total, df_sociaux)

    # Sauvegarde
    sauvegarder(df_resultat, fichier_resultat)
    print(f"✅ Résultat sauvegardé dans {fichier_resultat}")

if __name__ == "__main__":
    main()
