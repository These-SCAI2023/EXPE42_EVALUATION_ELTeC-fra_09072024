import glob
import json
# import numpy as np
# import pandas as pd
# from upsetplot import from_memberships
from matplotlib import pyplot as plt
from upsetplot import from_contents, UpSet
import re
from renommage import *
import os


def lire_json(chemin):
    with open(chemin) as mon_fichier:
        data = json.load(mon_fichier)
    return data

def titre_auteur(chemin):
    nomfich = chemin.split("/")[-1]
    return nomfich


def stocker(chemin, contenu):
    w = open(chemin, "w")
    w.write(json.dumps(contenu, indent=2))
    w.close()
    # print(chemin)

    return chemin




# path_corpora = "../Upstplt-ELTeC/*fra_sp*.json"
# path_corpora = "../Upsetplot_intersection/GLOBAL/small-*"
path_corpora = "../CORRECTION_DISTANCES/Upsetplot_intersection/GLOBAL/small-*"
# liste_version=[]
size=[2000, 4000, 6000, 10000,15000,20000,30000]
for path in glob.glob(f"{path_corpora}"):
    # print(path)
    new_dic = {}
    liste_ren = []
    output = path.split("/")
    # rep_out = "/".join([output[0], output[1], output[2], output[3], output[3] +"_PNG"])
    rep_out = "/".join([output[0], output[1], output[2], output[3],output[4], output[4] + "_PNG"])
    print("------ Rep_out : ",rep_out)
    if os.path.exists(rep_out) == False:
        os.mkdir(rep_out) ### Creéer le dossier

    for subpath in glob.glob(f"{path}/*.json"):
        path_output = "/".join([rep_out, subpath.split("/")[-1]])
        print("PATH OUTPUT : ", path_output)
        if os.path.exists(path_output) == False:


            modele_REN = (subpath.split("_")[-1]).split(".json")[0]
            liste_ren.append(modele_REN)
            print(liste_ren)
            dico_entite = lire_json(subpath)
            # print(dico_entite["Ref"])
            for key, value in dico_entite.items():
                print("OLD kEY : ",key)
                nouv_kee= nommage(key)
                new_dic[nouv_kee] = value
    # print("new_dic.keys()------>",new_dic.keys())

            liste_moteur = []


            for cle, valeur in new_dic.items():
                liste_moteur.append(cle)

                print("LISTE MOTEUR",liste_moteur)
            liste_moteur.remove("Ref.")
            print("LISTE MOTEUR", liste_moteur)

            for a in range(16):
                # print(a)

                if a>=len(liste_moteur):
                    print(len(liste_moteur))
                    print("liste_moteur trop petite")
                    continue
                print(len(liste_moteur))
                print("liste_moteur OK")
                #
                dico_entite = {k: set(v)for k, v in sorted(new_dic.items()) if k == liste_moteur[a] or k == "Ref."}

                test = from_contents(dico_entite)
                upset = UpSet(
                    test,
                    facecolor="silver",
                    orientation='horizontal',
                    sort_by='degree',
                    # subset_size='count',
                    # show_counts=True,
                    totals_plot_elements=3,
                    show_percentages=True
                )
                upset.style_subsets(
                    present="Ref.",
                    # label="Réf.",
                    # absent=[
                    #     "flair",
                    #     "camenBert"
                    # ],
                    edgecolor="firebrick",
                    # facecolor="dimgray",
                    # hatch="xx"
                )
                upset.style_subsets(
                    present=liste_moteur[a],
                    # label=liste_moteur[a],
                    # absent=[
                    #     "flair",
                    #     "camenBert"
                    # ],
                    # edgecolor="royalblue",
                    facecolor="steelblue",

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
                # params = {'legend.loc':"lower center",'legend.frameon':True,'legend.fontsize': 8}
                # with plt.rc_context(params):
                #     upset.plot()
                for x in size:
                    fig = plt.figure()
                    fig.legend(loc=7)
                    plt.subplots_adjust(left=0.112, right=0.975, top=0.782, bottom=0.101, wspace=0.2, hspace=0.2)
                    upset.plot(fig=fig)
                    for text in fig.findobj(plt.Text):
                        if "%" in text.get_text():
                            text.set_fontsize(8)
                    # plt.suptitle("Représentation de \n l'intersection des lexiques", fontsize=20)
                    # fig.figsize = (10, 6)
                    # plt.yscale('log', base=10)

                    plt.axis([-1.0, 2.3, 0.0, x])
                    plt.xticks(fontsize=8)
                    plt.yticks(fontsize=8)
                    plt.savefig(f"{path_output}_{liste_moteur[a]}_upsetplot-size-{x}.png", dpi=300)
                    # plt.show()
                    plt.close
