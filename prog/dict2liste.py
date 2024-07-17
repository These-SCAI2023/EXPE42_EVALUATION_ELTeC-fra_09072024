import json
import glob
import re
import os
import csv

def lire_json (chemin):
    with open(chemin) as mon_fichier:
        data = json.load(mon_fichier)
    return data

def modeles(chemin):
    model=chemin.split("/")[-1]
    model = model.split("_")[-1]
    model = model.split(".json")[0]
    if model== "fr-1.8.2":
        model = re.sub(model, "stanza-%s"%model, model)
    # print("model-------------------->",model)
    return model

def sortie(chemin_sortie):
    stz="fr-1.8.2"
    modelee=modeles(chemin_sortie)
    sortir=chemin_sortie.split("/")
    nom_fich=sortir[-1].split(".json")[0]
    if stz in nom_fich:
        nom_fich=nom_fich.split("_")
        nom_fich="_".join(nom_fich[:3])
        sortir = "/".join(sortir[:-2]) + "/NER/" + nom_fich+"_"+modelee + "-liste.json"
    else:
        sortir="/".join(sortir[:-2])+"/NER/"+nom_fich+"-liste.json"
    return sortir

def stocker(chemin, contenu):
    w = open(chemin, "w")
    w.write(json.dumps(contenu, indent=2))
    w.close()
    # print(chemin)

    return chemin

# Ajouter .json à la place de .txt
# path_corpora = "../DATA_ELTeC_spaCy3.5.1_Distances/DATA_ELTeC-eng_spaCy3.5.1/*/*OCR/*/SIM/*.txt"
path_corpora = "../DATA_TGB-2023_spaCy3.5.1_Distance/*/*OCR/*/SIM/*.txt"
for path in glob.glob(path_corpora):
    print(path)
    add_json=path.split(".txt")[0]+".json"
    print(add_json)
    os.rename(path, add_json)

# # # Compter le nombre de sorties par dossier pour détecter les fichiers manquants
# path_corpora = "../DATA_ELTeC_spaCy3.5.1/DATA_ELTeC-fra_spaCy3.5.1/*"
# i=0
# for path in glob.glob(path_corpora):
#     # print(path)
#     liste_fich=[]
#     i=i+1
#     for subpath in glob.glob("%s/OCR/*/NER_concat/SIM/*"%path):
#         liste_fich.append(subpath)
#     if len(liste_fich)!=:
#         print(path)
#     # print(len(liste_fich))
# print(i)
## Création du sous-dossier NER-concat

# path_corpora = "../DATA_test_09072024/ADAM_Mon-village/*"
# path_corpora = "../REN_08072024/*/*"
# for subpath in glob.glob(path_corpora):
#     # print("_____________",path)
#     for path in glob.glob("%s/*"%subpath):
#         if "OCR" in path:
#             add_rep=os.mkdir('%s/NER_concat'%path)
#     if "REF" in subpath:
#         add_rep = os.mkdir('%s/NER_concat' % subpath)



# Dict2list concaténation
# path_corpora = "../DATA_ELTeC-fra/DAUDET/*/DAUDET_petit-chose_PP_multiNER_4tools-intersection2_annot.json"
# path_corpora = "../DATA_test_09072024/ADAM_Mon-village/*"
path_corpora = "../DATA_ELTeC-eng_spaCy3.5.1/*/*"
# modeles = ["camenBert_ner", "sm", "lg","flair"]
# dico_entite = {}

# for path in glob.glob(path_corpora):
#     print("_____________",path)
#     for subpath in glob.glob("%s/*/*/*1.json"%path):
#         print(subpath)
#         mod=modeles(subpath)
#         print(mod)
#         path_output=sortie(subpath)
#         print("path_output",path_output)
#         dico_entite=lire_json(subpath)
#         liste_entite=[]
#         for cle, value in dico_entite.items():
#             # print(value["label"])
#             if value["label"]=="LOC" or value["label"]=="GPE":
#                 # print(value["text"])
#                 # i_replace = value["text"].replace(" ", "")
#                 # print(i_replace)
#                 liste_entite.append(value["text"])
#         print(len(liste_entite))
#         stocker(path_output, liste_entite)
#
#     for refpath in glob.glob("%s/*/*1.json"%path):
#         print(refpath)
#         mod = modeles(refpath)
#         print(mod)
#         path_output = sortie(refpath)
#         print("path_output", path_output)
#         dico_entite = lire_json(refpath)
#         liste_entite = []
#         for cle, value in dico_entite.items():
#             # print(value["label"])
#             if value["label"] == "LOC" or value["label"] == "GPE":
#                 # print(value["text"])
#                 # i_replace = value["text"].replace(" ", "")
#                 # print(i_replace)
#                 liste_entite.append(value["text"])
#         print(len(liste_entite))
#         stocker(path_output, liste_entite)





    # with open("%s.csv"%path_output, 'a', newline='') as csvfile:
    #     spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #     spamwriter.writerow(["NERtools","entite","annotation"])
    #     for key, value in dico_entite.items():
    #         # print(value)
    #         for item in value:
    #             print(key, item)
    #             spamwriter.writerow([key, item,""])