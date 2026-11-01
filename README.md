# Sistem Perpustakaan

## 1. Deskripsi Aplikasi

Sistem Perpustakaan merupakan aplikasi berbasis Python yang dirancang untuk membantu pengelolaan data perpustakaan. Aplikasi ini menerapkan pola arsitektur Model-View-Controller (MVC) untuk memisahkan pengelolaan data, proses bisnis, dan tampilan antarmuka pengguna.

Aplikasi menyediakan halaman login sebagai proses autentikasi pengguna serta pengelolaan data buku.

## 2. Struktur Direktori MVC

Struktur direktori proyek Sistem Perpustakaan adalah sebagai berikut:

```text
modul 8 tugas/
│
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml
│
├── config/
│   ├── __init__.py
│   └── database.py
│
├── controllers/
│   ├── __init__.py
│   ├── auth_controller.py
│   └── buku_controller.py
│
├── models/
│   ├── __init__.py
│   ├── user_model.py
│   └── buku_model.py
│
├── views/
│   ├── login_view.py
│   └── buku_view.py
│
├── tests/
│   ├── test_auth.py
│   └── test_buku.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

**Penjelasan struktur direktori:**

- **config:** Menyimpan konfigurasi aplikasi, termasuk koneksi database MySQL.
- **controllers:** Mengatur proses bisnis dan menghubungkan model dengan tampilan.
- **models:** Mengelola data pengguna dan data buku serta interaksi dengan database.
- **views:** Menampilkan antarmuka aplikasi kepada pengguna.
- **tests:** Menyimpan skrip pengujian otomatis untuk autentikasi dan pengelolaan buku.
- **.github/workflows:** Menyimpan konfigurasi GitHub Actions untuk menjalankan CI Pipeline.
- **main.py:** Menjadi file utama untuk menjalankan aplikasi.
- **requirements.txt:** Menyimpan daftar pustaka atau dependensi Python yang digunakan.

## 3. Panduan Instalasi dan Konfigurasi Database MySQL

### A. Persiapan

Pastikan perangkat telah memiliki:

- Python.
- Visual Studio Code.
- Laragon.
- MySQL.
- Git (opsional, untuk pengelolaan repositori).

### B. Membuat Virtual Environment

Buka terminal pada direktori proyek, kemudian jalankan:

```powershell
python -m venv env
```

Aktifkan virtual environment menggunakan perintah:

```powershell
.\env\Scripts\Activate.ps1
```

### C. Instalasi Dependensi

Instal seluruh pustaka yang dibutuhkan aplikasi menggunakan perintah:

```powershell
python -m pip install -r requirements.txt
```

### D. Konfigurasi Database MySQL

1. Buka aplikasi Laragon.
2. Aktifkan layanan MySQL.
3. Buka phpMyAdmin atau perangkat pengelolaan database yang digunakan.
4. Buat database sesuai nama database yang digunakan dalam konfigurasi proyek.
5. Buka file `config/database.py`.
6. Sesuaikan konfigurasi host, username, password, dan nama database dengan pengaturan MySQL pada perangkat.

Pastikan koneksi database berhasil sebelum menjalankan aplikasi.

## 4. Cara Menjalankan Aplikasi

Setelah instalasi dependensi dan konfigurasi database selesai, jalankan aplikasi melalui terminal VS Code dengan perintah:

```powershell
python main.py
```

Aplikasi akan menampilkan halaman login Sistem Perpustakaan. Pengguna dapat memasukkan username dan password yang telah terdaftar untuk melakukan autentikasi.

## 5. Pengujian Otomatis dan CI Pipeline

Proyek ini menggunakan Pytest untuk menjalankan pengujian otomatis dan Flake8 untuk memeriksa kualitas penulisan kode.

Pengujian dapat dijalankan menggunakan perintah:

```powershell
python -m pytest -v
```

Pemeriksaan kualitas kode menggunakan Flake8:

```powershell
flake8 models/ controllers/ --count --select=E9,F63,F7,F82 --show-source --statistics
```

Selain itu, GitHub Actions digunakan untuk menjalankan proses integrasi dan pengujian secara otomatis ketika terdapat perubahan kode pada repositori.