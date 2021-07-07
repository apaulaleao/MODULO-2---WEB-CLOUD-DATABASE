from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

registros=[
    {
        "id":1,
        "nome": "A Procura da Felicidade",
        "imagem_url": "https://images-na.ssl-images-amazon.com/images/I/91NGsamrW2L.jpg"
    },
    {
        "id":2,
        "nome": "A Procura da Felicidade",
        "imagem_url": "https://images-na.ssl-images-amazon.com/images/I/91NGsamrW2L.jpg"
    },

]

@app.route("/read")
def read_all():
    render_template('read_all.html', registros=registros)


if(__name__ == "__main__"):
   app.run(debug=True)
