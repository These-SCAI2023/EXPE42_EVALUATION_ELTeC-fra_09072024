import numpy as np
from sklearn.metrics import precision_recall_fscore_support


import glob
import csv
import json

def lire_csv(chemin):
    liste_donnees=[]
    with (open(chemin, newline='') as csvfile):
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if "B-LOC" in row[1] or "I-LOC" in row[1]:
            # or "I-LOC" in row[1]:
            # if row[1] == "B-LOC" or row[1] == "I-LOC":
                liste_donnees.append(row[0])
                    # trier_liste=sorted(liste_donnees)
                    # set_donnees=set(liste_donnees)
        return liste_donnees


def lire_json(chemin):
    with open(chemin) as mon_fichier:
        datajson = json.load(mon_fichier)
    return datajson


liste_OCR = ["kraken","kraken4.3.13.dev25","tesseract0.3.10","TesseractFra-PNG"]
mtOCR = liste_OCR[1]
print(mtOCR)
# path_Gold = "EXPE49_NERVAL_ACC-MAJ/ACC-MAJ_DAUDET_MAUPASSANT_une-vie_PP.txt.csv._10000bio"
# path_REF = "EXPE49_NERVAL_ACC-MAJ/DAUDET-MAUPASSANT_petit-chose_REF.txt_spacy-lg-3.7.5-tabO_10000.bio"
# path_REF = "../small-ELTeC-fra-2021-2024_REN/DAUDET/DAUDET_REF/NER/DAUDET_petit-chose_REF.txt_spacy-lg-3.7.5.bio"
# path_OCR = f"../small-ELTeC-fra-2021-2024_REN/DAUDET/DAUDET_OCR/DAUDET_petit-chose_{mtOCR}/NER/DAUDET_petit-chose_{mtOCR}.txt_spacy-lg-3.7.5.bio"
# path_OCR = f"../small-ELTeC-fra-2021-2024_REN/DAUDET/DAUDET_OCR/DAUDET_{mtOCR}/NER/DAUDET_petit-chose_{mtOCR}.txt_spacy-lg-3.7.5.bio"

path_REF = "../small-ELTeC-fra-2021-2024_REN/DAUDET/DAUDET_REF/NER/DAUDET_petit-chose_REF.txt_spacy-lg-3.7.5-liste.json"
path_OCR = f"../small-ELTeC-fra-2021-2024_REN/DAUDET/DAUDET_OCR/DAUDET_petit-chose_{mtOCR}/NER/DAUDET_petit-chose_{mtOCR}.txt_spacy-lg-3.7.5-liste.json"

print(path_OCR)
for pathg in glob.glob(path_REF):
    # print(pathg)
    # true = lire_csv(pathg)
    true = lire_json(pathg)

    print(true)


for pathr in glob.glob(path_OCR):
    print(pathr)
    # pred = lire_csv(pathr)
    pred = lire_json(pathr)
    print(pred)

intersect = set(pred).intersection(set(true))
print("Intersection : ",len(intersect))

print(" REF DAUDET", len(true))
print("OCR DAUDET", len(pred))
liste_pred=[]
liste_true=[]
for element1, element2 in zip(pred, true):
    liste_pred.append(element1)
    liste_true.append(element2)

y_true = np.array(liste_true)
y_pred = np.array(liste_pred)
# print("REF-----",y_true)
# print("OCR-------",y_pred)
# nna = precision_recall_fscore_support(y_true, y_pred)
macro = precision_recall_fscore_support(y_true, y_pred, average='macro')
micro = precision_recall_fscore_support(y_true, y_pred, average='micro')
w = precision_recall_fscore_support(y_true, y_pred, average='weighted')
# print(nna)
print(macro)
print(micro)
print(w)

# categorie = precision_recall_fscore_support(y_true, y_pred, average=None,
# labels=['B-LOC', 'B-PER', 'B-MISC', 'B-ORG'])
# print(categorie)