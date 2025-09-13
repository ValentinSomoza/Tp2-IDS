from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")

def index():
    title = "Club social socialisimo de la sociedad social sintiente"
    return render_template('index.html',page_title = title)

if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)