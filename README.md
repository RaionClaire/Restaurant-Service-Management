# Sistem Pemesanan Restoran

Aplikasi sederhana untuk mengelola pemesanan meja restoran menggunakan Python dengan prinsip pemrograman terstruktur dan berorientasi objek.

## 📋 Deskripsi

Sistem ini memungkinkan pengguna untuk:
- Mengelola data pelanggan
- Mengelola meja restoran
- Membuat dan mengelola pemesanan meja
- Menghasilkan laporan pemesanan
- Melakukan pengujian unit otomatis

## 🎯 Fitur Utama

### 1. Kelola Pelanggan
- Tambah pelanggan baru
- Lihat daftar pelanggan
- Cari pelanggan berdasarkan ID
- Update data pelanggan
- Hapus pelanggan

### 2. Kelola Meja
- Tambah meja baru
- Lihat semua meja
- Lihat meja yang tersedia
- Update data meja
- Hapus meja

### 3. Kelola Pemesanan
- Buat pemesanan baru
- Lihat semua pemesanan
- Filter pemesanan berdasarkan status
- Konfirmasi pemesanan
- Selesaikan pemesanan
- Batalkan pemesanan
- Hapus pemesanan

### 4. Laporan
- Laporan semua pemesanan
- Laporan berdasarkan status (pending, confirmed, completed, cancelled)
- Laporan berdasarkan rentang tanggal

### 5. Unit Testing
- Pengujian otomatis untuk semua kelas dan fungsi
- Validasi inheritance dan polymorphism

## 🏗️ Struktur Project

```
restaurant-system-management/
├── models/                      # Model OOP
│   ├── __init__.py
│   ├── base_entity.py          # Kelas dasar (inheritance)
│   ├── pelanggan.py            # Kelas Pelanggan
│   ├── meja.py                 # Kelas Meja
│   └── pemesanan.py            # Kelas Pemesanan
├── database/                    # Database layer
│   ├── __init__.py
│   └── db_manager.py           # Manager database & CRUD
├── services/                    # Business logic (pemrograman terstruktur)
│   ├── __init__.py
│   └── restaurant_service.py   # Fungsi-fungsi layanan
├── tests/                       # Unit tests
│   ├── __init__.py
│   └── test_models.py          # Pengujian unit
├── main.py                      # Aplikasi utama
├── README.md                    # Dokumentasi ini
├── requirements.txt             # Dependencies
└── DOKUMENTASI.md              # Dokumentasi lengkap
```

## 🔧 Teknologi yang Digunakan

- **Python 3.8+**: Bahasa pemrograman utama
- **MySQL/MariaDB**: Database server
- **mysql-connector-python**: Library koneksi database
- **unittest**: Framework pengujian unit

## 📦 Instalasi

### 1. Prasyarat
- Python 3.8 atau lebih tinggi
- MySQL atau MariaDB server
- pip (Python package manager)

### 2. Clone atau Download Project
```powershell
# Jika menggunakan git
git clone <repository-url>
cd restaurant-system-management

# Atau download dan extract ZIP
```

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 4. Setup Database
```sql
-- Buat database baru
CREATE DATABASE restaurant_db;

-- Gunakan database
USE restaurant_db;

-- Tabel akan dibuat otomatis saat aplikasi pertama kali dijalankan
```

## 🚀 Cara Menjalankan

### Menjalankan Aplikasi Utama
```powershell
python main.py
```

Saat pertama kali dijalankan, Anda akan diminta memasukkan kredensial database:
- Host (default: localhost)
- Database (default: restaurant_db)
- User (default: root)
- Password

### Menjalankan Unit Tests
```powershell
# Melalui aplikasi (menu utama pilih 5)
python main.py

# Atau langsung menjalankan test file
python -m tests.test_models
```

## 📝 Panduan Penggunaan

