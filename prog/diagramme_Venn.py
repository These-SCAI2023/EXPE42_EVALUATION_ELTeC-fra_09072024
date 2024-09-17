import re
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles
import json
import glob
import pandas as pd

# Lire les fichiers json
def read_json(chemin):
    with open(chemin) as json_data:
        data = json.load(json_data)
    return data


# calcul des diagrammes de Venn
def diagramme_venn(liste_en_pp, liste_en_ocr, ocr):
    font2 = {'size': 25}  # use for labels
    plt.rc('font', **font2)  # sets the default font
    plt.rcParams['text.color'] = 'black'  # changes default text colour
    venn2([set(liste_en_pp), set(liste_en_ocr)], set_labels=('EN Réf', 'EN %s' % ocr),
          set_colors=("darkgrey", "darkblue"), alpha=0.5)

    venn2_circles(subsets=(set(liste_en_pp), set(liste_en_ocr)), linestyle="dotted", linewidth=1)
    print(f"Analyse de la version {ocr}")


# stockage des diagrammes de Venn au format png
def stocker_png(nom_fichier):
    plt.gcf().set_size_inches(12, 7)
    plt.subplots_adjust(left=0.03, right=0.8, top=0.9, bottom=0.1)
    plt.savefig(nom_fichier, dpi=300)
    plt.gcf()
    # plt.clf()
    return nom_fichier


# path_data_ocr = "../ARTICLE_Revue-Corpus_16092024/small-*/*/*OCR/*/NER/*-liste.json"
# path_data_ref = "../ARTICLE_Revue-Corpus_16092024/small-*/*/*REF/NER/*-liste.json"
path_data = "../ARTICLE_Revue-Corpus_16092024/small-*/*/*"
# Stockage des données dans des structures listes pour ensuite les stocker dans une structure dictionnaire
# utilisable avec Pandas
dict_global = {}
liste_entit = []
liste_vers = []

for path in glob.glob(path_data):
    # print(path)
    # data = read_json(path)

    for file in glob.glob(f"{path}/*/NER/*liste.json"):
        # print(file)
        data_ocr = read_json(file)
        # print(data)
        vers = file.split("/")[5]
        vers = vers.split("_")[-1]
        liste_vers.append(vers)
        # print(liste_vers)
        for entity in data_ocr:
            liste_entit.append(entity)
            liste_vers.append(vers)

    if "REF" in path:
        vers = path.split("/")[4]
        vers = vers.split("_")[-1]
        # liste_vers.append(vers)
        for file in glob.glob(f"{path}/NER/*liste.json"):
            # print(file)
            data_ref = read_json(file)
            # print(data)
# print(liste_vers)

            for entity in data_ref:
                liste_entit.append(entity)
                liste_vers.append(vers)


print(len(liste_entit))
print(len(liste_vers))
# dict_global["Entite"] = liste_entit
# dict_global["version"] = liste_vers
# print(dict_global)
# data_tab = pd.DataFrame(dict_global)
# display(data_tab)
#
# dic_inter = {}
# for name_ocr in liste_ocr:
#     data_ref = data_tab.query("version=='REF'")
#     data_ocr = data_tab.query("version== @name_ocr")
    # print(data_ocr)

    # diagramme_venn(data_ref.Entite, data_ocr.Entite, name_ocr)
    #
    # dic_inter[name_ocr] = {}
    # intersection = set(data_ref.Entite) & set(data_ocr.Entite)
    # ens_ocr = set(data_ocr.Entite) - intersection
    # ens_ref = set(data_ref.Entite) - intersection
    # dic_inter[name_ocr]["intersection"] = list(intersection)
    # dic_inter[name_ocr]["Contamine"] = list(ens_ocr)
    # dic_inter[name_ocr]["Ref"] = list(ens_ref)

    # stocker_png("../DATA/INTERSECTION_GLOBALES/%s_%s_concat-intersection.png" % (name_ocr, modele))
    # plt.show()
