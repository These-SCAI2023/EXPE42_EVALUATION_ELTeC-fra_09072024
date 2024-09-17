import glob
import spacy
import json
import os


def lire_fichier(chemin):
    f = open(chemin, encoding='utf−8')
    chaine = f.read()
    return chaine


def sent_seg(texte_analyse, dico_result, cpt):
    assert texte_analyse.has_annotation("SENT_START")
    for sent in texte_analyse.sents:
        dico_result["segment_" + str(cpt)] = sent.text
        cpt = cpt + 1
    return dico_result


def tokenisation(texte_analyse, dico_result, cpt):
    for token in texte_analyse:
        dico_result[f"token_{cpt}"] = token.text
        cpt = cpt + 1
    return dico_result


def postag(texte_analyse, dico_result, cpt):

    for token in texte_analyse:
        dico_result[f"token_{cpt} "] = {}
        dico_result[f"token_{cpt} "]["text :"] = token.text
        dico_result[f"token_{cpt} "]["token.lemma_ "] = token.lemma_
        dico_result[f"token_{cpt} "]["token.pos_ "] = token.pos_
        dico_result[f"token_{cpt} "]["token.tag_ "] = token.tag_
        dico_result[f"token_{cpt} "]["token.dep_ "] = token.dep_
        dico_result[f"token_{cpt} "]["token.shape_ "] = token.shape_
        dico_result[f"token_{cpt} "]["token.is_alpha"] = token.is_alpha
        dico_result[f"token_{cpt} "]["token.is_stop"] = token.is_stop
        cpt = cpt + 1
        # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
    return dico_result


def stocker(chemin, contenu):
    w = open(chemin, "w")
    w.write(json.dumps(contenu, indent=2))
    w.close()
    # print(chemin)
    return chemin


path_corpora = "../small-ELTeC-fra-2021-2024_REN/MAUPASSANT/*"
start_char = 16492-80
end_char = 16505+80
# modeles = ["lg", "md", "sm"]
modeles = ["md"]
for mod in modeles:
    nlp = spacy.load(f"fr_core_news_{mod}")
    dico_sent = {}
    dico_tok = {}
    dico_postag = {}
    o = 0
    i = 0
    p = 0

    print(f"Le modèle : {mod}")
    for path_file in glob.glob(path_corpora):
        if "REF" in path_file:
            print("ok")
            outputdir_ref = f'{path_file}/Pos_Seg_Tok'
            os.mkdir(outputdir_ref)

            ref_files = f"{path_file}/*.txt"
            for reffile in glob.glob(ref_files):
                print("REF", reffile)
                texte = lire_fichier(reffile)
                # print(texte[start_char:end_char])
                # doc = nlp(texte[start_char:end_char])
                doc = nlp(texte)
                ##Token Segmentation
                dico_tok = tokenisation(doc, dico_tok, o)
                ##Sentence Segmentation
                dico_sent = sent_seg(doc, dico_sent, i)
                dico_postag = postag(doc, dico_postag, p)
                path_out_ref = "/".join(reffile.split("/")[:4]) + "/Pos_Seg_Tok/" + reffile.split("/")[4]

                stocker(f"{path_out_ref}_tok_{mod}.json", dico_tok)
                stocker(f"{path_out_ref}_seg_{mod}.json", dico_sent)
                stocker(f"{path_out_ref}_postag_{mod}.json", dico_postag)

        if "OCR" in path_file:
            ocr_files = f"{path_file}/*"
            for ocrdir in glob.glob(ocr_files):
                outputdir = f'{ocrdir}/Pos_Seg_Tok'
                os.mkdir(outputdir)
            for ocrfile in glob.glob(f"{ocr_files}/*.txt"):
                dicocr_sent = {}
                dicocr_tok = {}
                dicocr_postag = {}
                oc = 0
                ic = 0
                pc = 0
                print("OCR", ocrfile)
                texte_ocr = lire_fichier(ocrfile)
                # print(texte[start_char:end_char])
                # doc = nlp(texte[start_char:end_char])
                doc_ocr = nlp(texte_ocr)
                # ##Token Segmentation
                dicocr_tok = tokenisation(doc_ocr, dicocr_tok, oc)
                # ##Sentence Segmentation
                dicocr_sent = sent_seg(doc_ocr, dicocr_sent, ic)
                dicocr_postag = postag(doc_ocr, dicocr_postag, pc)
                path_out = "/".join(ocrfile.split("/")[:5])+"/Pos_Seg_Tok/"+ocrfile.split("/")[5]
                print(path_out)

                stocker(f"{path_out}_tok_{mod}.json", dicocr_tok)
                stocker(f"{path_out}_seg_{mod}.json", dicocr_sent)
                stocker(f"{path_out}_postag_{mod}.json", dicocr_postag)
