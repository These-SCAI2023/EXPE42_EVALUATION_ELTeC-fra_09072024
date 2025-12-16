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


# path_SEM = "../small-ELTeC-fra_SEM-WiNER/ADAM/*/*/*"
# path_CasEN = "../small-ELTeC-fra_CasEN/ADAM/*/*/*"
path_NERtools = "../small-ELTeC-fra-2021-2024_REN/*/*"
# path_NERtools = "../small-ELTeC-fra-2021-2024_REN_PST/*/*"
# path_NERtools = "../small-ELTeC-eng_REN/*/*"
# path_NERtools = "../small-ELTeC-por_REN/*/*"
liste_res=[]

EN_input = input("Entité recherchée : ")
for pathNERtools in glob.glob(path_NERtools):
    # print(pathNERtools)
    if "REF" in pathNERtools:
        # print(pathNERtools)
        pathNERtools_REF = f"{pathNERtools}/NER"
        # print(pathNERtools_REF)
        for path in glob.glob(f"{pathNERtools_REF}/*liste.json"):
            # if "liste" not in path or "freq" not in path:
                data = lire_json(path)
                # if type(data) is dict:
                toolsNER = nertools(path)
                # print(toolsNER)
                # print(data)
                for v in data:
                    if EN_input in v:  # si en entré dictionnaire

                        print(toolsNER, v)
                    # for key, value in data.items():
                    #     # print(value)
                    #     for k, v in value.items():
                    #         if k == "text":
                    #             # print(v)
                    #             if EN_input in v:
                    #             #     print("ALL --> ",toolsNER, value["label"], value["jalons"], v)
                    #                 if value["label"] == "LOC":
                    #                     liste_res.append(v)
                    #                     print(toolsNER, v)
                    #                     # print(toolsNER, value["label"], value["jalons"], v)
# # print(len(liste_res))
    if "OCR" in pathNERtools:
        # print(pathNERtools)
        pathNERtools_OCR = f"{pathNERtools}/*/NER"
        # print(pathNERtools_OCR)
        for path in glob.glob(f"{pathNERtools_OCR}/*liste.json"):
            # print(path)
            data = lire_json(path)
            # print(data)
            # for enti in data:
            #     # print(enti)
            #     if EN_input in enti :
            #         print(enti, path)
            # if type(data) is dict: # si en entré dictionnaire
            toolsNER = nertools(path)
            for v in data:
                # print(v)
            # print(toolsNER)
            # print(data)
            # for key, value in data.items():# si en entré dictionnaire
            #     # print(value)# si en entré dictionnaire
            #     for k, v in value.items():# si en entré dictionnaire
            #         if k == "text":# si en entré dictionnaire
            #             print(v)# si en entré dictionnaire
                if EN_input in v:# si en entré dictionnaire

                    print(toolsNER, v)
                    # print(toolsNER, value["label"], value["jalons"], v)# si en entré dictionnaire
# for pathSEM in glob.glob(path_SEM):
#     print(pathSEM)
# for pathCasEN in glob.glob(path_CasEN):
#     print(pathCasEN)