#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 10:18:55 2021

@author: antonomaz
"""


#from nltk.corpus import brown # si besoin dans jupyter pip install nltk (déjà installé sur ma machine)
from functools import reduce
import matplotlib.pyplot as pyplot
#import re # expression régulière 
import json
import glob
import spacy
import re

from nltk.corpus import stopwords
from renommage import *

def lire_fichier(chemin):
    with open(chemin) as json_data: 
        EN =json.load(json_data)
        
        return EN

def lire_fichier_txt (chemin):
    f = open(chemin , encoding = 'utf−8')
    chaine = f.read ()
    f.close ()
    return chaine

def text_2_tok(texte):
    liste_tok=[]
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
    texte_list=[]

    for mot in texte_dict.keys():
        texte_list.append([texte_dict[mot], mot])    

    texte_list.sort(reverse=True)
    return texte_list

        
def afficher_n(texte_list, n):
    
    cumul = 0
    print("rang\tmot\tfrequence\tfrequence(Zipf)")    
    print("-"*50)
    for _ in range(n):
        cumul += texte_list[_][0]
        print("{}\t{}\t{}\t\t{:.0f}".format(_+1, texte_list[_][1], texte_list[_][0], texte_list[0][0]/(_+1)))
    
    total = reduce(lambda x, y: x+y, [_[0] for _ in texte_list])
    prop = cumul/total*100
    
    print("-"*50)
    print("Ces {} mots représentent le {:0.2f}% du corpus".format(n, prop))

def plot_zipf(texte_list, ocr,ocr_name, log=False):
    pyplot.rcParams['figure.figsize'] = [15, 10]

    y = [_[0] for _ in texte_list]
    y_ = [_[0] for _ in ocr[0]]
    y1 = [_[0] for _ in ocr[1]]
    # y2 = [_[0] for _ in ocr[2]]
    # y3 = [_[0] for _ in ocr[3]]
    # y4 = [_[0] for _ in ocr[4]]

    pyplot.plot(y, "-", color = 'chartreuse', label="Référence")
    pyplot.plot(y_, "--", color = 'darkorange', label=ocr_name[0])
    pyplot.plot(y1, "-.", color = 'royalblue', label=ocr_name[1])
    # pyplot.plot(y2, "--", color='firebrick', label=ocr_name[2])
    # pyplot.plot(y3, "--", color='deepskyblue', label=ocr_name[3])
    # pyplot.plot(y4, "--", color='seagreen', label=ocr_name[4])
    # pyplot.plot(y_, "--", label="Approximation (Zipf)")
    
    if log:
        pyplot.yscale("log")
        pyplot.xscale("log")
#        pyplot.axis([0,10^2,0,10^2])  
    pyplot.ylim(0,10000)
    pyplot.xlim(0,95000)
      
#    pyplot.legend()
#    pyplot.title("Loi de Zipf (Brown Corpus)")
    pyplot.xlabel("Rang")
    pyplot.ylabel("Fréquence")
    
#    pyplot.show()    

def nom_fichier(chemin_fichier):
    
# NOM_FICHIER POUR LES TXT    
    nom_fichier= chemin_fichier.split("/")
    nom_fichier=nom_fichier[-1].split(".")
    nom_fichier=nom_fichier[0]
    # delete_PP = nom_fichier.split("_")
    # for i in delete_PP:
    #     if delete_PP[-1]=="PP":
    #         nom_fichier="_".join([delete_PP[0],delete_PP[1],"Ref"])
    return( nom_fichier)


def nom_fichier_REN(chemin_fichier):
# NOM_FICHIER POUR LES EN    
   nom_fichier = chemin_fichier.split("/")
   nom_fichier = nom_fichier[6].split(".")
   delete_txt = nom_fichier[1].split("_")
   delete_txt = "_".join([delete_txt[1],delete_txt[2]])
   delete_json = nom_fichier[2].split("-")
   delete_json = delete_json[1]
   delete_PP = nom_fichier[0].split("_")
   nom_fichier = "_".join([nom_fichier[0],delete_txt,delete_json])
   for i in delete_PP:
       if delete_PP[-1]=="PP":

           nom_fichier="_".join([delete_PP[0],delete_PP[1],"Ref",delete_txt,delete_json])

       else:
           nom_fichier="_".join([delete_PP[0],delete_PP[1],delete_PP[2],delete_txt,delete_json])
   return( nom_fichier)

def stocker(name_file):
#    pyplot.rcParams.update({'font.size': 16})
    titre_plt = name_file.split("/")
    titre_plt = titre_plt[3]
    titre_plt = titre_plt.split("_")
    titre_plt = " ".join(titre_plt)
    delete_png = titre_plt.split(".")
    titre_plt= " ".join([delete_png[0]])
    pyplot.legend()
    pyplot.title("Loi de Zipf -- %s"%titre_plt)
    pyplot.savefig(name_file, dpi=300)
    pyplot.clf()
    return name_file   

def filtre_stop(contenu, language):
    french_stopwords = set(stopwords.words('french'))
    filtre_stopfr =  lambda text: [token for token in text if token.lower() not in french_stopwords]
    return filtre_stopfr

#MAIN
path_corpora = "../small-TGB-RevueTAL_REN/"
# dans "corpora" un subcorpus = toutes les versions 'un texte'
texte_list_ref=[]
liste_list_ocr=[]
liste_noms_ocrs=[]
for subcorpus in sorted(glob.glob("%s*/"%path_corpora)):
    # print(subcorpus)
## _______________ZIPF sur .txt REF et OCRs
    for subpath in sorted(glob.glob("%s*REF/*.txt" % subcorpus)):
        print("subpath",subpath)
        texte = lire_fichier_txt(subpath)
        texte = re.sub("\!|\'|\?|\n|\.|\,|\-|\_|—|" "|' '|:|de|le|la|les|un|une|des|a|à", "", texte)
        texte_tok = text_2_tok(texte)
        # print(texte_tok)
        texte_dict = texte_to_dict(texte_tok)
        # print(texte_dict)
        texte_list_ref = dict_to_list(texte_dict)
        print(texte_list_ref)

    # for subpath in sorted(glob.glob("%s*OCR/*/*.txt"%subcorpus)):
    #     print("subpath",subpath)
    #     texte_ocr = lire_fichier_txt(subpath)
    #     nomfichier = nom_fichier(subpath)
    #     output_name= "_".join(nomfichier.split("_")[:2])
    #     nom_ocr = nomfichier.split("_")[-1]
    #     nom_ocr=nommage(nom_ocr)
    #     liste_noms_ocrs.append(nom_ocr)
    #
    #     texte_ocr = re.sub("\!|\'|\?|\n|\.|\,|\-|\_|—|" "|' '|:|de|le|la|les|un|une|des|a|à", "", texte_ocr)
    #     texte_tok_ocr = text_2_tok(texte_ocr)
    #     # print(texte_tok_ocr)
    #     texte_dict_ocr = texte_to_dict(texte_tok_ocr)
    #     # print(texte_dict_ocr)
    #     texte_list_ocr = dict_to_list(texte_dict_ocr)
    #     # print(texte_list_ocr)
    #     liste_list_ocr.append(texte_list_ocr)
    #     # print(texte_list_ref)
    #
    # graph=plot_zipf(texte_list_ref, liste_list_ocr, liste_noms_ocrs, log=True)
    # stocker("../small-ELTeC-fra_REN/ZIPF_PLT/%s.png"%output_name)
## _______________ZIPF sur .txt REF et OCRs
