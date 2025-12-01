# CHEATSHEET - Quick Reference
## Sistem Pemesanan Restoran

### 🚀 Quick Commands

```powershell
# Install dependencies
pip install -r requirements.txt

# Jalankan aplikasi
python main.py

# Jalankan demo
python demo.py

# Jalankan tests
python -m tests.test_models

# Jalankan test dengan verbose
python -m unittest tests.test_models -v
```

### 📦 Import Statements

```python
# Import models
from models.pelanggan import Pelanggan
from models.meja import Meja
from models.pemesanan import Pemesanan
from models.base_entity import BaseEntity

# Import database
from database.db_manager import DatabaseManager

# Import services
from services.restaurant_service import (
    init_database,
    tambah_pelanggan, lihat_pelanggan, update_pelanggan, hapus_pelanggan,
    tambah_meja, lihat_meja, update_meja, hapus_meja,
    tambah_pemesanan, konfirmasi_pemesanan, selesaikan_pemesanan,
    generate_laporan_pemesanan, print_laporan
)
```

### 🔧 Database Setup

```sql
-- Buat database
CREATE DATABASE restaurant_db;

-- Gunakan database
USE restaurant_db;

-- Jalankan setup script
SOURCE d:/Coding/restaurant-system-management/database/setup.sql;
```

### 💻 Code Examples

#### Inisialisasi Database
```python
from services.restaurant_service import init_database

db_config = {
    'host': 'localhost',
    'database': 'restaurant_db',
    'user': 'root',
    'password': 'your_password'
}

db = init_database(db_config)
```

#### CRUD Pelanggan
```python
# Create
pelanggan_id = tambah_pelanggan(db, "John Doe", "081234567890", "john@example.com")

# Read
pelanggan_list = lihat_pelanggan(db)  # Semua
pelanggan = lihat_pelanggan(db, pelanggan_id)  # Spesifik

# Update
update_pelanggan(db, pelanggan_id, "John Updated", "082345678901", "new@example.com")

# Delete
hapus_pelanggan(db, pelanggan_id)
```

#### CRUD Meja
```python
# Create
meja_id = tambah_meja(db, nomor_meja=5, kapasitas=4, status='tersedia')

# Read
meja_list = lihat_meja(db)  # Semua
meja_tersedia = lihat_meja(db, status='tersedia')  # Filter status

# Update
update_meja(db, meja_id, nomor_meja=5, kapasitas=6, status='terisi')

# Delete
hapus_meja(db, meja_id)
```

#### CRUD Pemesanan
```python
from datetime import datetime

# Create
tanggal = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
pemesanan_id = tambah_pemesanan(
    db, 
    pelanggan_id=1, 
    meja_id=1, 
    tanggal_pemesanan=tanggal,
    jumlah_orang=4,
    catatan="Dekat jendela"
)

# Read
pemesanan_list = lihat_pemesanan(db)  # Semua
pemesanan_pending = lihat_pemesanan(db, status='pending')  # Filter

# Update Status
konfirmasi_pemesanan(db, pemesanan_id)  # pending → confirmed
selesaikan_pemesanan(db, pemesanan_id)  # confirmed → completed
batalkan_pemesanan(db, pemesanan_id)   # any → cancelled

# Delete
hapus_pemesanan(db, pemesanan_id)
```

#### Generate Laporan
```python
# Laporan semua
laporan = generate_laporan_pemesanan(db)

# Laporan by status
laporan = generate_laporan_pemesanan(db, status='confirmed')

# Laporan by tanggal
laporan = generate_laporan_pemesanan(
    db,
    tanggal_mulai='2025-12-01',
    tanggal_akhir='2025-12-31'
)

# Print laporan
print_laporan(laporan)
```

#### Menggunakan OOP Models
```python
# Create objects
pelanggan = Pelanggan(id=1, nama="Alice", telepon="081111111111", email="alice@test.com")
meja = Meja(id=1, nomor_meja=5, kapasitas=4, status='tersedia')
pemesanan = Pemesanan(id=1, pelanggan_id=1, meja_id=1, jumlah_orang=4)

# Validasi
is_valid, error = pelanggan.validate_data()
if is_valid:
    print("Data valid")
else:
    print(f"Error: {error}")

# Display info (polymorphism)
print(pelanggan.display_info())
print(meja.display_info())
print(pemesanan.display_info())

# Getter/Setter
nama = pelanggan.get_nama()
pelanggan.set_nama("New Name")

# Status operations
if meja.is_tersedia():
    meja.set_status(Meja.STATUS_RESERVED)

pemesanan.update_status(Pemesanan.STATUS_CONFIRMED)
```

