from whoosh.fields import Schema
from whoosh.fields import ID, KEYWORD, TEXT
from whoosh import index
import os
from whoosh.index import create_in
from whoosh.qparser import QueryParser
from whoosh.query import Term, And
from whoosh.index import open_dir

class CreateIndex():
    def __init__(self, path_index, path_text):
        self.path_index = path_index
        self.path_text = path_text
    def create_index(self):
        pdf_schema = Schema(id = ID(unique=True,stored=True),
                            path=ID(stored=True),
                            title=TEXT(stored=True),
                            text=TEXT,
                            textdata=TEXT(stored=True))
        if not os.path.exists(self.path_index):
            os.mkdir(self.path_index)
        index = create_in(self.path_index,pdf_schema)
        #index = open_dir('paper-index')

        paper_writer = index.writer()
        files_txt = [f for f in os.listdir(self.path_text) if f.endswith('.txt')]
        print('total paper: ', len(files_txt))
        for i, f in enumerate(files_txt):
            print('{}/{} - {}'.format(i, len(files_txt), f))
            paper_writer.add_document(id=f,
                                      textdata=open(os.path.join(self.path_text, f),encoding='utf-8').read()
                                      )
        paper_writer.commit()


if __name__ == '__main__':
    path_index = 'E:\AUT\Dataset\paper_index\cs_CL'
    path_paper_text = 'E:\AUT\Dataset\paper_text\cs_CL'
    createIndx = CreateIndex(path_index, path_paper_text)
    createIndx.create_index()