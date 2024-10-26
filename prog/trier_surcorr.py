import json
import glob

def lire_fichier(chemin):
    with open(chemin) as json_data:
        EN = json.load(json_data)

        return EN


path_corpora = "../CORRECTION_DISTANCES/small-ELTeC-fra-2021-2024-corr-automatique_REN/AUDOUX/"
dico_compar ={}
for subcorpus in sorted(glob.glob("%s*/"%path_corpora)):
    print(subcorpus)
    for subpath in sorted(glob.glob("%s*dico-voc-freq.json" % subcorpus)):
        print(subpath)
        data_ref = lire_fichier(subpath)
        # print(data_ref)
        nom_vers = subpath.split("/")[-2]
        dico_compar["REF"] = data_ref

    for subpath in sorted(glob.glob("%s*/*dico-voc-freq-nontrier.json" % subcorpus)):
        print(subpath)
        data_ocr = lire_fichier(subpath)
        # print(data_ocr)
        nom_vers_ocr = subpath.split("/")[-2]
        dico_compar[nom_vers_ocr] = data_ocr
# print(dico_compar.keys())
for key, value in dico_compar.items():
    if "AUDOUX_kraken-jspll-pretrain" in key:
        diff = set(value).difference(set(dico_compar["AUDOUX_kraken"]))
        print(diff)