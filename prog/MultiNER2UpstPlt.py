import json
import glob
from renommage import *



def lire_fichier_json(chemin):
    with open(chemin) as json_data:
        EN = json.load(json_data)
    return EN

def stocker( chemin, contenu):
    #if os.path.exists(chemin)==True:  # Où mettre la sécurité ?
        #print(f"Already Done {chemin}")
    w =open(chemin, "w")
    w.write(json.dumps(contenu , indent = 2))
    w.close()

path_corpora = "../small-ELTeC-fra-2021-2024_REN/*/"

for subcorpus in sorted(glob.glob(path_corpora)):
    dico_upstplt = {}
    dico_upstplt_ref ={}
    print("subcorpus",subcorpus)
    for path in sorted(glob.glob("%s*REF/NER/*liste.json" % subcorpus)):
        print("path REF: ", path )
        data = lire_fichier_json(path)
        # print(data)
        nom_version = path.split("/")[-3].split("_")[-1]
        # print(nom_version)
        nom_ren = path.split("/")[-1].split("_")[-1].split("-liste.json")[0]
        print(nom_ren)
        dico_upstplt_ref[nom_ren] = data
    stocker(f"{path}_MultiNER_dic.json", dico_upstplt_ref)
    for path_ocrs in sorted(glob.glob("%s*OCR/*/NER/*liste.json" % subcorpus)):
        print("path OCRS: ", path_ocrs )
        data_ocr = lire_fichier_json(path_ocrs)
        nom_version = path_ocrs.split("/")[-3].split("_")[-1]
        nom_ocr =nommage(nom_version)
        # print(nom_ocr)
        nom_ren = path_ocrs.split("/")[-1].split("_")[-1].split("-liste.json")[0]
        print(nom_ren)
        dico_upstplt[nom_ren] = data_ocr
    stocker(f"{path_ocrs}_MultiNER_dic.json", dico_upstplt)