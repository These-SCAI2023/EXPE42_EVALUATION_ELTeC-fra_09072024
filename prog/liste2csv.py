import glob
import json
from collections import Counter
import csv


def lire_json (chemin):
    with open(chemin) as mon_fichier:
        data = json.load(mon_fichier)
    return data
def model_ocr(chemin):

    ocr_mod=chemin.split("/")[5]
    ocr_mod = ocr_mod.split("_")[-1]
    # liste_moteur.append(ocr_mod)
    # moteur = set(liste_moteur)
    return ocr_mod

def corpus(chemin):
    ocr_mod="/".join(chemin.split("/")[:3])
    # ocr_mod = ocr_mod.split("_")[0]
    return ocr_mod

corpusa=["DATA_TGB-2023_spaCy3.5.1_Distance","DATA_ELTeC-fra_spaCy3.5.1","DATA_ELTeC-eng_spaCy3.5.1","DATA_ELTeC-Por_spaCy3.5.1"]
corpa=corpusa[1]
path_corpora = f"../DATA_spaCy3.5.1_ENliste_compte-set_globale-et-par-auteur/{corpa}/*"

liste_res=[]
for gen_path in glob.glob(path_corpora):
    # print("_____________",gen_path)
    corp = corpus(gen_path)
    # print(corp)
    paths_ocr="%s/*OCR/*/NER/*liste.json" % gen_path
    paths_ref = "%s/*REF/NER/*liste.json" % gen_path

    for path_ocr in glob.glob(paths_ocr):
        # print(path_ocr)
        dico_resultat = {}
        pathoutpu=path_ocr.split("/")[-1]
        print(pathoutpu)
        data_ocr=lire_json(path_ocr)
        # print(data_ocr)
        for data in data_ocr:
            if data in dico_resultat:
                dico_resultat[data]+=1
            else:
                dico_resultat[data] = 1
        print(dico_resultat)
        myfile = open(f'../DATA_spaCy3.5.1_ENliste_compte-set_globale-et-par-auteur/DATA_CSV/{pathoutpu}.csv', 'w')
        mywriter = csv.writer(myfile, delimiter=';', lineterminator='\n')
        for k, v in dico_resultat.items():
            mywriter.writerow([k, v])
# #
    for path_ref in glob.glob(paths_ref):
        # print(path_ref)
        dico_resultat = {}
        pathoutpu_ref = path_ref.split("/")[-1]
        data_ref=lire_json(path_ref)
        for data in data_ref:
            if data in dico_resultat:
                dico_resultat[data]+= 1
            else:
                dico_resultat[data] = 1
        myfile = open(f'../DATA_spaCy3.5.1_ENliste_compte-set_globale-et-par-auteur/DATA_CSV/{pathoutpu_ref}.csv', 'w')
        mywriter = csv.writer(myfile, delimiter=';', lineterminator='\n')
        for k, v in dico_resultat.items():
            mywriter.writerow([k, v])
# print(dico_resultat)


        # with open(f'../DATA_spaCy3.5.1_ENliste_compte-set_globale-et-par-auteur/DATA_CSV/{pathoutpu}.csv', 'a',
        #           newline='') as csvfile:
        #         spamwriter = csv.writer(csvfile, delimiter=';',
        #                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #         spamwriter.writerow(["Entite", "Freq"])
        #         for ent_r in data_ref:
        #             freq_r = Counter(data_ref).get(ent_r)
        #             dic_res[ent_r]=
        #             spamwriter.writerow(set(liste_res))

# ints = [1, 2, 3, 4, 5]
# item = 3
#
#     freq = Counter(ints).get(item)
#     print(freq)