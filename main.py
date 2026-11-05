import random

from flask import Flask

app = Flask(__name__)
facts_list = [
    "Kebanyakan orang yang menderita kecanduan teknologi mengalami stres yang kuat ketika mereka berada di luar area jangkauan jaringan atau tidak dapat menggunakan perangkat mereka",
    "Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.",
    "Studi tentang ketergantungan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan"
]

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1><a href="/tes">View a random fact!</a>'

@app.route("/tes")
def tes_python():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/secret")
def secret():
    return '<h1>Sebenarnya aku adalaah youtuber dan developer scratch kecil!</h1><a href="https://www.youtube.com/@Galoreclue/featured"><iframe width="560" height="315" src="https://www.youtube.com/embed/_g18Ny4gYc8?si=mnVM0jXoOGqiOBg_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></a>'

app.run(debug=True)