### 📊 Status Values

#### Meja Status
- `tersedia` - Meja kosong dan bisa dipesan
- `reserved` - Meja sudah dipesan tapi belum ditempati
- `terisi` - Meja sedang ditempati pelanggan

#### Pemesanan Status
- `pending` - Pemesanan baru, menunggu konfirmasi
- `confirmed` - Pemesanan dikonfirmasi, pelanggan sudah datang
- `completed` - Pemesanan selesai, meja dibebaskan
- `cancelled` - Pemesanan dibatalkan

### 🔄 Alur Status Pemesanan

```
1. Buat Pemesanan
   pemesanan: pending
   meja: reserved

2. Konfirmasi Pemesanan
   pemesanan: confirmed
   meja: terisi

3. Selesaikan Pemesanan
   pemesanan: completed
   meja: tersedia
```

### 🧪 Unit Testing

```python
# Jalankan semua tests
python -m tests.test_models

# Jalankan test class spesifik
python -m unittest tests.test_models.TestPelanggan

# Jalankan single test
python -m unittest tests.test_models.TestPelanggan.test_create_pelanggan

# Verbose mode
python -m unittest tests.test_models -v
```

### 📁 File Locations

```
models/
  - base_entity.py      # Kelas dasar
  - pelanggan.py        # Kelas Pelanggan
  - meja.py             # Kelas Meja
  - pemesanan.py        # Kelas Pemesanan

database/
  - db_manager.py       # Database operations
  - setup.sql           # SQL script

services/
  - restaurant_service.py  # Business logic

tests/
  - test_models.py      # Unit tests

main.py                 # Aplikasi utama
demo.py                 # Demo script
```

### 🐛 Common Issues & Solutions

#### "ModuleNotFoundError: No module named 'mysql'"
```powershell
pip install mysql-connector-python
```

#### "Access denied for user"
- Periksa username dan password MySQL
- Pastikan user punya akses ke database

#### "Can't connect to MySQL server"
```powershell
# Windows - Start MySQL service
Start-Service -Name MySQL80

# Atau via XAMPP/WAMP control panel
```

#### "Unknown database 'restaurant_db'"
```sql
CREATE DATABASE restaurant_db;
```

### 📝 SQL Queries

```sql
-- Lihat semua data
SELECT * FROM pelanggan;
SELECT * FROM meja;
SELECT * FROM pemesanan;

-- Join tables
SELECT p.*, pel.nama, m.nomor_meja 
FROM pemesanan p
JOIN pelanggan pel ON p.pelanggan_id = pel.id
JOIN meja m ON p.meja_id = m.id;

-- Filter
SELECT * FROM meja WHERE status = 'tersedia';
SELECT * FROM pemesanan WHERE status = 'pending';

-- Statistik
SELECT status, COUNT(*) as total 
FROM pemesanan 
GROUP BY status;
```

### 🎯 Keyboard Shortcuts (dalam aplikasi)

- `1-5` - Pilih menu
- `0` - Kembali/Keluar
- `Enter` - Konfirmasi
- `Ctrl+C` - Force quit

### 📚 Documentation Files

- `README.md` - Panduan utama
- `DOKUMENTASI.md` - Dokumentasi teknis lengkap
- `INSTALL.md` - Panduan instalasi
- `RINGKASAN.md` - Ringkasan project
- `CHEATSHEET.md` - Quick reference (this file)

### 💡 Tips

1. **Selalu validasi data** sebelum insert ke database
2. **Gunakan try-except** untuk error handling
3. **Close connection** setelah selesai
4. **Backup database** secara berkala
5. **Test dulu** sebelum demo

---

**Quick Help**
- Dokumentasi: Baca README.md
- Issues: Cek INSTALL.md troubleshooting
- Testing: python -m tests.test_models
- Demo: python demo.py

**Good luck dengan demonstrasi!** 🚀
