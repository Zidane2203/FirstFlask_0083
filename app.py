from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Flask berjalan."


@app.route("/proses", methods=["POST"])
def proses():
    # Parsing parameter dari body request (form) yang dikirim dengan method POST
    nama = request.form.get("nama", "").strip()
    if not nama:
        return "Nama tidak boleh kosong.", 400
    return f"Halo, {nama}! Data diterima lewat method POST."


if __name__ == "__main__":
    app.run(debug=True)
