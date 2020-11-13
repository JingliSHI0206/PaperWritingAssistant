import PyPDF2
import os
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pdfminer.high_level
import pdfminer.layout
import pdfminer
import sys
import subprocess
from pathlib import Path


OUTPUT_TYPES = ((".htm", "html"),
                (".html", "html"),
                (".xml", "xml"),
                (".tag", "tag"))

class Pdf2Text():
    def __init__(self,path_input=None, path_output=None):
        self.pdf_path = path_input
        self.txt_path = path_output

    def pdf2txt(self):
        os.chdir(os.getcwd())
        files_pdf = [f for f in os.listdir(self.pdf_path) if f.endswith('.pdf')]
        print('total pdf: ', len(files_pdf))
        for i, fp in enumerate(files_pdf):
            name_pdf = os.path.join(self.pdf_path , fp)
            name_txt = os.path.join(self.txt_path , fp.replace('pdf','txt'))
            print(i, name_pdf, name_txt)

            out = subprocess.Popen(['pdf2txt.py', name_pdf, '-o', name_txt],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            print(out.communicate())

            #outfp = self.extract_text(name_pdf,name_txt)
            #outfp.close()
            #outfp = open(name_txt,'wb')


            #with open(self.pdf_path + fp, "rb") as fp_pdf:
             #   pdfminer.high_level.extract_text_to_fp(fp_pdf, outfp=outfp)

            #outfp.close()

    def extract_text(fname, outfile='-',
                 no_laparams=False, all_texts=None, detect_vertical=None,
                 word_margin=None, char_margin=None, line_margin=None,
                 boxes_flow=None, output_type='text', codec='utf-8',
                 strip_control=False, maxpages=0, page_numbers=None,
                 password="", scale=1.0, rotation=0, layoutmode='normal',
                 output_dir=None, debug=False, disable_caching=False):
        #if not files:
         #   raise ValueError("Must provide files to work upon!")

        # If any LAParams group arguments were passed,
        # create an LAParams object and
        # populate with given args. Otherwise, set it to None.
        if not no_laparams:
            laparams = pdfminer.layout.LAParams()
            for param in ("all_texts", "detect_vertical", "word_margin",
                          "char_margin", "line_margin", "boxes_flow"):
                paramv = locals().get(param, None)
                if paramv is not None:
                    setattr(laparams, param, paramv)
        else:
            laparams = None

        if output_type == "text" and outfile != "-":
            for override, alttype in OUTPUT_TYPES:
                if outfile.endswith(override):
                    output_type = alttype

        if outfile == "-":
            outfp = sys.stdout
            if outfp.encoding is not None:
                codec = 'utf-8'
        else:
            outfp = open(outfile, "wb")

        #for fname in files:
        print(fname)
        with open(fname, "rb") as fp:
            pdfminer.high_level.extract_text_to_fp(fp, **locals())
        return outfp




if __name__ == '__main__':
    path_pdf = 'E:\AUT\Dataset\paper_ai_arxiv\cs.CL'
    #path_pdf = 'H:\AUT_Research_Local\LargeData\arxiv\612177_1135627_compressed_arxiv-metadata-oai-snapshot.json\paper_ai\cs.CL'
    path_text = 'text/arxiv_cs_cl/'
    #pdf2txt = Pdf2Text('pdf/','text/')
    pdf2txt = Pdf2Text(path_pdf, path_text)
    pdf2txt.pdf2txt()



