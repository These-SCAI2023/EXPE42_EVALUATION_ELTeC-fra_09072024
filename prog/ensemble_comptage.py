import glob
import json

def lire_json (chemin):
    with open(chemin) as mon_fichier:
        data = json.load(mon_fichier)
    return data
def model_ocr(chemin):
    # ocr_mod=chemin.split("/")[4]REN Normale
    ocr_mod = chemin.split("/")[6]##5 Correction 6 archéo
    ocr_mod = ocr_mod.split("_")[-1]
    # liste_moteur.append(ocr_mod)
    # moteur = set(liste_moteur)
    return ocr_mod

def model_REN(chemin):
    REN_version = chemin.split("_")[-1]
    REN_version = REN_version.split("-liste")[0]
    return REN_version


def stocker(chemin, contenu):
    w = open(chemin, "w")
    w.write(json.dumps(contenu, indent=2))
    w.close()
    # print(chemin)
    return chemin

path_corpora = f"../ARCHEO_Correction_Distances/small-*fra-c*/*3.5.1"
dico_compte={}
for file in glob.glob(f"{path_corpora}/*/*OCR/*/NER/*-liste.json"):
    OCR= model_ocr(file)
    NER=model_REN(file)
    print(file)
    print(OCR)
    print(NER)
    if "lg" in NER and OCR =="kraken":
        data_liste = lire_json(file)
        data_set=set(data_liste)
        print(len(data_set))
        dico_compte[file] = len(data_set)
        stocker(f"{OCR}-{NER}_comptage.json",dico_compte)

# res_liste=[
#
#   ]
# res_set=set(res_liste)
# print(len(res_liste))
# print(len(res_set))


