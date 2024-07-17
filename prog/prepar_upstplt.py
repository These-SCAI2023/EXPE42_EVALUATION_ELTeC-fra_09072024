import glob
import json

def lire_json (chemin):
    with open(chemin) as mon_fichier:
        data = json.load(mon_fichier)
    return data
def model_ocr(chemin):

    ocr_mod=chemin.split("/")[5]
    ocr_mod = ocr_mod.split("_")[-1]
    # liste_moteur.append(ocr_mod)
    # moteur = set(liste_moteur)
    return ocr_mod

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
corpusa=["DATA_TGB-2023_spaCy3.5.1_Distance","DATA_ELTeC-fra_spaCy3.5.1","DATA_ELTeC-eng_spaCy3.5.1","DATA_ELTeC-Por_spaCy3.5.1"]
corpa=corpusa[3]
path_corpora = f"../DATA_spaCy3.5.1_ENliste_globale/{corpa}/*"
dico_resultat={}

for gen_path in glob.glob(path_corpora):
    print("_____________",gen_path)
    corp = corpus(gen_path)
    print(corp)
    auteur=gen_path.split("/")[-1]
    print(auteur)
    paths_ocr="%s/*OCR/*/NER/*liste.json" % gen_path
    paths_ref = "%s/*REF/NER/*liste.json" % gen_path

    # dico_resultat={}
    for path_ocr in glob.glob(paths_ocr):
        # print(path_ocr)
        liste_ner_ocr = []
        moteur_ocr = model_ocr(path_ocr)
        data_ocr=lire_json(path_ocr)
        # print(data_ocr)
        # data_ocr=set(data_ocr)
        for data in data_ocr:
            liste_ner_ocr.append(data+"_"+auteur)

        if moteur_ocr in dico_resultat:
            set_tmp=dico_resultat[moteur_ocr]
            # set_tmp += data_ocr
            # dico_resultat[moteur_ocr] = set_tmp
            set_tmp+=liste_ner_ocr
            dico_resultat[moteur_ocr]= set_tmp
    #
        else:
            # dico_resultat[moteur_ocr] = data_ocr
            dico_resultat[moteur_ocr] = liste_ner_ocr
    #

    # print((json.dumps(dico_resultat, indent=2)))


    for path_ref in glob.glob(paths_ref):
        # print(path_ref)
        liste_ner_ref = []
        data_ref=lire_json(path_ref)
        # dico_resultat["Ref"] = data_ref
        for data in data_ref:
            liste_ner_ref.append(data+"_"+auteur)
        if "Ref" in dico_resultat:
            set_tmp_ref=dico_resultat["Ref"]
            set_tmp_ref+=liste_ner_ref
            print(set_tmp_ref)
            dico_resultat["Ref"]= set_tmp_ref

        else:
            dico_resultat["Ref"] = liste_ner_ref

    stocker("%s_moteurOCR-global--par-auteur.json" % corp, dico_resultat)
    # # print(dico_resultat)
    liste_res_nb = {}
    for cle, valeur in dico_resultat.items():
        set_valeur = len(set(valeur))
        liste_res_nb[cle] = {}
        liste_res_nb[cle]["EN-occ"] = len(valeur)
        liste_res_nb[cle]["EN-type"] = set_valeur

    stocker("%s_moteurOCR-global--par-auteur--nb_entite.json"%corp,liste_res_nb)




