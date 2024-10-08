#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:44:43 2024

@author: ceres
"""

import glob
import json
import numpy as np


def lire_fichier_json(chemin):
    with open(chemin) as json_data: 
        texte = json.load(json_data)
    return texte


def moyenne(liste_res):
    somme = sum(liste_res)
    moyenne = somme/len(liste_res)
    return moyenne


def mediane(liste_resm):
    a = np.array(liste_resm)
    median_value = np.percentile(a, 50)
    return median_value


def stocker_json(chemin, contenu):
    with open(chemin, "w", encoding="utf-8") as w:
        w.write(json.dumps(contenu, indent=2, ensure_ascii=False))
    return


dico_res = {}
liste_CER = []
corpus = ["small-TGB-RevueTAL-corr-automatique_REN", "small-TGB-RevueCorpus-corr-automatique_REN", "small-ELTeC-fra-2021-2024-corr-automatique_REN","small-ELTeC-eng-corr-automatique_REN","small-ELTeC-por-corr-automatique_REN","small-ELTeC-fra-corr-automatique_REN"]
corp = corpus[5]
calcul = ["sim2-3", "word"]
calc = calcul[0]
path_file = f"../CORRECTION_DISTANCES/{corp}/*/*OCR/*"

for path in glob.glob(path_file):
    print(path)
    moteur_ocr = path.split("/")[-1].split("_")[-1]
    print(moteur_ocr)
    for file in glob.glob(f"%s/SIM/{calc}*.json"%path): ##REF
    # for file in glob.glob(f"{path}/NER/SIM/{calc}*.json"):  ##NER
        print("NER", file)
        ner_model =file.split("_")[-1].split("-liste.json")[0]
        print(ner_model)
        filename = file.split("/")[-1]
        data = lire_fichier_json(file)
        # print(data)
        for key, value_dic in data.items():
            if key == "KL_res":
                # print(value_dic)
                for k, v in value_dic.items():
                    if k == "CER":
                        if moteur_ocr in dico_res:
                            liste_CER = dico_res[moteur_ocr]
                            liste_CER.append(v)
                            dico_res[moteur_ocr] = liste_CER
                        else:
                            dico_res[moteur_ocr] = [v]
print("DICO--RES ***** ",dico_res)
dico_mediane={}
for cle, valeur in dico_res.items():
    dico_mediane[cle]= {}
    dico_mediane[cle]["mediane"] = mediane(valeur)
    dico_mediane[cle]["moyenne"] = moyenne(valeur)


print(f"../CORRECTION_DISTANCES/{corp}/OCR_{calc}_moy_mediane.json")
stocker_json(f"../CORRECTION_DISTANCES/{corp}/OCR_{calc}_moy_mediane.json",dico_mediane)

# print(f"../DATA_ELTeC_spaCy3.5.1_Distances/{corp}/{corp}_{calc}-test_moy_mediane.json")
# stocker_json(f"../ARCHEO_Correction_Distances/{corp}/{corp}_{calc}-test_moy_mediane.json",dico_mediane)
# mediane(liste_CERK)
# moyenne(liste_CERK)

# dico_res[moteur_ocr] = liste_CER
# print(dico_res)



####_______________________Programme version-1_______________________________
# mod_fr=["PP--Kraken","PP--Kraken-base",
#          "Kraken-base--PP","PP--TesseractFra-PNG","TesseractFra-PNG--PP",]
# mod_en=["REF--Kraken","Kraken--REF","REF--Kraken-jspll-pretrain", "Kraken-jspll-pretrain--REF","REF--Kraken-jspll-ELTeC","REF--Tesseract-PNG","Tesseract-PNG-jspll-ELTeC--REF","Tesseract-PNG-jspll-pretrain--REF"]
# mod_pt=[]
# liste_WERK=[]
# liste_WERT=[]
# ref=["PP","REF"]
# liste_CERK=[]
# liste_CERKeltec=[]
# liste_CERKpt=[]
# liste_CERT=[]
# liste_CERTeltec=[]
# liste_CERTpt=[]
        #             if f"{ref[0]}" in k and "Kraken" in k:
        #
        #                 if k == f"{ref[0]}--Kraken":
        #                     k=k.replace(k, f"Kraken--{ref[0]}")
        #                 if k == "REF--Kraken-jspll-ELTeC":
        #                     k=k.replace(k, "Kraken-jspll-ELTeC--REF")
        #                 if k == "REF--Kraken-jspll-pretrain":
        #                     k =k.replace(k, "Kraken-jspll-pretrain--REF")
        #
        #                 dico_res[k]={}
        #                 if k=="Kraken--REF":
        #                     for ssk, ssv in v.items():
        #                                 if ssk == "KL_res":
        #                                     for sssk,sssv in ssv.items():
        #                                         if sssk =="CER":
        #                                             dico_res[k][sssk]={}
        #                                             #print(sssk,sssv)
        #                                             liste_CERK.append(sssv)
        #                                             medcerk =mediane(liste_CERK)
        #                                             moycerk=moyenne(liste_CERK)
        #                                             dico_res[k][sssk]["med"]=medcerk
        #                                             dico_res[k][sssk]["moy"]=moycerk
        #
        #                 if k=="Kraken-jspll-ELTeC--REF":
        #                     for ssk, ssv in v.items():
        #                                 if ssk == "KL_res":
        #                                     for sssk,sssv in ssv.items():
        #                                         if sssk =="CER":
        #                                             dico_res[k][sssk]={}
        #                                             #print(sssk,sssv)
        #                                             liste_CERKeltec.append(sssv)
        #                                             medcerk =mediane(liste_CERKeltec)
        #                                             moycerk=moyenne(liste_CERKeltec)
        #                                             dico_res[k][sssk]["med"]=medcerk
        #                                             dico_res[k][sssk]["moy"]=moycerk
        #
        #
        #                 if k=="Kraken-jspll-pretrain--REF":
        #                     for ssk, ssv in v.items():
        #                                 if ssk == "KL_res":
        #                                     for sssk,sssv in ssv.items():
        #                                         if sssk =="CER":
        #                                             dico_res[k][sssk]={}
        #                                             #print(sssk,sssv)
        #                                             liste_CERKpt.append(sssv)
        #                                             medcerk =mediane(liste_CERKpt)
        #                                             moycerk=moyenne(liste_CERKpt)
        #                                             dico_res[k][sssk]["med"]=medcerk
        #                                             dico_res[k][sssk]["moy"]=moycerk
        #
        #
        #             if "REF" in k and "Tesseract-PNG" in k:
        #                 if k == "REF--Tesseract-PNG":
        #                     k=k.replace(k, "Tesseract-PNG--REF")
        #                 if k == "REF--Tesseract-PNG-jspll-ELTeC":
        #                     k=k.replace(k, "Tesseract-PNG-jspll-ELTeC--REF")
        #                 if k == "REF--Tesseract-PNG-jspll-pretrain":
        #                     k=k.replace(k, "Tesseract-PNG-jspll-pretrain--REF")
        #
        #                 dico_res[k]={}
        #                 if k=="Tesseract-PNG--REF":
        #                     for ssk, ssv in v.items():
        #                         if ssk == "KL_res":
        #                             for sssk,sssv in ssv.items():
        #                                 if sssk =="CER":
        #                                     dico_res[k][sssk]={}
        #                                     #print(sssk,sssv)
        #                                     liste_CERT.append(sssv)
        #                                     # dico_res[k][sssk]= liste_CERT
        #                                     # print(k,liste_CERK)
        #                                     moycert=moyenne(liste_CERT)
        #                                     medcert =mediane(liste_CERT)
        #                                     dico_res[k][sssk]["med"]=medcert
        #                                     dico_res[k][sssk]["moy"]=moycert
        #
        #
        #                 if k=="Tesseract-PNG-jspll-ELTeC--REF":
        #                     for ssk, ssv in v.items():
        #                         if ssk == "KL_res":
        #                             for sssk,sssv in ssv.items():
        #                                 if sssk =="CER":
        #                                     dico_res[k][sssk]={}
        #                                     #print(sssk,sssv)
        #                                     liste_CERTeltec.append(sssv)
        #                                     # dico_res[k][sssk]= liste_CERTeltec
        #                                     # print(k,liste_CERK)
        #                                     moycert=moyenne(liste_CERTeltec)
        #                                     medcert =mediane(liste_CERTeltec)
        #                                     dico_res[k][sssk]["med"]=medcert
        #                                     dico_res[k][sssk]["moy"]=moycert
        #
        #
        #                 if k=="Tesseract-PNG-jspll-pretrain--REF":
        #                     for ssk, ssv in v.items():
        #                         if ssk == "KL_res":
        #                             for sssk,sssv in ssv.items():
        #                                 if sssk =="CER":
        #                                     dico_res[k][sssk]={}
        #                                     #print(sssk,sssv)
        #                                     liste_CERTpt.append(sssv)
        #                                     # dico_res[k][sssk]= liste_CERTpt
        #                                     moycert=moyenne(liste_CERTpt)
        #                                     medcert =mediane(liste_CERTpt)
        #                                     dico_res[k][sssk]["med"]=medcert
        #                                     dico_res[k][sssk]["moy"]=moycert
        #
        #
        #
        #             for ssk, ssv in v.items():
        #                 if ssk == "KL_res":
        #                     for sssk,sssv in ssv.items():
        #                         if sssk =="CER":
        #                             dico_res["Kraken"][sssk]={}
        #                             #print(sssk,sssv)
        #                             liste_CERK.append(sssv)
        #                             moycerk=moyenne(liste_CERK)
        #                             medcerk =mediane(liste_CERK)
        #                             dico_res["Kraken"][sssk]["moy"]=moycerk
        #                             dico_res["Kraken"][sssk]["med"]=medcerk
        #                         if sssk=="WER":
        #                             dico_res["Kraken"][sssk]={}
        #                             liste_WERK.append(sssv)
        #                             moywerk=moyenne(liste_WERK)
        #                             medwerk =mediane(liste_WERK)
        #                             dico_res["Kraken"][sssk]["moy"]=moywerk
        #                             dico_res["Kraken"][sssk]["med"]=medwerk
        #         if "PP--TesseractFra-PNG" in k or "TesseractFra-PNG--PP" in k:
        #             dico_res["Tess. fra"]={}
        #             for ssk, ssv in v.items():
        #                 if ssk == "KL_res":
        #                     for sssk,sssv in ssv.items():
        #                         if sssk =="CER":
        #                             dico_res["Tess. fra"][sssk]={}
        #                             #print(sssk,sssv)
        #                             liste_CERT.append(sssv)
        #                             moycert=moyenne(liste_CERT)
        #                             medcert =mediane(liste_CERT)
        #                             dico_res["Tess. fra"][sssk]["moy"]=moycert
        #                             dico_res["Tess. fra"][sssk]["med"]=medcert
        #                         if sssk=="WER":
        #                             dico_res["Tess. fra"][sssk]={}
        #                             liste_WERT.append(sssv)
        #                             moywert=moyenne(liste_WERT)
        #                             medwert =mediane(liste_WERT)
        #                             dico_res["Tess. fra"][sssk]["moy"]=moywert
        #                             dico_res["Tess. fra"][sssk]["med"]=medwert
        #     stocker_json("../DATA_ELTeC_spaCy3.5.1_Distances/DATA_ELTeC-fra_spaCy3.5.1_d/word_moy_mediane.json",dico_res)