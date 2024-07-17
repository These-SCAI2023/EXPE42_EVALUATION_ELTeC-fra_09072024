#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:18:42 2024

@author: mandar
"""

import shutil
import glob

# shutil.rmtree()

path_corpora = "../ELTeC-fra_09072024_complet/*/*"

# for path in glob.glob(path_corpora):
#     print(path)
#     # if "REF" in path:
#     #     shutil.rmtree(f"{path}/NER_concat")
#     if "REF" in path:
#         for path_file in glob.glob(f"{path}/NER_concat"):
#             shutil.rmtree(path_file)
        
    # if "NER_concat" in path:
        # shutil.rmtree(path)

for path in glob.glob(path_corpora):
    # print(path)
    if "REF" in path:
        for path_file in glob.glob(f"{path}/NER_concat"):
            print(path_file)
            
    if "OCR" in path:
        for path_file in glob.glob(f"{path}/*/NER_concat"):
            
            print(path_file)
            