# from nltk.corpus import brown # si besoin dans jupyter pip install nltk (déjà installé sur ma machine)
from functools import reduce
import matplotlib.pyplot as pyplot
# import re # expression régulière
import json
import glob
import spacy
import re
import pandas as pd
from IPython.display import display
import seaborn as sns
import scipy.stats as stats
from nltk.corpus import stopwords
from renommage import *


def lire_fichier(chemin):
    with open(chemin) as json_data:
        EN = json.load(json_data)

        return EN


def lire_fichier_txt(chemin):
    f = open(chemin, encoding='utf−8')
    chaine = f.read()
    f.close()
    return chaine


def text_2_tok(texte):
    liste_tok = []
    nlp = spacy.load("fr_core_news_sm")
    nlp.max_length = 5000000
    doc = nlp(texte)
    for token in doc:
        liste_tok.append(token.text)

    #        print(token.text)

    return liste_tok


def texte_to_dict(texte):
    texte_dict = {}

    for token in texte:
        if token in texte_dict:
            texte_dict[token] += 1
        else:
            texte_dict[token] = 1

    return texte_dict


def dict_to_list(texte_dict):
    texte_list = []

    for mot in texte_dict.keys():
        texte_list.append([texte_dict[mot], mot])

    texte_list.sort(reverse=True)
    return texte_list


def afficher_n(texte_list, n):
    cumul = 0
    print("rang\tmot\tfrequence\tfrequence(Zipf)")
    print("-" * 50)
    for _ in range(n):
        cumul += texte_list[_][0]
        print("{}\t{}\t{}\t\t{:.0f}".format(_ + 1, texte_list[_][1], texte_list[_][0], texte_list[0][0] / (_ + 1)))

    total = reduce(lambda x, y: x + y, [_[0] for _ in texte_list])
    prop = cumul / total * 100

    print("-" * 50)
    print("Ces {} mots représentent le {:0.2f}% du corpus".format(n, prop))


# def plot_zipf(texte_list, ocr, config_name, liste_ren_ref, log=False):
#     pyplot.rcParams['figure.figsize'] = [15, 10]
#
#     y = [_[0] for _ in texte_list]
#     y_ = [_[0] for _ in ocr[0]]
#
#     pyplot.plot(y, "-", color='chartreuse', label="Référence")
#     pyplot.plot(y_, "--", color='darkorange', label=config_name[0])
#     # pyplot.plot(y1, "-.", color='royalblue', label=ocr_name[1])
#
#     if log:
#         pyplot.yscale("log")
#         pyplot.xscale("log")
#     #        pyplot.axis([0,10^2,0,10^2])
#     pyplot.ylim(0, 10000)
#     pyplot.xlim(0, 95000)
#
#     #    pyplot.legend()
#     #    pyplot.title("Loi de Zipf (Brown Corpus)")
#     pyplot.xlabel("Rang")
#     pyplot.ylabel("Fréquence")
#
#
#    # pyplot.show()
def plot_zipf(log=True):
    pyplot.rcParams['figure.figsize'] = [15, 10]

    if log:
        # pyplot.yscale("log")
        pyplot.xscale("log")
    #        pyplot.axis([0,10^2,0,10^2])
    pyplot.ylim(0, 50)
    pyplot.xlim(0, 100)

    #    pyplot.legend()
    #    pyplot.title("Loi de Zipf (Brown Corpus)")
    pyplot.xlabel("Rang")
    pyplot.ylabel("Fréquence")
def nom_fichier(chemin_fichier):
    # NOM_FICHIER POUR LES TXT
    nom_fichier = chemin_fichier.split("/")
    nom_fichier = nom_fichier[-1].split(".")
    nom_fichier = nom_fichier[0]
    # delete_PP = nom_fichier.split("_")
    # for i in delete_PP:
    #     if delete_PP[-1]=="PP":
    #         nom_fichier="_".join([delete_PP[0],delete_PP[1],"Ref"])
    return (nom_fichier)


def nom_fichier_REN(chemin_fichier):
    # NOM_FICHIER POUR LES EN
    nom_fichier = chemin_fichier.split("/")
    nom_fichier = nom_fichier[6].split(".")
    delete_txt = nom_fichier[1].split("_")
    delete_txt = "_".join([delete_txt[1], delete_txt[2]])
    delete_json = nom_fichier[2].split("-")
    delete_json = delete_json[1]
    delete_PP = nom_fichier[0].split("_")
    nom_fichier = "_".join([nom_fichier[0], delete_txt, delete_json])
    for i in delete_PP:
        if delete_PP[-1] == "PP":

            nom_fichier = "_".join([delete_PP[0], delete_PP[1], "Ref", delete_txt, delete_json])

        else:
            nom_fichier = "_".join([delete_PP[0], delete_PP[1], delete_PP[2], delete_txt, delete_json])
    return (nom_fichier)


