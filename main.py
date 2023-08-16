from flask import Flask, render_template, url_for
app = Flask(__name__)

lang_flag_dicts = [{"lang":"Thai", "flag":"thai-flag.png"}, {"lang":"Spanish", "flag":"spanish-flag.png"}]

@app.route("/")
def index():
    return render_template("home.html", langs=lang_flag_dicts)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)