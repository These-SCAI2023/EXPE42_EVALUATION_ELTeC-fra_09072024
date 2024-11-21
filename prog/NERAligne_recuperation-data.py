import json
import glob


def lire_json(chemin):
    with open(chemin) as mon_fichier:
        datajson = json.load(mon_fichier)
    return datajson


def nertools(chemin):
    infos = chemin.split('/')[-1]
    tools = infos.split('_')[-1]
    version = infos.split('.')[0]
    return version, tools


auteur="AIMARD"
path_NERaligne= f"../small-ELTeC-fra-2021-2024_NERAligne/{auteur}*.json"

liste_res=[]

EN_input = input("Entité recherchée : ")
for path_file in glob.glob(path_NERaligne):
        data = lire_json(path_file)
        print(path_file)
        for key, value in data.items():
            # print("----------------------",key)

            for k , v in value.items():
                if EN_input in k:
                    print("CLE ---->", k,", config", key,"\n")
                    for kk, vv in v.items():
                        # print("KLE---->", k, "ALigne ---> ", kk,", Distance ---> ", vv)
                        print("                             Entité(s) alignée(s) ---> ", kk, ", Distance ---> ", vv,"\n\n")


# for pathSEM in glob.glob(path_SEM):
#     print(pathSEM)
# for pathCasEN in glob.glob(path_CasEN):
#     print(pathCasEN)