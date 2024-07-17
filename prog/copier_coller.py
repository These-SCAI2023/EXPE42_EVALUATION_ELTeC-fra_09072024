import glob
import json
import shutil

path_input="../copier_coller/DATA_ELTeC-eng_spaCy3.5.1_sim2-3-word/*/*OCR/*/SIM"


for path in glob.glob(path_input):
    # print(path)
    path_output=path.split("/")
    path_output="/".join([path_output[0],path_output[1],"DATA_ELTeC-eng_spaCy3.5.1",path_output[3],path_output[4],path_output[5],path_output[6]])
    print(path_output)


    shutil.copytree(path,path_output)