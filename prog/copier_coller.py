import glob
import json
import shutil
import os

path_input="../small-ELTeC-fr*/*/*OCR/*/"


for path in glob.glob(path_input):
    if "jspll" in path or "jspl" in path:
        print(path)
        shutil.rmtree(path)

    # path_rename= "/".join(path.split("/")[:3])+"/"+path.split("/")[2]+"_REF"
    # print(path_rename)
    # os.rename(path, path_rename)

    # path_output=path.split("/")
    # path_output="/".join([path_output[0],path_output[1],"DATA_ELTeC-eng_spaCy3.5.1",path_output[3],path_output[4],path_output[5],path_output[6]])
    # print(path_output)

    # os.remove(path)
    # shutil.copytree(path,path_output)

