import glob
import json
import re
import pandas as pd
from IPython.display import display
from scipy import stats
from renommage import *


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
corpus = path_corpora.split("/")[1]
liste_auteur = []
liste_moteur_ocr = []
liste_cos = []
liste_ren = []
dico_cos = {}
name_metric=["cosinus","jaccard"]
nm=name_metric[-1]
for gen_path in glob.glob(path_corpora):
    # print(gen_path)
    for ocr_path in glob.glob(f"{gen_path}/SIM/*json"):
        auteur = ocr_path.split("/")[-1].split(".")[0].split("_")[1]
        moteur_ocr = ocr_path.split("/")[-1].split("_")[-1]  ## A remettre en ordre pour d'autres corpus que correction
        moteur_ocr = re.split(".txt|.json", moteur_ocr)[0]
        moteur_ocr = nommage(moteur_ocr)
        # print("auteur", auteur)
        print("moteur_ocr", moteur_ocr)
        data=lire_json(ocr_path)
        # print(data)

        for key, value in data.items():
            # print(key)
            if key == nm:
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
        # print(ren_path)
        auteur = ren_path.split("/")[-1].split(".")[0].split("_")[1]
        # moteur_ocr = ren_path.split("/")[-1].split(".")[0].split("_")[-1]
        moteur_ocr = ocr_path.split("/")[-1].split("_")[-1]  ## A remettre en ordre pour d'autres corpus que correction
        moteur_ocr = re.split(".txt|.json", moteur_ocr)[0]
        moteur_ocr = nommage(moteur_ocr)
        ren = "-".join(ren_path.split("/")[-1].split("_")[-1].split("-")[:2])
        # print("auteur", auteur)
        # print("moteur_ocr", moteur_ocr)
        # print("moteur_ren", ren)
        data = lire_json(ren_path)
        # print(data)

        for key, value in data.items():
            # print(key)
            if key == nm:
                liste_auteur.append(auteur)
                liste_moteur_ocr.append(moteur_ocr)
                liste_ren.append(ren)
                for rc in value:
                    liste_cos.append(rc)
    # print(len(liste_auteur))
    print(len(liste_moteur_ocr))
    print(liste_moteur_ocr)
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
stocker(f"../{corpus}_dico-liste-distance_{nm}.json", dico_resultat)
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
            dico_spearman[key][k]["spearman.stats"] = res.statistic
            dico_spearman[key][k]["p-value"] = res.pvalue
            # print(res_f)
print(dico_spearman)
print(dico_spearman.keys())
stocker(f"../{corpus}_spearman-correlation_{nm}.json", dico_spearman)
# x = [
#       0.7423045930701048,
#       0.7700800162058138,
#       0.717212562339938,
#       0.6650892665089266,
#       0.7347626141589482,
#       0.7470343310550711,
#       0.6990554414784395,
#       0.7424456368257555,
#       0.7210052552161923,
#       0.7701705985023366,
#       0.7501000667111407
#     ]
# y = [
#       0.36601135120845196,
#       0.3145387111100434,
#       0.3829421380145216,
#       0.3414972256538247,
#       0.2609347476790954,
#       0.6806055143882737,
#       0.31062297175663145,
#       0.2070064740161115,
#       0.30239241816939333,
#       0.17478848939464398,
#       0.3712258182857089
#     ]
# res = stats.spearmanr(x, y)
# print(res.statistic)