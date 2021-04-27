from flask import Flask, request , render_template
from youtube import search
from description_search import create_woosh_index, query_on_whoosh

app = Flask(__name__) # the name of the script 

# request handler
@app.route("/")
def index(): #method name doesnt matter to flask
    return render_template("index.html")

@app.route("/query", methods=['GET','POST'])
def query():
    arg = request.args.get('q')
    if not arg or not arg.strip():
        return render_template("query.html")
  
    index_name = "whoosh_index" + arg

    if request.method=='GET':
        results = search(arg,1)
        create_woosh_index(results, index_name)
        return render_template("query.html", query_term=arg, data=results)
    
    if request.method =='POST':
        search_term = request.form['description_search']
        results = query_on_whoosh(index_name, search_term)
        return render_template("query.html", query_term=arg, data=results)


@app.route("/music", methods=['GET','POST'])
def spotify():
    arg = request.args.get('q')
    if not arg or not arg.strip():
        return render_template("music.html")
  
    index_name = "whoosh_index" + arg

    if request.method=='GET':
        results = search(arg,1)
        create_woosh_index(results, index_name)
        return render_template("music.html", query_term=arg, data=results)
    
    if request.method =='POST':
        search_term = "Spotify"#request.form['description_search']
        results = query_on_whoosh(index_name, search_term)
        return render_template("music.html", query_term=arg, data=results)