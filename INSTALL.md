# PANDUAN INSTALASI DAN SETUP
# Sistem Pemesanan Restoran

## Prerequisites

Sebelum memulai, pastikan Anda telah menginstall:
- Python 3.8 atau lebih tinggi
- MySQL atau MariaDB
- pip (Python package manager)

## Langkah-Langkah Instalasi

### 1. Download Project

```powershell
# Navigasi ke folder project
cd d:\Coding\restaurant-system-management
```

### 2. Install Dependencies Python

```powershell
# Install library yang dibutuhkan
pip install -r requirements.txt
```

**Isi requirements.txt:**
- mysql-connector-python==8.0.33

### 3. Setup MySQL/MariaDB

#### Option A: Setup Otomatis (Recommended)

Aplikasi akan membuat tabel secara otomatis saat pertama kali dijalankan.

```powershell
# Langsung jalankan aplikasi
python main.py
```

Masukkan kredensial database:
- Host: localhost
- Database: restaurant_db
- User: root
- Password: [password Anda]

#### Option B: Setup Manual

```powershell
# Login ke MySQL
mysql -u root -p

# Atau untuk MariaDB
mariadb -u root -p
```

```sql
-- Buat database
CREATE DATABASE restaurant_db;

-- Gunakan database
USE restaurant_db;

-- Jalankan script SQL
SOURCE d:/Coding/restaurant-system-management/database/setup.sql;
```

### 4. Verifikasi Instalasi

```powershell
# Test koneksi database dan jalankan unit tests
python -m tests.test_models
```

**Expected Output:**
```
test_create_pelanggan (tests.test_models.TestPelanggan) ... ok
test_display_info (tests.test_models.TestPelanggan) ... ok
...
----------------------------------------------------------------------
Ran 27 tests in 0.XXXs

OK
```

### 5. Jalankan Aplikasi

```powershell
python main.py
```

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'mysql'"

**Solusi:**
```powershell
pip install mysql-connector-python
```

### Error: "Access denied for user 'root'@'localhost'"

**Solusi:**
1. Pastikan password MySQL benar
2. Atau buat user baru:

```sql
CREATE USER 'restaurant_user'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON restaurant_db.* TO 'restaurant_user'@'localhost';
FLUSH PRIVILEGES;
```

Kemudian gunakan kredensial:
- User: restaurant_user
- Password: password123

### Error: "Can't connect to MySQL server"

**Solusi:**
1. Pastikan MySQL/MariaDB service running:

```powershell
# Cek status MySQL
Get-Service -Name MySQL*

# Start service jika tidak running
Start-Service -Name MySQL80  # Sesuaikan dengan nama service Anda
```

2. Atau via XAMPP/WAMP Control Panel, start MySQL service

### Error: "Unknown database 'restaurant_db'"

**Solusi:**
```sql
CREATE DATABASE restaurant_db;
```

### Error: Python tidak ditemukan

**Solusi:**
1. Install Python dari https://www.python.org/downloads/
2. Centang "Add Python to PATH" saat instalasi
3. Restart PowerShell/Command Prompt

## Konfigurasi Tambahan

### Mengubah Port MySQL (Jika Berbeda)

Edit file `database/db_manager.py`:

```python
def __init__(self, host='localhost', database='restaurant_db', 
             user='root', password='', port=3306):  # Tambahkan parameter port
```

### Menggunakan Environment Variables (Recommended untuk Production)

Buat file `.env`:
```
DB_HOST=localhost
DB_DATABASE=restaurant_db
DB_USER=root
DB_PASSWORD=your_password
```

Install python-dotenv:
```powershell
pip install python-dotenv
```

## Testing

### Menjalankan Semua Tests

```powershell
python -m tests.test_models
```

### Menjalankan Test Spesifik

```powershell
# Test pelanggan saja
python -m unittest tests.test_models.TestPelanggan

# Test dengan verbose
python -m unittest tests.test_models -v
```

## Uninstall

### Hapus Database

```sql
DROP DATABASE restaurant_db;
```

### Hapus Python Packages

```powershell
pip uninstall mysql-connector-python -y
```

### Hapus Project

```powershell
Remove-Item -Path "d:\Coding\restaurant-system-management" -Recurse -Force
```

## Bantuan Lebih Lanjut

Jika mengalami masalah yang tidak tercantum di sini:

1. Periksa error message dengan teliti
2. Cek dokumentasi di `DOKUMENTASI.md`
3. Pastikan semua prerequisites terpenuhi
4. Restart terminal/PowerShell setelah instalasi

---

**Selamat! Sistem siap digunakan!** 🎉
