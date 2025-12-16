#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 12:09:59 2023

@author: antonomaz
"""

import csv
import glob
import json

def stocker_json(chemin,contenu):
    with open(chemin, "w", encoding="utf-8") as w:
        w.write(json.dumps(contenu, indent =2,ensure_ascii=False))
    return

DATA_path = "../DAUDET_ANNOTATION_MANUELLE_TYPOLOGIE/*.csv"


for file_path in glob.glob(DATA_path):
    liste_resultat = []
    print(file_path)
    with open(file_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
        next(spamreader)

        for row in spamreader:
            #            print(row[1])
            liste_resultat.append(row)
        # print(liste_resultat)
    dico_resultat = {}
    liste_Hapax = []
    liste_Freq = []
    liste_VP_Hapax = []
    liste_VP_Freq = []
    liste_FP_Hapax = []
    liste_FP_Freq = []
    liste_FVP_Hapax=[]
    liste_FVP_Freq=[]
    liste_FFN_Hapax = []
    liste_FFN_Freq= []
    liste_FFP_Hapax = []
    liste_FFP_Freq = []

    for data in liste_resultat:
        # if len(data)<4:
        #  print(len(data),"-->",data)
           # print(data[0],data[1])
        if data[1] == "1":
            #        print(data)
            liste_Hapax.append(data)
        else:
            liste_Freq.append(data)
        dico_resultat["nb. hapax"] = len(liste_Hapax)
        dico_resultat["nb. occ"] = len(liste_Freq)

    for dt in liste_Hapax:
        if dt[3] == "VP":
            liste_VP_Hapax.append(dt)
            dico_resultat["nb. VP hapax"] = len(liste_VP_Hapax)
        if dt[3] == "FVP":
            liste_FVP_Hapax.append(dt)
            dico_resultat["nb. FVP hapax"] = len(liste_FVP_Hapax)
        if dt[3] == "FP":
            liste_FP_Hapax.append(dt)
            dico_resultat["nb. FP hapax"] = len(liste_FP_Hapax)
        if dt[3] == "FFN":
            liste_FFN_Hapax.append(dt)
            dico_resultat["nb. FFN hapax"] = len(liste_FFN_Hapax)
        if dt[3] == "FFP":
            liste_FFP_Hapax.append(dt)
            dico_resultat["nb. FFP hapax"] = len(liste_FFP_Hapax)

    for dtf in liste_Freq:
        if dtf[3] == "VP":
            liste_VP_Freq.append(dtf)
            dico_resultat["nb. VP occ"] = len(liste_VP_Freq)
        if dtf[3] == "FP":
            liste_FP_Freq.append(dtf)
            dico_resultat["nb. FP occ"] = len(liste_FP_Freq)
        if dtf[3] == "FVP":
            liste_FVP_Freq.append(dtf)
            dico_resultat["nb. FVP occ"] = len(liste_FVP_Freq)
        if dtf[3] == "FFN":
            liste_FFN_Freq.append(dtf)
            dico_resultat["nb. FNN occ"] = len(liste_FFN_Freq)
        if dtf[3] == "FFP":
            liste_FFP_Freq.append(dt)
            dico_resultat["nb. FFP occ"] = len(liste_FFP_Freq)


    print(dico_resultat)
    stocker_json(f"{file_path}_compte-typologie_2.json",dico_resultat)
    #     if dt[2] == "FP" or dt[2] == "PERS" or dt[2] == "EVENT" or dt[2] == "TIME":
    #         liste_FP_Hapax.append(dt)
    #         liste_FP_Freq.append(dt)
    # for dt in liste_Freq:
    #     if dt[2] == "VP":
    #         liste_VP_Freq.append(dt)
    #
    #     if dt[2] == "AMBIG":
    #         liste_AMB_Freq.append(dt)
    #
    #     if dt[2] == "FP" or dt[2] == "PERS" or dt[2] == "EVENT" or dt[2] == "TIME":
    #         liste_FP_Freq.append(dt)
    #
    # liste_VP_Freq.append(dt)
    # dico_resultat["nb. VP occ"] = len(liste_VP_Freq)

    #
    # print("\\begin{tabular}{|l|l|l|l|}")
    # print("\\hline")
    # print("&\multicolumn{3}{c|}{", f"{file_path}", "}\\")
    # print("\hline")
    # print("VP hapax", len(liste_VP_Hapax))
    # print("FP hapax", len(liste_FP_Hapax))
    # print("Ambig hapax", len(liste_AMB_Hapax))
    # print("VP type", len(liste_VP_Freq))
    # print("FP type", len(liste_FP_Freq))
    # print("Ambig type", len(liste_AMB_Freq))