### 1. Setup Awal
Setelah aplikasi berjalan, lakukan setup awal:
1. Tambah beberapa meja terlebih dahulu (Menu 2)
2. Daftarkan pelanggan (Menu 1)
3. Buat pemesanan (Menu 3)

**⚠️ PENTING:** Baca [Aturan Validasi Input](VALIDASI.md) untuk mengetahui format input yang benar!

### 2. Alur Pemesanan Normal
1. **Pelanggan mendaftar** → Menu Kelola Pelanggan → Tambah Pelanggan
2. **Lihat meja tersedia** → Menu Kelola Meja → Lihat Meja Tersedia
3. **Buat pemesanan** → Menu Kelola Pemesanan → Buat Pemesanan Baru
   - Status otomatis: `pending`
   - Meja otomatis: `reserved`
4. **Konfirmasi pemesanan** → Menu Kelola Pemesanan → Konfirmasi Pemesanan
   - Status berubah: `confirmed`
   - Meja berubah: `terisi`
5. **Selesaikan pemesanan** → Menu Kelola Pemesanan → Selesaikan Pemesanan
   - Status berubah: `completed`
   - Meja berubah: `tersedia` (meja dibebaskan)

### 3. Membuat Laporan
- Menu Laporan → Pilih jenis laporan
- Laporan akan ditampilkan dalam format tabel yang rapi

## 🧪 Pengujian

Sistem dilengkapi dengan comprehensive unit tests yang mencakup:

### Test Coverage:
- ✅ **Test Pelanggan**: Validasi, getter/setter, display info
- ✅ **Test Meja**: Status meja, kapasitas, validasi
- ✅ **Test Pemesanan**: Validasi, update status, tanggal otomatis
- ✅ **Test Inheritance**: Memastikan semua kelas mewarisi BaseEntity
- ✅ **Test Polymorphism**: Memastikan display_info berbeda per kelas

### Menjalankan Tests:
```powershell
# Semua tests dengan verbose
python -m tests.test_models

# Atau melalui unittest
python -m unittest tests.test_models -v
```

### Hasil Test yang Diharapkan:
```
Test Pelanggan: 6 tests ✓
Test Meja: 8 tests ✓
Test Pemesanan: 9 tests ✓
Test Inheritance: 3 tests ✓
Test Polymorphism: 1 test ✓
----------------------------
Total: 27 tests passed
```

## 📊 Schema Database

### Tabel: pelanggan
| Field | Type | Description |
|-------|------|-------------|
| id | INT (PK, AUTO_INCREMENT) | ID pelanggan |
| nama | VARCHAR(100) | Nama pelanggan |
| telepon | VARCHAR(20) | Nomor telepon |
| email | VARCHAR(100) | Email (opsional) |
| created_at | TIMESTAMP | Waktu pembuatan |

### Tabel: meja
| Field | Type | Description |
|-------|------|-------------|
| id | INT (PK, AUTO_INCREMENT) | ID meja |
| nomor_meja | INT (UNIQUE) | Nomor meja |
| kapasitas | INT | Kapasitas orang |
| status | ENUM | tersedia/terisi/reserved |
| created_at | TIMESTAMP | Waktu pembuatan |

### Tabel: pemesanan
| Field | Type | Description |
|-------|------|-------------|
| id | INT (PK, AUTO_INCREMENT) | ID pemesanan |
| pelanggan_id | INT (FK) | ID pelanggan |
| meja_id | INT (FK) | ID meja |
| tanggal_pemesanan | DATETIME | Tanggal & waktu |
| jumlah_orang | INT | Jumlah orang |
| status | ENUM | pending/confirmed/completed/cancelled |
| catatan | TEXT | Catatan tambahan |
| created_at | TIMESTAMP | Waktu pembuatan |

## 🎓 Prinsip yang Diterapkan

### 1. Coding Guidelines & Best Practices ✅
- Penamaan variabel, fungsi, dan kelas mengikuti PEP 8
- Docstring lengkap untuk semua fungsi dan kelas
- Komentar yang jelas dan ringkas
- Kode terstruktur dan mudah dibaca

