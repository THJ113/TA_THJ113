from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def temp():
    return render_template("homepage.html")

@app.route("/about")
def about():
    return render_template("about_page.html")

@app.route("/hello/<name>")
def hello(name):
    return render_template("hello_2.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
