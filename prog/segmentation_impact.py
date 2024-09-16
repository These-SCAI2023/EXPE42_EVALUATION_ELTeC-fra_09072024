import glob
import spacy
import json


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


def stocker(chemin, contenu):
    w = open(chemin, "w")
    w.write(json.dumps(contenu, indent=2))
    w.close()
    # print(chemin)
    return chemin


path_corpora = "../small-ELTeC-fra-2021-2024_REN/MAUPASSANT/*"
start_char = 16492-80
end_char = 16505+80
modeles = ["lg", "md", "sm"]
# modeles = ["md"]
for mod in modeles:
    nlp = spacy.load(f"fr_core_news_{mod}")
    dico_sent = {}
    dico_tok = {}
    o = 0
    i = 0

    print(f"Le modèle : {mod}")
    for path_file in glob.glob(path_corpora):
        if "REF" in path_file:
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
                stocker(f"{reffile}_tok_{mod}.json", dico_tok)
                stocker(f"{reffile}_seg_{mod}.json", dico_sent)

        if "OCR" in path_file:
            ocr_files = f"{path_file}/*/*.txt"
            for ocrfile in glob.glob(ocr_files):
                dicocr_sent = {}
                dicocr_tok = {}
                oc = 0
                ic = 0
                print("OCR", ocrfile)
                texte_ocr = lire_fichier(ocrfile)
                # print(texte[start_char:end_char])
                # doc = nlp(texte[start_char:end_char])
                doc_ocr = nlp(texte_ocr)
                # ##Token Segmentation
                dicocr_tok = tokenisation(doc_ocr, dicocr_tok, oc)
                # ##Sentence Segmentation
                dicocr_sent = sent_seg(doc_ocr, dicocr_sent, ic)

                stocker(f"{ocrfile}_tok_{mod}.json", dicocr_tok)
                stocker(f"{ocrfile}_seg_{mod}.json", dicocr_sent)
