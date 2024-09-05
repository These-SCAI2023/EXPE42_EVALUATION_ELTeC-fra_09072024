import glob
import spacy
import json
def lire_fichier(chemin):
    f = open(chemin, encoding='utf−8')
    chaine = f.read()
    return chaine

def stocker(chemin, contenu):
    w = open(chemin, "w")
    w.write(json.dumps(contenu, indent=2))
    w.close()
    # print(chemin)
    return chemin

path_corpora="../small-ELTeC-fra-2021-2024_REN/ADAM/*"
start_char= 16492-200
end_char= 16505+200
modeles=["lg","sm","md"]

i=0

for mod in modeles:
    nlp = spacy.load(f"fr_core_news_{mod}")
    dico_res = {}
    print(f"Le modèle : {mod}")
    for path_file in glob.glob(path_corpora):
        if "REF" in path_file:
                    ref_files= f"{path_file}/*.txt"
                    for reffile in glob.glob(ref_files):
                        print("REF", reffile)
                        texte = lire_fichier(reffile)
                        texte = lire_fichier(reffile)
                        print(texte[start_char:end_char])
                        doc = nlp(texte[start_char:end_char])

                        for ent in doc.ents:
                            print(ent.text, ent.start_char, ent.end_char, ent.label_)


##Segmentation

                        doc = nlp(texte)
                        assert doc.has_annotation("SENT_START")
                        for sent in doc.sents:
                            dico_res["segment" + str(i)] = sent.text
                            i=i+1
                            # print(i,"******",sent.text)
                    stocker(f"{reffile}_seg_{mod}.json",dico_res)


##REN
        # print(path_file)
        # if "OCR" in path_file:
        #     ocr_files= f"{path_file}/*/*.txt"
        #     for ocrfile in glob.glob(ocr_files):
        #         print("OCR",ocrfile)
        #         texte = lire_fichier(ocrfile)
        #         print(texte[238567:238599])


        # if "REF" in path_file:
        #     ref_files= f"{path_file}/*.txt"
        #     for reffile in glob.glob(ref_files):
        #         print("REF", reffile)
        #