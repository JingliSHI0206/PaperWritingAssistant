from whoosh.fields import Schema
from whoosh.fields import ID, KEYWORD, TEXT
import os
from whoosh.index import create_in
from whoosh.qparser import QueryParser
from whoosh.query import Term, And,Or
from whoosh.highlight import HtmlFormatter
from whoosh.index import open_dir

class SearchPaper():
    def __init__(self, path_index, key_words=None):
        self.path_index = path_index
        self.key_words = key_words


    def sear_paper(self):
        if not self.key_words or len(self.key_words)==0:
            return '0'
        q = [Term("textdata", k) for k in self.key_words]
        index =   open_dir(self.path_index) # open_dir('paper-index')
        searcher = index.searcher()
        results = searcher.search(Or(q))
        results.fragmenter.maxchars = 30000
        results.fragmenter.surround = 150
        print('Number of hits:', len(results))
        hf = HtmlFormatter(tagname="span",classname="match", termclass="term")
        results._set_formatter(hf)

        hl_results = [hit.highlights("textdata") for hit in results]
        #for hit in results:
        #    print(hit.highlights("textdata"))
        return hl_results


if __name__ == '__main__':
    search_paper = SearchPaper(['approach', 'our'])
    search_paper.sear_paper()