from flask import Flask
from flask import render_template, request

app = Flask(__name__)
brojac: int = 6


rules: dict = {
    "a": "⍺",
    "b": "△",
    "c": "Ↄ",
    "č": "5",
    "ć": "M",
    "d": "7",
    "dž": "ž",
    "đ": "N",
    "e": "≠",
    "f": "⎳",
    "g": "⏜",
    "h": "X",
    "i": "⌇",
    "j": "∥",
    "k": "▻",
    "l": "⌝",
    "lj": "S",
    "m": "→",
    "n": "<",
    "nj": "⌽",
    "o": "3",
    "p": "4",
    "r": "½",
    "s": "%",
    "š": "R",
    "t": "1",
    "u": "𝞵",
    "v": "𝞿",
    "z": "𝟁",
    "ž": "₸",
    "x": "⨁",
    "y": "⥛",
    "q": "∼",
    "w": "⏚",
    " ": " ",

}
rules_reverse: dict = {}
for i in rules:
    v = rules[i]
    #    rules_reverse["lj"] = "f"
    rules_reverse[v] = i


@app.route("/")
def hello_world():
    return render_template("button.html")


@app.route('/encode', methods=['GET', 'POST'])
def encode():
    if request.method == "POST":
        uno = request.form["uno"]
        uno_e = ""
        for s in uno.lower():
            uno_e += rules.get(s, "?")
        return render_template("anakceda_in.html", uno_e=uno_e, uno=uno)
    elif request.method == "GET":
        return render_template("anakceda_in.html", uno_e="", uno="")


@app.route('/decode', methods=['GET', 'POST'])
def decode():
    if request.method == "POST":
        uno2 = request.form["uno2"]
        uno_d = ""
        for s in uno2.lower():
            uno_d += rules_reverse.get(s, "?")
        return render_template("anakceda_out.html", uno_d=uno_d, uno2=uno2)
    elif request.method == "GET":
        return render_template("anakceda_out.html", uno_d="", uno2="")