def stocker(name_file):
    #    pyplot.rcParams.update({'font.size': 16})
    # titre_plt = name_file.split("/")
    # titre_plt = titre_plt[3]
    # titre_plt = titre_plt.split("_")
    # titre_plt = " ".join(titre_plt)
    # delete_png = titre_plt.split(".")
    # titre_plt = " ".join([delete_png[0]])
    # pyplot.legend()
    # pyplot.title("Loi de Zipf -- %s" % name_file)
    pyplot.savefig(name_file, dpi=300)
    pyplot.clf()
    return name_file


def filtre_stop(contenu, language):
    french_stopwords = set(stopwords.words('french'))
    filtre_stopfr = lambda text: [token for token in text if token.lower() not in french_stopwords]
    return filtre_stopfr

# def quantile_plot(x, **kwargs):
#     quantiles, xr = stats.probplot(x, fit=False)
#     pyplot.scatter(xr, quantiles, **kwargs)
def qqplot(x, y, **kwargs):
    # _, xr = stats.probplot(x, fit=False)
    # _, yr = stats.probplot(y, fit=False)
    pyplot.plot(x, y, **kwargs)

# MAIN
path_corpora = "../small-ELTeC-fra-2021-2024_REN/"
# dans "corpora" un subcorpus = toutes les versions 'un texte'


for subcorpus in sorted(glob.glob("%sAIMARD_TRAPPEURS/" % path_corpora)):
    # print(subcorpus)
    data_list = []
    liste_version = []
    lst_nom_rens = []
    liste_data = []
    liste_freq = []
    liste_indice = []
    # k=0
#
#     ## _______________ZIPF sur EN.json REF et OCRs
    for subpath in sorted(glob.glob("%s*REF/NER/*liste.json" % subcorpus)):
        k = 0
        print("subpath", subpath)
        nomfichier_ref = subpath.split("/")[-1]
        # print(nomfichier_ref)
        nom_ren_ref = (" ").join(nomfichier_ref.split("_")[-1].split("-")[:2])
        entite = lire_fichier(subpath)
        # print(entite)
        texte_dict = texte_to_dict(entite)
        # print(texte_dict)
        text_liste = dict_to_list(texte_dict)
        for i in text_liste :
            # print("---------",i)
            liste_data.append(i[-1])
            liste_freq.append(i[0])
            liste_version.append("Référence")
            lst_nom_rens.append(nom_ren_ref)
            liste_indice.append(k)
            k+=1
    #
    for subpath in sorted(glob.glob("%s*OCR/*/NER/*liste.json" % subcorpus)):
        k = 0
        print("subpath", subpath)
        entite_ocr = lire_fichier(subpath)
        nomfichier = subpath.split("/")[-1]
        # print(nomfichier)
        output_name = "_".join(nomfichier.split(".")[0].split("_")[:2])
        print(output_name)
        nom_ocr = nomfichier.split("_")[2].split(".")[0]
        nom_ocr = nommage(nom_ocr)
        nom_ren = (" ").join(nomfichier.split("_")[-1].split("-")[:2])
        # print(nom_ren)
        texte_dict_ocr = texte_to_dict(entite_ocr)
        # print(texte_dict_ocr)
        texte_list_ocr = dict_to_list(texte_dict_ocr)
        # print(texte_list_ocr)
        for i in texte_list_ocr :
            # print("---------",i)
            liste_data.append(i[-1])
            liste_freq.append(i[0])
            liste_version.append(nom_ocr)
            lst_nom_rens.append(nom_ren)
            liste_indice.append(k)
            k+=1
        # print(liste_freq)
        # print(liste_indice)
        # print(len(lst_nom_rens))
        # print(len(liste_version))
        # print(len(liste_freq))
        # print(len(liste_data))
        # print(len(liste_indice))
        tableau = {}
        tableau["OCR"] = liste_version
        tableau["REN"] = lst_nom_rens
        tableau["Data"] = liste_data
        tableau["frequence"] = liste_freq
        tableau["rang"] = liste_indice
        data_tab = pd.DataFrame(tableau)
        # print(data_tab)
        # display(data_tab)
        g = sns.FacetGrid(data_tab, hue="REN", col="OCR", height=4)
        g.map(qqplot, "rang","frequence")

        plot_zipf()
        g.add_legend()
#
# #
# #     # graph = plot_zipf(texte_list_ref, liste_list_ocr, lst_nom_config, lst_nom_ren_ref, log=True)
        stocker("../ZIPF_PLT/%s.png" % output_name)
# #
#     ## _______________ZIPF sur EN.json REF et OCRs
