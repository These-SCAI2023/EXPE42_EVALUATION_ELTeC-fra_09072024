import json
import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def lire_json (chemin):
    with open(chemin) as mon_fichier:
        data = json.load(mon_fichier)
    return data


sns.set_theme(style="whitegrid")
pathdata = "../MISSLABEL_F-score-precision_29102024/*.json"


for path in glob.glob(pathdata):
    print(path)
    liste_FP_NA = []
    liste_label = []
    liste_FP = []
    liste_auteur = []
    liste_version = []
    liste_statut = []
    auteur = path.split("/")[-1].split("_")[0]
    version = path.split("/")[-1].split("_")[1]
    data = lire_json(path)
    for key, value in data.items():
        # print(key, value)
        if key == "Tokens FP (NA)":
            for k , v in value.items():
                # print(k, v)
                liste_statut.append(("FP, non entité"))
                liste_label.append(k)
                liste_FP.append(v)
                liste_auteur.append(auteur)
                liste_version.append(version)
        if key == "Tokens FP (Label Error)":
            for k , v in value.items():
                # print(k,v)
                liste_statut.append(("FP, mauvaise catégorie"))
                liste_label.append(k)
                liste_FP.append(v)
                liste_auteur.append(auteur)
                liste_version.append(version)

    print(len(liste_statut))
    print(len(liste_label))
    print(len(liste_FP))
    print(len(liste_auteur))
    print(len(liste_version))


    tableau = {}
    tableau["Types d'erreurs"] = liste_statut
    tableau["nombre d'entités mal étiquetées (FP)"] = liste_FP
    tableau["Catégories"] = liste_label
    tableau["auteur"] = liste_auteur
    tableau["version"] = liste_version

    data_tab = pd.DataFrame(tableau)
    data_tab = data_tab.sort_values(by="Types d'erreurs")
    print(data_tab)
    # sns.displot(data_tab, x="Statut", hue="Label attribué")
    # sns.catplot(data=data_tab, x="Statut", y="nombre", jitter=False)
    sns.catplot(data=data_tab, x="Types d'erreurs", y="nombre d'entités mal étiquetées (FP)", hue="Catégories", kind="swarm",s=250, palette="colorblind")
    # sns.relplot(data=data_tab, x="Statut", y="nombre", hue="Label attribué", size="nombre")
    # sns.catplot(data=data_tab, x="nombre", y="Statut", hue="Label attribué", kind="violin",)
    plt.ylim([-10,150])
    plt.savefig(f"../MISSLABEL_F-score-precision_29102024/seaborn_plot/{auteur}_{version}_mislabelling.png",dpi=300, bbox_inches="tight")##NER Multi
