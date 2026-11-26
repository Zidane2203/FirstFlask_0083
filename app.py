from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """Menampilkan halaman form."""
    return render_template("index.html", pesan=None, nama="")


@app.route("/proses", methods=["POST"])
def proses():
    """Menerima data form lewat method POST lalu menampilkan hasilnya."""
    # Parsing parameter dari body request (form) yang dikirim dengan method POST
    nama = request.form.get("nama", "").strip()

    if not nama:
        pesan = "Nama tidak boleh kosong."
        sukses = False
        kode = 400
    else:
        pesan = f"Halo, {nama}! Data berhasil diterima lewat method POST."
        sukses = True
        kode = 200

    return render_template("index.html", pesan=pesan, sukses=sukses, nama=nama), kode


if __name__ == "__main__":
    app.run(debug=True)
