# Flask POST Sederhana

Project sederhana Flask untuk belajar **parsing parameter dengan method POST**.
Pengguna mengisi nama pada form, data dikirim lewat method POST, lalu server
menampilkan hasilnya pada label.

## Struktur project
```
.
├── app.py                 # aplikasi Flask (route GET "/" dan POST "/proses")
├── templates/
│   └── index.html         # TextField, Button, dan Label
├── static/
│   └── styles.css         # tampilan (opsional)
├── requirements.txt
└── README.md
```

## Cara menjalankan
1. Pasang Flask:
   ```bash
   pip install flask
   ```
   (atau `pip3 install flask`, atau `pip install -r requirements.txt`)
2. Jalankan aplikasi:
   ```bash
   python app.py
   ```
3. Buka http://127.0.0.1:5000 di browser.

## Cara kerja
- `GET /` menampilkan halaman `index.html`.
- Form pada halaman mengirim field `nama` ke `POST /proses`.
- Di `app.py`, parameter dibaca dengan `request.form.get("nama")`.
- Hasilnya dikirim kembali ke template dan ditampilkan pada label `#hasil`.
- Jika nama kosong, server membalas status 400 dengan pesan kesalahan.

## Mencoba dengan curl
```bash
curl -X POST -d "nama=Budi" http://127.0.0.1:5000/proses
```
