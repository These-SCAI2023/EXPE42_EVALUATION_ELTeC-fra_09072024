# from supervenn import supervenn
from matplotlib import pyplot as plt
import glob
import json
import numpy as np
import pandas as pd
from upsetplot import from_memberships
from matplotlib import pyplot as plt
from upsetplot import from_contents, UpSet, plot
import re
def lire_json (chemin):
    with open(chemin) as mon_fichier:
        data = json.load(mon_fichier)
    return data


def titre_auteur(chemin):
    nomfich= chemin.split("/")[-1]
    # nomfich= nomfich.split(".")[0]
    # nomfich= nomfich.split("_")
    # # nomfich= nomfich.upper()
    # nomfich= ("_").join([nomfich[0]])
    return nomfich


def stocker(chemin, contenu):
    w = open(chemin, "w")
    w.write(json.dumps(contenu, indent=2))
    w.close()
    # print(chemin)

    return chemin


liste_ren=[]
# path_corpora = "../Upstplt-ELTeC/*fra_sp*.json"
path_corpora = "../Upsetplot_intersection"
new_dic={}
# liste_version=[]

for path in glob.glob(f"{path_corpora}/*.json"):
    print(path)
    path_output =path.split(".json")[0]
    print(path_output)
    modele_REN=(path.split("_")[-1]).split(".json")[0]
    liste_ren.append(modele_REN)
    # print(liste_ren)
    dico_entite=lire_json(path)
    # print(dico_entite["Ref"])
    for key, value in dico_entite.items():
        print(key)


        if key == "Kraken-base.txt" or key == "kraken" or key == "Kraken":
            new_key = re.sub("Kraken-base.txt|kraken|Kraken", "Kraken", key)
            print("key : ", new_key)
            new_dic[new_key] =value


        if key == "kraken-jspll-pretrain.txt" or key == "kraken-jspll-pretrain":
            new_key = re.sub("kraken-jspll-pretrain.txt|kraken-jspll-pretrain", "Kraken--jspl-fr", key)
            print("key : ", new_key)
            new_dic[new_key] = value



        if key == "Kraken-jspll-pretrain":
            new_key = re.sub("Kraken-jspll-pretrain", "Kraken--jspl-en", key)
            print("key : ", new_key)
            new_dic[new_key] = value



        if key == "kraken-jspll-ELTeC.txt" or key == "kraken-jspll-ELTeC":
            new_key = re.sub("kraken-jspll-ELTeC.txt|kraken-jspll-ELTeC", "Kraken--jspl-ELTeCfr", key)
            print("key : ", new_key)
            new_dic[new_key] = value



        if key == "Kraken-jspll-ELTeC":
            new_key = re.sub("Kraken-jspll-ELTeC", "Kraken--jspl-ELTeCen", key)
            print("key : ", new_key)
            new_dic[new_key] = value



        if key == "Kraken-jspl-ELTeC":
            new_key = re.sub("Kraken-jspl-ELTeC", "Kraken--jspl-ELTeCpt", key)
            print("key : ", new_key)
            new_dic[new_key] = value



        if key == "TesseractFra-PNG.txt" or key == "TesseractFra-PNG" or key == "TesseractFra-png":
            new_key = re.sub("TesseractFra-PNG.txt|TesseractFra-PNG|TesseractFra-png", "Tess. fr", key)
            print("key : ", new_key)
            new_dic[new_key] = value



        if key == "tesseract" or key == "Tesseract-PNG":
            new_key = re.sub("tesseract|Tesseract-PNG", "Tess.", key)
            print("key : ", new_key)
            new_dic[new_key] = value



        if key == "TesseractPor-PNG":
            new_key = re.sub("TesseractPor-PNG", "Tess. pt", key)
            print("key : ", new_key)
            new_dic[new_key] = value



        if key == "TesseractFra-PNG-jspll-pretrain.txt" or key == "TesseractFra-PNG-jspll-pretrain":
            new_key = re.sub("TesseractFra-PNG-jspll-pretrain.txt|TesseractFra-PNG-jspll-pretrain",
                             "Tess. fr -- jspl-fr", key)
            print("key : ", new_key)
            new_dic[new_key] = value



        if key == "tesseract-jspll-pretrain" or key == "Tesseract-PNG-jspll-pretrain":
            new_key = re.sub("tesseract-jspll-pretrain|Tesseract-PNG-jspll-pretrain", "Tess. -- jspl-en", key)
            print("key : ", new_key)
            new_dic[new_key] = value



        if key == "TesseractFra-PNG-jspll-ELTeC.txt" or key == "TesseractFra-PNG-jspll-ELTeC":
            new_key = re.sub("TesseractFra-PNG-jspll-ELTeC.txt|TesseractFra-PNG-jspll-ELTeC",
                             "Tess. fr -- jspl-ELTeCfr", key)
            print("key : ", new_key)
            new_dic[new_key] = value



        if key == "Tesseract-PNG-jspll-ELTeC":
            new_key = re.sub("Tesseract-PNG-jspll-ELTeC", "Tess. -- jspl-ELTeCen", key)
            print("key : ", new_key)
            new_dic[new_key] = value


        if key == "TesseractPor-PNG-jspl-ELTeC":
            new_key = re.sub("TesseractPor-PNG-jspl-ELTeC", "Tess. pt -- jspl-ELTeCpt", key)
            print("key : ", new_key)
            new_dic[new_key] = value


        if key == "Ref":
            new_key = re.sub("Ref", "Ref.", key)
            print("key : ", new_key)
            new_dic[new_key] = value

        if key == "tesseract0.3.10":
            new_key = re.sub("tesseract0.3.10", "Tess. fr 3.10", key)
            print("key : ", new_key)
            new_dic[new_key] = value

        if key == "kraken4.3.13.dev25":
            new_key = re.sub("kraken4.3.13.dev25", "Kraken 4.3.13", key)
            print("key : ", new_key)
            new_dic[new_key] = value

        if key == "lectaurep-kraken4.3.13.dev25":
            new_key = re.sub("lectaurep-kraken4.3.13.dev25", "Kraken Lectp. 4.3.13", key)
            print("key : ", new_key)
            new_dic[new_key] = value

