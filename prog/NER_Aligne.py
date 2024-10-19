import glob
import json
import re
import pandas as pd
from IPython.display import display
import sklearn
from sklearn.metrics import DistanceMetric
from sklearn.feature_extraction.text import CountVectorizer
from renommage import *

# -----------------------------------------------------------------------------------------------------------------
    
def nom_model(chemin):
    nom_model = re.split("/", chemin)[-1]
    nom_model = re.split("_", nom_model)[-1]
    nom_model = re.split("-liste", nom_model)[0]
    # print("nom_model",nom_model)
    return nom_model
        
    
def nom_version(path):
    noms_mod = re.split("/", path)[-1]
    noms_mod = re.split("_",noms_mod)[2].split(".txt")[0]
    noms_mod = nommage(noms_mod)
    # print("noms_version",noms_mod)
    return noms_mod

def get_file_path_info(chemin):
    listechemin = re.split("/", chemin)
    detailnomfichier = listechemin[-1].split("_")
    listechemin.remove(listechemin[-1])
    listechemin.remove(listechemin[-1])
    detailnomfichier.remove(detailnomfichier[-2])
    ret = listechemin + detailnomfichier
    return ret

def get_save_path(chemin):
    listechemin = re.split("/", chemin)
    listechemin.pop(-2)
    listechemin2 = "/".join(listechemin)
    return listechemin2

def lire_fichier_json(chemin):
    with open(chemin) as json_data:
        EN = json.load(json_data)
    return EN


# ["jaccard", "braycurtis","dice", "cosinus"]
def get_distances_word(texte1, texte2, N=2, liste_name=["jaccard", "cosinus"]):
    dico = {}
    for metric_name in liste_name:
        dico[metric_name] = []
        liste_resultat_dist2 = []
        # for n_max in range(1, N+1):###range([min, default = 0], max, [step, default = 1])
        V = CountVectorizer(analyzer='char', ngram_range=(1, 2), stop_words=None)
        X = V.fit_transform([texte1, texte2]).toarray()
        if metric_name != "cosinus":
            dist = DistanceMetric.get_metric(metric_name)
            distance_tab1 = dist.pairwise(X)
        else:
            distance_tab1 = sklearn.metrics.pairwise.cosine_distances(X)
        liste_resultat_dist2.append(distance_tab1[0][1])
        dico[metric_name] = liste_resultat_dist2
    return dico


def get_similar_word(liste_ref, liste_ocr, seuil=0.35):
    dico_total = {}
    # # suppression des répétitions dans les listes
    liste_PP = set(liste_ref)
    liste_OCR = set(liste_ocr)
    print(len(liste_PP))
    print(len(liste_OCR))

    # conversion en liste + organisation dans l'ordre alphabetique
    liste_PP_sort = list(liste_PP)
    liste_PP_sort.sort()
    liste_OCR_sort = list(liste_OCR)
    liste_OCR_sort.sort()

    # Calcul des distances
    print("#########Calcul des distances###########")
    for mot in liste_PP_sort:
        dico_total[mot] = {}
        if 3 > len(mot):
            dico_total[mot] = {"pas de comparaison"}
            continue
        for motocr in liste_OCR_sort:
            if 1 == len(motocr):
                dico_total[mot][motocr] = {"pas de comparaison"}
                continue
            dico_total[mot][motocr] = get_distances_word(mot, motocr)

    # sélection des mots en fonction des distances
    print("########sélection des mots en fonction des distances###########")
    new_dico = {}
    for mot in liste_PP_sort:
        new_dico[mot] = {}
        if 3 > len(mot):
            continue
        for motocr in liste_OCR_sort:
            if 1 == len(motocr):
                continue
            if dico_total[mot][motocr]["cosinus"][0] < seuil:
                new_dico[mot][motocr] = dico_total[mot][motocr]
    return new_dico

