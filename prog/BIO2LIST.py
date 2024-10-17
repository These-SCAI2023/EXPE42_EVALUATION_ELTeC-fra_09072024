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
            if row[1]!="O":
                liste_row.append(row)
        return liste_row

def stocker(chemin, contenu):
    w = open(chemin, "w")
    w.write(json.dumps(contenu, indent=2))
    w.close()
    # print(chemin)
    return chemin


path_data = "../EXPE52_COMPARAISONS-ANNOTATIONS-MANUELLES_en cours/CORPUS_COMPAR/*/*TAL-ENS*/NER/*.bio"

for file_data in glob.glob(path_data):
    print(file_data)
    data = lire_csv(file_data)
    # print(data)
    i = 0
    liste_toto = []
    liste_mot = []
    liste_entite = []
    premier=0
    for d in data:
        if "B-" in d[1]:
            if premier==0:
                liste_mot.append(d[0])
                liste_entite.append(d[1])
                premier=1
            else:
                liste_toto.append(" ".join(liste_mot))
                liste_mot = []
                liste_entite = []
                liste_mot.append(d[0])
                liste_entite.append(d[1])

        if "I-" in d[1]:
            liste_mot.append(d[0])
            liste_entite.append(d[1])

    print(liste_toto)


    # for data[i] in data:
    #     # print(data[i])
    #     if "I-" in data[i][1]:
    #         # print(data[i-1])
    #         if "I-" in data[i-1][1]:
    #             dataconcat = data[i - 1][0] +" " +data[i][0]
    #             # print(dataconcat)
    #             if "I-" in data[i-2][1]:
    #                 # print(data[i-2])
    #                 dataconcat2 = data[i-2][0] +" " +dataconcat
    #                 # print(detaconcat2)
    #
    #             if "B-" in data[i-2][1]:
    #                 # print(data[i-2])
    #                 dataconcat2 = data[i-2][0] + " "+dataconcat
    #                 # print(detaconcat3)
    #                 liste_mot.append(dataconcat2)
    #     if "B-" in data[i][1]:
    #         liste_mot.append(data[i][0])
    #
    #     i = i+1
    # print(liste_mot)
#     # stocker(f"{file_data}-liste.json")
# #     for data[i] in data:
# #         if "I-" in data[i][1]:
#             # print(data[i-1])
#             if "I-" in data[i-1][1]:
#                 dataconcat = data[i - 1] + data[i]
#                 if "B-" in data[i-2][1]:
#                     # print(data[i-2])
#                     detaconcat2 = data[i-2] + dataconcat
#                     print(detaconcat2)
#         i=i+1
#
#
# print(liste_mot)
