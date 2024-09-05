import json
import glob


def lire_json (chemin):
    with open(chemin) as mon_fichier:
        data = json.load(mon_fichier)
    return data

def NERtools(chemin):
    infos=chemin.split('/')[-1]
    tools=infos.split('_')[-1]
    version=infos.split('.')[0]
    return version, tools

path_SEM="../small-ELTeC-fra_SEM-WiNER/ADAM/*/*/*"
path_CasEN="../small-ELTeC-fra_CasEN/ADAM/*/*/*"
path_NERtools = "../small-ELTeC-fra-2021-2024_REN/ADAM/*"


EN_input = input("Entité recherchée : ")
for pathNERtools in glob.glob(path_NERtools):
    if "REF" in pathNERtools:
        # print(pathNERtools)
        pathNERtools_REF= f"{pathNERtools}/NER"
        # print(pathNERtools_REF)
        for path in glob.glob(f"{pathNERtools_REF}/*.json"):
            data=lire_json(path)
            if type(data) == dict :
                toolsNER = NERtools(path)
                # print(toolsNER)
                # print(data)
                for key, value in data.items():
                    # print(value)
                    for k, v in value.items():
                        if k =="text":
                            # print(v)
                            if EN_input in v :
                                print(toolsNER, value["label"],value["jalons"], v)
    # if "OCR" in pathNERtools:
    #     # print(pathNERtools)
    #     pathNERtools_REF= f"{pathNERtools}/*/NER"
    #     # print(pathNERtools_REF)
    #     for path in glob.glob(f"{pathNERtools_REF}/*.json"):
    #         data=lire_json(path)
    #         if type(data) == dict :
    #             toolsNER = NERtools(path)
    #             # print(toolsNER)
    #             # print(data)
    #             for key, value in data.items():
    #                 # print(value)
    #                 for k, v in value.items():
    #                     if k =="text":
    #                         # print(v)
    #                         if EN_input in v :
    #                             print(toolsNER,value["label"],value["jalons"], v)

# for pathSEM in glob.glob(path_SEM):
#     print(pathSEM)
# for pathCasEN in glob.glob(path_CasEN):
#     print(pathCasEN)