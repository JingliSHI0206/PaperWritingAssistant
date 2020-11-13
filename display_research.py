from flask import Flask
from flask import render_template
from flask import request,jsonify
from flask import redirect
import datetime
from search_paper import SearchPaper

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('search_results.html')

@app.route('/search_paper')
def search_paper():
    res = request.args.get('keywords','')
    keywords = [w for w in res.split(' ')]
    print(keywords)

    res_paper = get_resutls(keywords)
    print('res: ', len(res_paper))
    return jsonify(res_paper=res_paper)

def get_resutls(keywords=None):
    if len(keywords) == 0:
        return ''
    path_index = 'YOUR PAPER INDEX PATH'
    search_paper = SearchPaper(path_index,keywords)
    res = search_paper.sear_paper()
    return res

if __name__ == '__main__':
    app.run()