def stocker( chemin, contenu):
    #if os.path.exists(chemin)==True:  # Où mettre la sécurité ?
        #print(f"Already Done {chemin}")
    w =open(chemin, "w")
    w.write(json.dumps(contenu , indent = 2))
    w.close()
    
# -----------------------------------------------------------------------------------------------------------------


# chemin d'accès aux fichiers
path_corpora = "../small-ELTeC-fra-2021-2024_REN_test/*/"
# dans "corpora" un subcorpus = toutes les versions 'un texte'

# récupération du contenu des fichiers


# dico_en = {}

for subcorpus in sorted(glob.glob(path_corpora)):
    print("subcorpus",subcorpus)
    liste_EN = []
    liste_version = []
    liste_modele_REN = []
    for path in sorted(glob.glob("%s*REF/NER/*liste.json" % subcorpus)):
        print("path : ", path )
        data = lire_fichier_json(path)
        # print(data)
        version = nom_version(path)
        modele_REN = nom_model(path)
        print(version)
        print(modele_REN)
        print(data)
        liste_EN.append(data)
        liste_version.append(version)
        liste_modele_REN.append(modele_REN)
        # cle_dic = version+"--"+modele_REN
        # dico_en[cle_dic] = data

    for path_ocrs in sorted(glob.glob("%s*OCR/*/NER/*liste.json" % subcorpus)):
        print("path OCRS: ", path_ocrs )
        data_ocr = lire_fichier_json(path_ocrs)
        version = nom_version(path_ocrs)
        modele_REN = nom_model(path_ocrs)
        liste_EN.append(data_ocr)
        liste_version.append(version)
        liste_modele_REN.append(modele_REN)
        # cle_dic = version + "--" + modele_REN
        # dico_en[cle_dic] = data_ocr

#     for config, listeen in dico_en.items():

# # print(dico_en.keys())
    tableau = {}
    dic_sim = {}
    tableau["Version"] = liste_version
    tableau["REN"] = liste_modele_REN
    tableau["EN"] = liste_EN
    data_tab = pd.DataFrame(tableau)
    # print(data_tab)
    # display(data_tab)
    REN_liste=set(tableau["REN"])
    for r in REN_liste:
        data_tab1=data_tab.query('REN == @r')
        # display(data_tab1)
        data_tab2=data_tab1.query('Version == "REF"')
        # display(data_tab2)
        liste_reference = data_tab2["EN"].values[0]
        # print(liste_test)
        for i in range(len(data_tab1)):
            print(i)
            if data_tab1["Version"].values[i] != "REF":
                liste_roc = data_tab1["EN"].values[i]
                cle_dir= data_tab1["Version"].values[i] +"--"+ r
                print(cle_dir)
                dic_sim[cle_dir]  = get_similar_word(liste_reference, liste_roc, seuil=0.35)
            i=i+1
    stocker(f"{subcorpus}_NERALIGNE.json",dic_sim)





# while i <len(liste_EN_ocr) :
#     print("i--------->",i)
#     print(liste_EN_ocr[i])
#     nom_OCR = nom_version(liste_EN_ocr[i])
#     # print(nom_OCR)
#     modele_REN = nom_model(liste_EN_ocr[i])
#     print(modele_REN)
#     # print("mod : ",nom_OCR+"--"+modele_REN)
#     cle_dic= nom_OCR+"--"+modele_REN
#     dictionnaire_tot[cle_dic] = {}
#     liste_ref = liste_EN_ref[i+1]
#     # print(liste_ref)
#     liste_ocr = liste_EN_ocr[i+1]
#
#     dictionnaire_tot[cle_dic]  = get_similar_word(liste_ref,liste_ocr)
# # #     # print(dictionnaire_tot.keys())
# # #     # print("########ecriture fichier###########")
# # #     # SavePath=get_save_path(liste_EN_ocr[i])
# # #     # SaveP = "%s_NERAligne.json"%(SavePath)
# # #     # # print(SaveP)
# # #     # stocker(SaveP, dictionnaire_tot[cle_dic])
#     i=i+2

