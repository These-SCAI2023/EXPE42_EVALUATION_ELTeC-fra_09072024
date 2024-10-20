# from nltk.corpus import brown # si besoin dans jupyter pip install nltk (déjà installé sur ma machine)
from functools import reduce
import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import axes3d
import json
import glob
import spacy
import re
import pandas as pd
import numpy as np


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


def plot_zipf(n, log=False):
    pyplot.rcParams['figure.figsize'] = [15, 10]
    pyplot.rcParams['axes.labelsize'] = 25
    pyplot.rcParams['xtick.labelsize'] = 25
    pyplot.rcParams['ytick.labelsize'] = 25

    if log:
        pyplot.yscale("log")
        pyplot.xscale("log")
    #        pyplot.axis([0,10^2,0,10^2])
    pyplot.ylim(0, n)
    pyplot.xlim(0, n)
    #    pyplot.title("Loi de Zipf (Brown Corpus)")
    pyplot.xlabel("Rang")
    pyplot.ylabel("Fréquence")
    # pyplot.tick_params(axis='both', labelsize=25)


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
    # pyplot.legend(fontsize='22',bbox_to_anchor=(0.5, 0., 0.5, 0.5))
    pyplot.legend(fontsize='22', bbox_to_anchor=(1.05,1))
    # pyplot.title("Loi de Zipf -- %s" % name_file)
    pyplot.savefig(name_file, dpi=300, bbox_inches="tight")
    pyplot.clf()
    return name_file

# MAIN
# path_corpora = "../CORRECTION_DISTANCES/small-TGB-RevueCorpus-corr-automatique_REN/"
path_corpora = "../small-ELTeC-por_REN/"
# dans "corpora" un subcorpus = toutes les versions 'un texte'

taille=[1000, 10000]
for subcorpus in sorted(glob.glob("%s*/" % path_corpora)):
    # print(subcorpus)
    data_list = []
    liste_version = []
    lst_nom_rens = []
    liste_data = []
    liste_freq = []
    liste_indice = []
    liste_auteur = []
    liste_frequence = []
    liste_rang = []
    liste_version_global = []

#     ## _______________ZIPF sur EN.json REF et OCRs
    for subpath in sorted(glob.glob("%s*REF/NER/*liste.json" % subcorpus)):
        k = 0
        print("subpath", subpath)
        nomfichier_ref = subpath.split("/")[-1]
        # print(nomfichier_ref)
        nom_ren_ref = (" ").join(nomfichier_ref.split("_")[-1].split("-")[:2])
        if "1.8.2" in nom_ren_ref :
            nom_ren_ref = re.sub("en 1.8.2", "stanza", nom_ren_ref)
        entite = lire_fichier(subpath)
        # print(entite)
        texte_dict = texte_to_dict(entite)
        # print(texte_dict)
        text_liste = dict_to_list(texte_dict)
        nomfichier = subpath.split("/")[-1]
        auteur = "_".join(nomfichier.split(".")[0].split("_")[:2])
        print("auteur", auteur)
        for i in text_liste :
            # print("---------",i)
            liste_data.append(i[-1])
            liste_freq.append(i[0])
            liste_version.append("Référence")
            lst_nom_rens.append(nom_ren_ref)
            liste_auteur.append(auteur)
            liste_indice.append(k)
            k+=1
        liste_frequence.append(liste_freq)
        liste_rang.append(liste_indice)
        liste_version_global.append(liste_version)
    #
    for subpath in sorted(glob.glob("%s*OCR/*/NER/*liste.json" % subcorpus)):
        k = 0
        # print("subpath", subpath)
        entite_ocr = lire_fichier(subpath)
        nomfichier = subpath.split("/")[-1]
        # print(nomfichier)
        output_name = "_".join(nomfichier.split(".")[0].split("_")[:2])
        # print("output_name",output_name)
        nom_ocr = nomfichier.split("_")[2].split(".")[0]
        nom_ocr = nommage(nom_ocr)
        nom_ren = (" ").join(nomfichier.split("_")[-1].split("-")[:2])
        if "1.8.2" in nom_ren :
            nom_ren = re.sub("en 1.8.2", "stanza", nom_ren)
        # print(nom_ren)
        # if nom_ocr =="Kraken" or nom_ocr =="Kraken 4.3.13":
        # if nom_ocr == "Tess. fr" or nom_ocr == "Tess. fr 3.10":
        if "lectaurep" not in nom_ocr:
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
                liste_auteur.append(output_name)
                k+=1
            liste_frequence.append(liste_freq)
            liste_rang.append(liste_indice)
            liste_version_global.append(liste_version)
        # print(liste_freq)
        # print(liste_indice)
        # print(len(lst_nom_rens))
        # print(len(liste_version))
        # print(len(liste_freq))
        # print(len(liste_data))
        # print(len(liste_indice))
    # tableau = {}
    # tableau["OCR"] = liste_version
    # # print(len(liste_version))
    # tableau["REN"] = lst_nom_rens
    # tableau["Data"] = liste_data
    # tableau["Fréquence"] = liste_freq
    # tableau["Rang"] = liste_indice
    # tableau["Auteur"] = liste_auteur
    # data_tab = pd.DataFrame(tableau)
    # # print(data_tab)


        # plot 3D
    ensemble_OCR = set(liste_version)
    # print(ensemble_OCR)
    i = 1
    liste_version_int_global = []
    # for k in liste_version_global:
    #     for j in k:
    #         if j == ensemble_OCR[0]:
    #             liste_version_int_global.append(0)
    #         if j == ensemble_OCR[1]:
    #             liste_version_int_global.append(1)
    #         if j == ensemble_OCR[2]:
    #             liste_version_int_global.append(2)
    liste_version_int_global = liste_version_global
    for v in ensemble_OCR:
        for k in range(len(liste_version_int_global)):
        #     for j in range(len(liste_version_int_global[k])):
        #         if liste_version_int_global[k][j] == v:
        #             liste_version_int_global[k][j] = i
        i = i+1

    # print("liste_rang", len(liste_rang))
    # for rg in liste_rang:
    #     print("len rg", len(rg))
    # print("len liste_frequence", len(liste_frequence))
    # for fq in liste_frequence:
    #     print("len fq", len(fq))
    # print("len liste_version_global", len(liste_version_int_global))
    # for vg in liste_version_int_global:
    #     print("len vg", len(vg))
    # print(liste_version_int_global[0:2])
    # # print(liste_version_int_global[10000:11000])
    # f, ax = pyplot.subplots(figsize=(20, 25), subplot_kw={'projection': '3d'})
    # version_pn = np.array(liste_version_global)
    # rang_pn = np.array(liste_rang)
    # freq_pn = np.array(liste_frequence)
    # # print(type(version_int))
    # # # ax.plot_trisurf(liste_indice, liste_freq, liste_version_int, linewidth=0, antialiased=False)
    # # ax.plot_wireframe(rang_pn, freq_pn, version_pn, rstride=10, cstride=0)
    # ax.plot_wireframe(freq_pn, version_pn, rang_pn)
    #
    #
    # # plot_zipf(t, True)
    # # #     # graph = plot_zipf(texte_list_ref, liste_list_ocr, lst_nom_config, lst_nom_ren_ref, log=True)
    # #     stocker("../ZIPF_PLT/%s-%s-4.png" %(output_name,t))
    # stocker("../3D-ZIPF_PLT/%s-4.png" % output_name)
# # #
#     ## _______________ZIPF sur EN.json REF et OCRs
