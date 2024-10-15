import glob
import json
import pandas as pd
from IPython.display import display
from scipy import stats


def lire_json (chemin):
    with open(chemin) as mon_fichier:
        data = json.load(mon_fichier)
    return data

def stocker(chemin, contenu):
    w = open(chemin, "w")
    w.write(json.dumps(contenu, indent=2))
    w.close()
    # print(chemin)
    return chemin

path_corpora = "../small-ELTeC-fra-2021-2024_REN/*/*OCR/*"
liste_auteur = []
liste_moteur_ocr = []
liste_cos = []
liste_ren = []
dico_cos = {}
for gen_path in glob.glob(path_corpora):
    print(gen_path)
    for ocr_path in glob.glob(f"{gen_path}/SIM/*json"):
        auteur = ocr_path.split("/")[-1].split(".")[0].split("_")[1]
        moteur_ocr = ocr_path.split("/")[-1].split(".")[0].split("_")[-1]
        # print("auteur", auteur)
        # print("moteur_ocr", moteur_ocr)
        data=lire_json(ocr_path)
        # print(data)

        for key, value in data.items():
            # print(key)
            if key == "jaccard":
                liste_auteur.append(auteur)
                liste_moteur_ocr.append(moteur_ocr)
                liste_ren.append("txt")
                for rc in value:
                    liste_cos.append(rc)
        # print(len(liste_auteur))
        # print(len(liste_moteur_ocr))
        # print(len(liste_cos))
        # print(liste_cos)
    for ren_path in glob.glob(f"{gen_path}/NER/SIM/*json"):
        print(ren_path)
        auteur = ren_path.split("/")[-1].split(".")[0].split("_")[1]
        moteur_ocr = ren_path.split("/")[-1].split(".")[0].split("_")[-1]
        ren = "-".join(ren_path.split("/")[-1].split("_")[-1].split("-")[:2])
        # print("auteur", auteur)
        # print("moteur_ocr", moteur_ocr)
        # print("moteur_ren", ren)
        data = lire_json(ren_path)
        # print(data)

        for key, value in data.items():
            # print(key)
            if key == "cosinus":
                liste_auteur.append(auteur)
                liste_moteur_ocr.append(moteur_ocr)
                liste_ren.append(ren)
                for rc in value:
                    liste_cos.append(rc)
    # print(len(liste_auteur))
    # print(len(liste_moteur_ocr))
    # print(len(liste_cos))
    # print(len(liste_ren))
    # print(liste_cos)
    # print(liste_ren)
dico_cos["auteur"] = liste_auteur
dico_cos["moteur_ocr"] = liste_moteur_ocr
dico_cos["cos"] = liste_cos
dico_cos["REN"] = liste_ren

dico_pvalue={}
data_tab = pd.DataFrame(dico_cos)
# display(data_tab)

OCR_liste = set(dico_cos["moteur_ocr"])
liste_liste_x = []
dico_resultat = {}


for o in OCR_liste:
    data_tab1 = data_tab.query('moteur_ocr == @o ')
    # display(data_tab1)

    REN_liste = set(dico_cos["REN"])
    dico_resultat[o]={}
    liste_liste_y = []
    for r in REN_liste :

        data_tab2 = data_tab1.query('REN == @r ')
        display(data_tab2)
        print("_____________________")
        liste_x = data_tab2['cos'].tolist()
        dico_resultat[o][r] = liste_x
# print(dico_resultat.keys())
dico_spearman = {}
for key, values in dico_resultat.items():
    # print(key)
    dico_spearman[key] = {}
    for k, v in values.items():
        if k != "txt":
            dico_spearman[key][k]={}
            # print(k)

            res = stats.spearmanr(values["txt"], values[k])
            # res_f = res.statistic
            dico_spearman[key][k]["resultats"] = res.statistic
            dico_spearman[key][k]["p-value"] = res.pvalue
            # print(res_f)
print(dico_spearman)
stocker("../jaccard_spearman_correlation.json", dico_spearman)






