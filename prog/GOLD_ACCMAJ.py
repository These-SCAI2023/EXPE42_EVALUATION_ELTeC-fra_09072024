import csv
import glob
import collections


def lire_csv(chemin):
    liste_row = []
    with open(chemin, newline='', encoding="utf-8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        next(spamreader)
        for row in spamreader:
            if row[0]!="":
                if row[1]!="":
                    liste_row.append([row[0],row[1]])
                else:
                    liste_row.append([row[0]+" O"])
    return liste_row

def stocker(chemin, contenu):
    with open(chemin, 'w', newline='') as f:
        bio_file = csv.writer(f, delimiter=' ', quotechar='|')
        bio_file.writerows(contenu)
    return bio_file

path_csv="../EXPE49_TAL-ENs_vs_GOLD-WG_en cours/REF_small-ELTeC-fra_IOB/*.bio"

for path in glob.glob(path_csv):
    # print(path)
    liste_label=[]
    print(path)
    data=lire_csv(path)
    # print(data)
    stocker(f"{path}.bio",data)

    for d in data:
        if d[-1]== "B-LOC" or d[-1]== "B-PER" or d[-1]== "B-ORG" or d[-1]== "B-MISC":
            liste_label.append(d[-1])
    print(len(liste_label))
    c = collections.Counter(liste_label)
    print(c)


