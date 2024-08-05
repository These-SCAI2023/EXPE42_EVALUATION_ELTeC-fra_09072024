import glob
import json
import shutil
import os

# path_input="../ARCHEO_Corr/small-ELTeC-fra2024*/*"
path_input="../PREPA_Correction-Auto/small-ELTeC-fra-2021-*/*/*REF/NER/*"


for path in glob.glob(path_input):
    # print(path)
    if "_PP.txt" in path:
        print(path)
        # os.remove(path)

    # if "AIMARD" not in path:
        # print(path)
        # path_rename=path.split("_")
        # path_rename = "_".join(path_rename[:3])


    # if "-jspll-" in path or "-jspl-" in path:
    #     print(path)
    #     shutil.rmtree(path)

    # path_rename= "/".join(path.split("/")[:4])+"/"+path.split("/")[3]+"_REF"
    # print(path_rename)
    # os.rename(path, path_rename)



    # path_output=path.split("/")
    # path_output="/".join([path_output[0],path_output[1],"DATA_ELTeC-eng_spaCy3.5.1",path_output[3],path_output[4],path_output[5],path_output[6]])
    # print(path_output)


    # shutil.copytree(path,path_output)