# print(i, new_dic.keys())
    liste_moteur=[]
    a=6

    for cle, valeur in new_dic.items():
        liste_moteur.append(cle)

    dico_entite = {k: set(v)for k,v in new_dic.items() if k ==liste_moteur[a] or k =="Ref."}

    test = from_contents(dico_entite)
    upset = UpSet(
        test,
        orientation='horizontal',
        sort_by='degree',
        # subset_size='count',
        # show_counts=True,
        totals_plot_elements=3,
        show_percentages=True
    )
    # upset.style_subsets(
    #     present=["sm", "lg"],
    #     absent=[
    #         "flair",
    #         "camenBert"
    #     ],
    #     edgecolor="yellow",
    #     facecolor="blue",
    # )

    fig = plt.figure()
    fig.legend(loc=7)
    plt.subplots_adjust(left=0.112, right=0.975, top=0.782, bottom=0.101, wspace=0.2, hspace=0.2)
    upset.plot(fig=fig)
    for text in fig.findobj(plt.Text):
        if "%" in text.get_text():
            text.set_fontsize(8)
    # plt.suptitle("Représentation de \n l'intersection des lexiques", fontsize=20)
    # fig.figsize = (10, 6)
    plt.yscale('log', base=2)
    # plt.axis([-1, 2.3, 0, 8000])
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.savefig(f"{path_output}_{liste_moteur[a]}_upsetplot.png", dpi=300)
    plt.show()




# # ##SuperVenn
    # for key, value in dico_entite.items():
    #     if key=="sm":
    #         sm=set(value)
    #         print(len(sm))
    #     if key=="lg":
    #         lg = set(value)
    #     if key=="camenBert":
    #         camenBert = set(value)
    #     if key=="flair":
    #         flair = set(value)

    # sets = [sm, lg, camenBert, flair]
    # labels = ["sm", "lg", "camenBert", "flair"]
    # plt.figure(figsize=(10, 6))
    # supervenn(sets, labels, widths_minmax_ratio=0.1, sets_ordering='minimize gaps', rotate_col_annotations=True, col_annotations_area_height=1.2 )
    #
    # plt.savefig("%s_image.png"%path_output,dpi=300, bbox_inches="tight")

