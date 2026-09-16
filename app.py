# my first DAPP
from flask import Flask, render_template, request
app = Flask(__name__) #normal naming convention in Flask
@app.route("/", methods=["GET","POST"])
def index():
    return(render_template("index.html"))
if __name__=="__main__":
    app.run()
