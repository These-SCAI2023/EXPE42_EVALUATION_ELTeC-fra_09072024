import glob
import json
import shutil
import os
import re

# path_input="../ARCHEO_Corr/small-ELTeC-fra2024*/*"
# path_input="../small-ELTeC-fra_SEM-WiNER/*/*/*/*"
path_input="../Upsetplot_intersection/GLOBAL/small-ELTeC-fra-2021-2024_REN/small-ELTeC-fra-2021-2024_REN_PNG/*10000.png"
path_output = "../Upsetplot_intersection/GLOBAL/small-ELTeC-fra-2021-2024_REN/small-ELTeC-fra-2021-2024_REN_PNG_10000/"
# path_input="../Archeo_spaCy-3.7.5/small-*/*/*REF/*/*"

for path in glob.glob(path_input):
    print(path)
    pathout = path.split("/")[-1]
    print(pathout)
    output = path_output+pathout
    print(">>",output)

    # rep_output=path.split("_")
    # print("rep_output",rep_output)
    # path_output= "../ARCHEO_Correction_Distances"+"/"+rep_output[-2].split("/")[-1]+"/"+path.split("/")[-1]
    # print("PATH OUTPUT",path_output)
    # shutil.copytree(path,path_output)

    # shutil.rmtree(path)
    # if "spacy-lg" in path or "spacy-sm" in path or "spacy-md" in path:
    #     print(path)
    #     os.remove(path)

   ### Renommer les fichiers pour TGB revue TAL ? ou Corpus ?
    # if "tesseract" in path:
    #     path_rename=re.sub("tesseract","tesseract0.3.10", path)
    #     print("version : ", path_rename)
    #     os.rename(path, path_rename)
    # if "kraken" in path:
    #     path_renamek=re.sub("kraken","kraken4.3.13.dev25", path)
    #     print("version : ", path_renamek)
    #     os.rename(path, path_renamek)

    # if ".txt.json" in path:
        # os.remove(path)

    # if "spacy" not in path:
    #     print(path)
    #     os.remove(path)

    # if "_PP.txt" in path:
    #     print(path)
    #     os.remove(path)


    # if "AIMARD" not in path:
    #     # print(path)
    #     path_rename=path.split("/")
    #     path_rename = "/".join(path_rename[:4])+"/"+path_rename[3]+"_"+path_rename[-1]
    #     print(path_rename)
    #
    #     os.rename(path, path_rename)

## Retirer les dossiers jamspell
    # if "-jspll-" in path or "-jspl-" in path:
    #     print(path)
    #     shutil.rmtree(path)

    # path_output=path.split("/")
    # rep_output=path_output[2].split("-")
    # rep_output="-".join(rep_output[:3])
    # print("REP OUTPUT",rep_output)
    # path_output="/".join([path_output[0],path_output[1],rep_output,path_output[3],path_output[4],path_output[5],path_output[6]])
    # print("PATH OUTPUT",path_output)
    # #
    # #
    shutil.copy2(path,output)

