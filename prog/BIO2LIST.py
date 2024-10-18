import csv
import glob
import json


def lire_csv(chemin):
    liste_row = []
    with open(chemin, newline='', encoding="utf-8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        next(spamreader)
        for row in spamreader:
            # print(row)
            if "B-" in row[1]:
                liste_row.append(row)
        return liste_row


def stocker(chemin, contenu):
    w = open(chemin, "w")
    w.write(json.dumps(contenu, indent=2))
    w.close()
    # print(chemin)
    return chemin


path_data = "../EXPE52_COMPARAISONS-ANNOTATIONS-MANUELLES_en cours/CORPUS_COMPAR/*/*TAL-ENS*/NER/*.bio"
dico = {}
for file_data in glob.glob(path_data):
    print(file_data)
    data = lire_csv(file_data)
    liste_loc = []
    liste_per = []
    liste_org = []
    liste_misc = []
    name_file = file_data.split("/")[-1]
    dico[name_file] = {}
    # print(data)
    # liste_toto = []
    # liste_mot = []
    # liste_entite = []
    # premier = 0
    for d in data:
        # print(d)
        if d[1] == "B-LOC":
            liste_loc.append(d[0])
            dico[name_file][d[1]] = len(liste_loc)
        if d[1] == "B-PER":
            liste_per.append(d)
            dico[name_file][d[1]] = len(liste_per)
        if d[1] == "B-ORG":
            liste_org.append(d)
            dico[name_file][d[1]] = len(liste_org)

        if d[1] == "B-MISC":
            liste_misc.append(d)
            dico[name_file][d[1]] = len(liste_misc)
    print(dico)
    stocker("../EXPE52_COMPARAISONS-ANNOTATIONS-MANUELLES_en cours/CORPUS_COMPAR/dico_nombre.json", dico)

    #     if d == data[-1]:
    #         if "B-" in d[1]:
    #             liste_toto.append(" ".join(liste_mot))
    #             liste_toto.append(d[0])
    #         if "I-" in d[1]:
    #             liste_mot.append(d[0])
    #             liste_toto.append(" ".join(liste_mot))
    #     else:
    #         if "B-" in d[1]:
    #             if premier == 0:
    #                 liste_mot.append(d[0])
    #                 liste_entite.append(d[1])
    #                 premier = 1
    #             else:
    #                 liste_toto.append(" ".join(liste_mot))
    #                 liste_mot = []
    #                 liste_entite = []
    #                 liste_mot.append(d[0])
    #                 liste_entite.append(d[1])
    #
    #         if "I-" in d[1]:
    #             liste_mot.append(d[0])
    #             liste_entite.append(d[1])
    #
    # print(liste_toto)
    # stocker(f"{file_data}-liste.json", liste_toto)