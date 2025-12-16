import json
import glob
import pandas as pd
import collections






def lire_json(chemin):
    with open(chemin) as mon_fichier:
        datajson = json.load(mon_fichier)
    return datajson


def stocker(chemin, contenu):
    w = open(chemin, "w")
    w.write(json.dumps(contenu, indent=2))
    w.close()
    # print(chemin)
    return chemin

annotations = {"e_1" : "PERS", "e_2" : "LOC", "e_3" : "ORG", "e_4" : "OTHER", "e_5" : "WORK", "e_6" : "DEMO", "e_7" :"ROLE","e_8" : "EVENT"}

path_data = "../EXPE52_COMPARAISONS-ANNOTATIONS-MANUELLES_en cours/CORPUS_COMPAR_TAL-ENS/*/*_WG-ELTeC/NER/*ann.json"

for file in glob.glob(path_data):
    auteur = file.split("/")[3]
    liste_label = []
    liste_text = []
    liste_label_iob = []
    print(file)
    data=lire_json(file)
    # print(data)
    for keys, values in data.items():
        if keys == "entities":
            # print(type(values))
            for index in values:
                # print(index)
                for cles, valeurs in index.items():
                    # print(valeurs)
                    if cles=="classId":
                        if valeurs == "e_1":
                            liste_label.append("B-"+annotations["e_1"])
                        if valeurs == "e_2":
                            liste_label.append("B-"+annotations["e_2"])
                        if valeurs == "e_3":
                            liste_label.append("B-"+annotations["e_3"])
                        if valeurs == "e_4":
                            liste_label.append("B-"+annotations["e_4"])
                        if valeurs == "e_5":
                            liste_label.append("B-"+annotations["e_5"])
                        if valeurs == "e_6":
                            liste_label.append("B-"+annotations["e_6"])
                        if valeurs == "e_7":
                            liste_label.append("B-"+annotations["e_7"])
                        if valeurs == "e_8":
                            liste_label.append("B-"+annotations["e_8"])
                    if cles == "offsets":
                        for id in valeurs:
                            for k, v in id.items():
                                if k == "text":
                                    liste_text.append(v)


    print(liste_label)
    # print(liste_text)
    print(len(liste_label))
    print(len(liste_text))
    c = collections.Counter(liste_label)
    print(c)
    dic_toto={}
    dic_toto[auteur] = c
    stocker(f"../EXPE52_COMPARAISONS-ANNOTATIONS-MANUELLES_en cours/{auteur}_WG-ELTeC_nbentite.json",dic_toto)

    # tableau={}
    # tableau["EN"] = liste_text
    # tableau["Label"]= liste_label
    # data_tab = pd.DataFrame(tableau)
    # data_tab.to_csv(f"{file}.bio", index=False, sep = " ")
    # Loc_label = data_tab.query("Label == 'B-LOC'")["EN"].tolist()
    # print("Loc_label", Loc_label)
    # stocker(f"{file}-liste.json", Loc_label)
