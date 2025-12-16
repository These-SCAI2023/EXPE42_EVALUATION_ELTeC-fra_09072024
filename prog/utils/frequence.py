import json
import glob

def lire_fichier_json(chemin):
    with open(chemin) as json_data:
        EN = json.load(json_data)
    return EN


def stocker( chemin, contenu):
    #if os.path.exists(chemin)==True:  # Où mettre la sécurité ?
        #print(f"Already Done {chemin}")
    w =open(chemin, "w")
    w.write(json.dumps(contenu , indent = 2))
    w.close()



path_corpora = "../CORRECTION_DISTANCES/small-ELTeC-fra-2021-2024-corr-automatique_REN/*/"
for path in glob.glob(f"{path_corpora}*REF/NER/*liste.json"):
    dico_freq = {}
    print("REF : ",path)
    data = lire_fichier_json(path)
    print(data)
    for d in data:
        if d not in dico_freq:
            dico_freq[d] = 1
        else:
            dico_freq[d] += 1
    sorted_dicofreq = {key: value for key, value in sorted(dico_freq.items(), key=lambda item: item[1], reverse=True)}
    stocker(f"{path}_freq.json", sorted_dicofreq)

for path_ocrs in glob.glob(f"{path_corpora}*OCR/*/NER/*liste.json"):
    dicocr_freq = {}
    print("OCR : ",path_ocrs)
    data_ocr = lire_fichier_json(path_ocrs)
    print(data_ocr)
    for do in data_ocr:
        if do not in dicocr_freq:
            dicocr_freq[do] = 1
        else:
            dicocr_freq[do] += 1
    sorted_dicocrfreq = {key: value for key, value in sorted(dicocr_freq.items(), key=lambda item: item[1], reverse=True)}
    stocker(f"{path_ocrs}_dico-freq.json", sorted_dicocrfreq)