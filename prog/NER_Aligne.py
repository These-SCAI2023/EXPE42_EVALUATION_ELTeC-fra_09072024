import glob
import json
import re
import sklearn
from sklearn.neighbors import DistanceMetric
from sklearn.feature_extraction.text import CountVectorizer

# -----------------------------------------------------------------------------------------------------------------


def nom_repertoire(chemin):
    for mot in glob.glob(chemin):
        noms_rep = re.split("/", chemin)
        noms_repo = re.split("_", noms_rep[7])
        noms_repo = re.split("_", noms_repo[-1])
        noms_repo = "".join(noms_repo)
#        print("NOM FICHIER",noms_fichiers)

        return noms_repo
    
def nom_model(chemin):
    nom_model = re.split("/", chemin)[-1]
    nom_model = re.split("_", nom_model)[-1]
    nom_model = re.split("-", nom_model)[0]
    return nom_model
        
    
def nom_version(path):
    for mot in glob.glob(path): 
        noms_mod = re.split("/", path)
        noms_mods = re.split("_",noms_mod[6])
        # nm = re.split("-",noms_mods[-1])
        # nmod =nm[0]
        nmod =noms_mods[-1]
        return nmod

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

dictionnaire_tot = {}
# chemin d'accès aux fichiers
path_corpora = "../NER_GEO_COMPAR/OUTPUT/NER_CONCAT/SPACY_NER_CONCAT/ADAM/*/*"
# # dans "corpora" un subcorpus = toutes les versions 'un texte'

# récupération du contenu des fichiers
liste_EN_ocr = []
liste_EN_pp = []
liste_ref = []
liste_ocr = []
i=0

for subcorpus in sorted(glob.glob(path_corpora)):
    # print(subcorpus)
    for path in sorted(glob.glob("%s/*.json" % subcorpus)):
        print("path : ",path )

        texte = lire_fichier_json(path)
    #    print("************",subcorpus)
    #    print(texte)
        nomrep = nom_repertoire(path)
#        print(nomrep)

        if nomrep == "REF":
            liste_EN_pp.append(path)
    #        liste_texte_pp.append(subcorpus)
            liste_EN_pp.append(texte)

        elif nomrep == "OCR":
            liste_EN_ocr.append(path)
    #         liste_texte_ocr.append(subcorpus)
            liste_EN_ocr.append(texte)

while i <len(liste_EN_ocr) :
    nom_mod_pp = nom_version(liste_EN_pp[i])
    modele = nom_model(liste_EN_pp[i])
    print("mod : ",nom_mod_pp+modele)
    dictionnaire_tot[nom_mod_pp+modele] = {}
    liste_ref = liste_EN_pp[i+1]
    liste_ocr = liste_EN_ocr[i+1]
    dictionnaire_tot[nom_mod_pp+modele]  = get_similar_word(liste_ref,liste_ocr)
    print("########ecriture fichier###########")
    SavePath=get_save_path(liste_EN_ocr[i])
    SaveP = "%s_NERAligne.json"%(SavePath)
    # print(SaveP)
    stocker(SaveP, dictionnaire_tot[nom_mod_pp+modele])
    i=i+2

