import glob
import json

def lire_json (chemin):
    with open(chemin) as mon_fichier:
        data = json.load(mon_fichier)
    return data
def model_ocr(chemin):
    ocr_mod=chemin.split("/")[4]
    # ocr_mod = chemin.split("/")[5]
    ocr_mod = ocr_mod.split("_")[-1]
    # liste_moteur.append(ocr_mod)
    # moteur = set(liste_moteur)
    return ocr_mod

def model_REN(chemin):
    REN_version = chemin.split("_")[-1]
    REN_version = REN_version.split("-liste")[0]
    return REN_version

def corpus(chemin):
    ocr_mod="/".join(chemin.split("/")[:3])
    # ocr_mod = ocr_mod.split("_")[0]
    return ocr_mod
def stocker(chemin, contenu):
    w = open(chemin, "w")
    w.write(json.dumps(contenu, indent=2))
    w.close()
    # print(chemin)
    return chemin

# corpusa=["DATA_TGB-2023_spaCy3.5.1_Distance","DATA_ELTeC-fra_spaCy3.5.1","DATA_ELTeC-eng_spaCy3.5.1","DATA_ELTeC-Por_spaCy3.5.1"]
# corpa=corpusa[3]

path_corpora = f"../ELTeC-*/*"


for gen_path in glob.glob(path_corpora):
    dico_REN = {}
    # print("_____________",gen_path)
    corp = gen_path.split("/")[1]
    print(corp)
    auteur=gen_path.split("/")[-1]
    # print(auteur)
    paths_ocr= f"{gen_path}/*OCR/*/NER/*liste.json"
    paths_ref = "%s/*_REF/NER/*liste.json"%gen_path

    # dico_resultat={}
    for path_ocr in glob.glob(paths_ocr):
        print("auteur OCR",auteur)
        # print(path_ocr)
        version_REN_ocr=model_REN(path_ocr)
        # dico_REN[version_REN_ocr]={}
        moteur_ocr=model_ocr(path_ocr)
        liste_ner_ocr = []
        # print(moteur_ocr)
        data_ocr=lire_json(path_ocr)
        # print(data_ocr)
        # data_ocr=set(data_ocr)
        for data in data_ocr:
            liste_ner_ocr.append(data+"_"+auteur)
        if version_REN_ocr  in dico_REN:
            if moteur_ocr in dico_REN[version_REN_ocr]:
                dico_REN[version_REN_ocr][ moteur_ocr] = liste_ner_ocr
            else:
                dico_REN[version_REN_ocr][ moteur_ocr] = liste_ner_ocr
        else:
            dico_REN[version_REN_ocr ] = {}
            if moteur_ocr in dico_REN[version_REN_ocr]:
                dico_REN[version_REN_ocr][moteur_ocr]= liste_ner_ocr
            else:
                dico_REN[version_REN_ocr][moteur_ocr] = liste_ner_ocr
            # print("------------------------>",dico_resultat)

    for path_ref in glob.glob(paths_ref):
        # print(path_ref)
        print("auteur REF", auteur)
        version_REN_ref = model_REN(path_ref)
        liste_ner_ocr = []
        liste_ner_ref = []
        data_ref=lire_json(path_ref)
        for data in data_ref:
            liste_ner_ref.append(data+"_"+auteur)
        if version_REN_ref  in dico_REN:
            if "Ref" in dico_REN[version_REN_ref]:
                dico_REN[version_REN_ref]["Ref"] = liste_ner_ref
            else:
                dico_REN[version_REN_ref]["Ref"] = liste_ner_ref
        else:
            dico_REN[version_REN_ref ] = {}
            if "Ref" in dico_REN[version_REN_ocr]:
                dico_REN[version_REN_ref]["Ref"]= liste_ner_ref
            else:
                dico_REN[version_REN_ref]["Ref"] = liste_ner_ref

    for kle, value in dico_REN.items():
        print(kle)
        stocker(f"../Upsetplot_intersection/PAR_AUTEUR/{corp}/{auteur}_{corp}_{kle}.json" ,value)
# # print(dico_resultat)
    liste_res_nb = {}
    for key, dico_resultat in dico_REN.items():
        for cle, valeur in dico_resultat.items():
            set_valeur = len(set(valeur))
            liste_res_nb[key+"_"+cle] = {}
            liste_res_nb[key+"_"+cle]["EN-occ"] = len(valeur)
            liste_res_nb[key+"_"+cle]["EN-type"] = set_valeur

            stocker(f"../Upsetplot_intersection/PAR_AUTEUR/nombre_entite/{corp}/{auteur}_{corp}--nb_entite.json",liste_res_nb)



