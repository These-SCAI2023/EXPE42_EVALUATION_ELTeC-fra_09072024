import glob
import json
import shutil
import os

path_input="../small-ELTeC-fra/*/*REF/*.txt"


for path in glob.glob(path_input):
    if "PP" in path:
        print(path)
        os.remove(path)
    # path_output=path.split("/")
    # path_output="/".join([path_output[0],path_output[1],"DATA_ELTeC-eng_spaCy3.5.1",path_output[3],path_output[4],path_output[5],path_output[6]])
    # print(path_output)

    #
    # shutil.copytree(path,path_output)

    # shutil.rmtree(path)