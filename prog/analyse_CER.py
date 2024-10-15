import glob
import json

def lire_json (chemin):
    with open(chemin) as mon_fichier:
        data = json.load(mon_fichier)
    return data

path_corpora = "../small-TGB-RevueTAL_REN/*/*OCR/*/SIM/*.json"

for gen_path in glob.glob(path_corpora):
    print(gen_path)
    # auteur=gen_path.split("/")[-1].split(".")[0].split("_")[1:4]
    # print(auteur)
    # data=lire_json(gen_path)
    # # print(data)
    #
    # for key, value in data.items():
    #     # print(key)
    #     if key == "KL_res":
    #         for k, v in value.items():
    #             # print(k)
    #             if k == "CER":
    #                 print(v)