import numpy as np
from sklearn.metrics import precision_recall_fscore_support


import glob
import csv

def lire_csv(chemin):
    liste_donnees=[]
    with (open(chemin, newline='') as csvfile):
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if "B-" in row[1] or "I-" in row[1]:
        #     # if row[1] == "B-LOC" or row[1] == "I-LOC":
                liste_donnees.append(row[0])
                    # trier_liste=sorted(liste_donnees)
                    # set_donnees=set(liste_donnees)
        return liste_donnees


path_Gold = "EXPE49_NERVAL_ACC-MAJ/ACC-MAJ_DAUDET_MAUPASSANT_une-vie_PP.txt.csv._10000bio"
path_REF = "EXPE49_NERVAL_ACC-MAJ/DAUDET-MAUPASSANT_petit-chose_REF.txt_spacy-lg-3.7.5-tabO_10000.bio"

for pathg in glob.glob(path_Gold):
    # print(pathg)
    true = lire_csv(pathg)
    print(true)


for pathr in glob.glob(path_REF):
    print(pathr)
    pred = lire_csv(pathr)
    print(pred)


# print("ACC-MAJ_DAUDET_MAUPASSANT", len(true))
# print("DAUDET-MAUPASSANT", len(pred))
# liste_pred=[]
# liste_true=[]
# for element1, element2 in zip(pred, true):
#     liste_pred.append(element1)
#     liste_true.append(element2)
#
# y_true = np.array(liste_true)
# y_pred = np.array(liste_pred)
# print(y_true)
# print(y_pred)
# macro = precision_recall_fscore_support(y_true, y_pred, average='macro')
# micro = precision_recall_fscore_support(y_true, y_pred, average='micro')
# w = precision_recall_fscore_support(y_true, y_pred, average='weighted')
# print(macro)
# print(micro)
# print(w)