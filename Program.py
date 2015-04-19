from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def temp():
    return render_template("homepage.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/guides")
def guides():
    return render_template("guides.html")

if __name__ == "__main__":
    app.run(debug=True)
