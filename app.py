from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")

def index():
    oncelik = request.args.get("oncelik")

    conn = sqlite3.connect('gorevler.db')
    cursor = conn.cursor()

    if oncelik:
        cursor.execute("SELECT * FROM gorevler WHERE oncelik=? ", (oncelik,))
    else:
        cursor.execute("SELECT * FROM gorevler")

    gorevler = cursor.fetchall()

    conn.close()

    return render_template('index.html',
                           gorevler = gorevler
                           )


@app.route("/ekle", methods=["POST"])

def ekle():
    baslik = request.form["baslik"]
    aciklama = request.form["aciklama"]
    oncelik = request.form["oncelik"]
    durum = request.form["durum"]

    conn = sqlite3.connect("gorevler.db")
    cursor = conn.cursor()

    cursor.execute("""
                  INSERT INTO gorevler (baslik, aciklama, oncelik, durum) VALUES (?,?,?,?)
    """, (baslik, aciklama, oncelik, 0))

    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/degistir/<int:id>")

def degistir(id):
    conn = sqlite3.connect("gorevler.db")
    cursor = conn.cursor()
    cursor.execute("SELECT durum FROM gorevler WHERE id=?", (id,))
    durum = cursor.fetchone()[0]
    yeni_durum = 1 if durum == 0 else 0
    cursor.execute("UPDATE gorevler SET durum=? WHERE id=?",(yeni_durum,id))

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/sil/<int:id>")

def sil(id):
    conn = sqlite3.connect("gorevler.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM gorevler WHERE id=?",(id,))

    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == ("__main__"):
    app.run(debug="True")






