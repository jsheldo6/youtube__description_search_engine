from flask import Flask, request , render_template
from youtube import search
from description_search import create_woosh_index

app = Flask(__name__) # the name of the script 

# request handler
@app.route("/")
def index(): #method name doesnt matter to flask
    username = request.args.get('name')
    if not username or not username.strip():
        username = "World"

    return render_template("index.html",name=username)

#100.25.129.237
@app.route("/query")
def query():
    arg = request.args.get('q')
    if not arg or not arg.strip():
        return render_template("query.html")

    index_name = "whoosh_index" + query_term
    results = search(arg,1)
    create_woosh_index(results,index_name)
    return render_template("query.html",data=results)