### 2. Pemrograman Terstruktur ✅
- Modul terpisah untuk fungsi-fungsi dasar
- Penggunaan tipe data yang sesuai
- Struktur kontrol (percabangan & pengulangan)
- Fungsi-fungsi modular dan reusable

### 3. Pemrograman Berorientasi Objek ✅
- **Inheritance**: BaseEntity → Pelanggan, Meja, Pemesanan
- **Encapsulation**: Atribut private dengan getter/setter
- **Polymorphism**: Method display_info() di-override setiap kelas

### 4. Pre-existing Library ✅
- `mysql-connector-python`: Koneksi database
- `unittest`: Framework testing
- `datetime`: Manipulasi tanggal
- Semua library berlisensi open source

### 5. Akses Basis Data ✅
- Skema database lengkap dengan foreign keys
- Implementasi CRUD untuk semua entitas
- SQL parameterized untuk keamanan
- Koneksi database yang aman

### 6. Dokumentasi ✅
- Docstring untuk setiap kelas dan fungsi
- Parameter dan return value terdokumentasi
- README lengkap dengan panduan
- Komentar inline untuk logika kompleks

### 7. Debugging ✅
- Error handling dengan try-except
- Pesan error yang informatif
- Validasi input di setiap fungsi
- Logging aktivitas penting

### 8. Unit Testing ✅
- Skenario pengujian untuk setiap fungsi
- Test coverage untuk semua modul
- Hasil pengujian terdokumentasi
- Automated testing dengan unittest

## 🔍 Contoh Penggunaan

### Contoh 1: Tambah Pelanggan
```python
from database.db_manager import DatabaseManager
from services.restaurant_service import init_database, tambah_pelanggan

# Inisialisasi database
db = init_database()

# Tambah pelanggan
pelanggan_id = tambah_pelanggan(
    db, 
    nama="John Doe",
    telepon="081234567890",
    email="john@example.com"
)
```

### Contoh 2: Buat Pemesanan
```python
from services.restaurant_service import tambah_pemesanan

# Buat pemesanan
pemesanan_id = tambah_pemesanan(
    db,
    pelanggan_id=1,
    meja_id=1,
    tanggal_pemesanan="2025-12-01 19:00:00",
    jumlah_orang=4,
    catatan="Dekat jendela"
)
```

### Contoh 3: Generate Laporan
```python
from services.restaurant_service import generate_laporan_pemesanan, print_laporan

# Generate dan tampilkan laporan
laporan = generate_laporan_pemesanan(
    db,
    status="confirmed",
    tanggal_mulai="2025-12-01",
    tanggal_akhir="2025-12-31"
)

print_laporan(laporan)
```

## 🐛 Troubleshooting

### Error: "Access denied for user"
**Solusi**: Periksa kredensial database (username, password)

### Error: "Unknown database 'restaurant_db'"
**Solusi**: Buat database terlebih dahulu:
```sql
CREATE DATABASE restaurant_db;
```

### Error: "No module named 'mysql'"
**Solusi**: Install dependencies:
```powershell
pip install mysql-connector-python
```

### Error: "Table doesn't exist"
**Solusi**: Jalankan aplikasi sekali untuk membuat tabel otomatis, atau jalankan manual:
```python
from database.db_manager import DatabaseManager
db = DatabaseManager()
db.connect()
db.create_tables()
```

## 📞 Support

Untuk pertanyaan atau masalah, silakan buat issue di repository atau hubungi developer.

## 📄 Lisensi

Project ini dibuat untuk keperluan praktik demonstrasi dan pembelajaran.

## 👥 Kontributor

- Developer: Restaurant Management System Team
- Tanggal: Desember 2025

---

**Selamat menggunakan Sistem Pemesanan Restoran!** 🍽️
