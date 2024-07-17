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
path_corpora = f"../DATA_ELTeC_spaCy3.5.1_ENliste/DATA_ENliste/{corpa}_moteurOCR-global.json"
dico_resultat={}

for gen_path in glob.glob(path_corpora):
    print("_____________",gen_path)
    data=lire_json(gen_path)
    # print(data)
    liste_res_nb = {}
    for cle, valeur in data.items():
        print(cle)
        set_valeur=len(set(valeur))
        # en_type=str(set_valeur)
        liste_res_nb[cle] = {}
        liste_res_nb[cle]["EN-occ"] = len(valeur)
        liste_res_nb[cle]["EN-type"] = set_valeur
    stocker("%s_--nb_entite.json"%gen_path,liste_res_nb)