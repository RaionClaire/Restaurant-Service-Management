# Aturan Validasi Input - Sistem Pemesanan Restoran

## 📋 Daftar Isi
1. [Validasi Pelanggan](#validasi-pelanggan)
2. [Validasi Meja](#validasi-meja)
3. [Validasi Pemesanan](#validasi-pemesanan)
4. [Contoh Input yang Valid](#contoh-input-yang-valid)
5. [Contoh Input yang Tidak Valid](#contoh-input-yang-tidak-valid)

---

## 👤 Validasi Pelanggan

### Nama Pelanggan
✅ **Aturan:**
- Tidak boleh kosong
- Minimal 2 karakter
- Tidak boleh mengandung angka (0-9)
- Boleh mengandung spasi dan karakter khusus (-, ', dll)

❌ **Contoh yang SALAH:**
- `""` (kosong)
- `"A"` (kurang dari 2 karakter)
- `"John123"` (mengandung angka)
- `"Budi007"` (mengandung angka)

✅ **Contoh yang BENAR:**
- `"John Doe"`
- `"Ahmad"`
- `"Siti Nurhaliza"`
- `"O'Brien"`
- `"Jean-Pierre"`

### Nomor Telepon
✅ **Aturan:**
- Tidak boleh kosong
- Harus dimulai dengan salah satu:
  - `628` (format Indonesia internasional tanpa +)
  - `08` (format lokal Indonesia)
  - `+628` (format Indonesia internasional dengan +)
- Hanya boleh berisi angka (dan tanda + di awal)
- Panjang: 10-15 digit (tidak termasuk +)
- Boleh mengandung spasi, tanda hubung, atau tanda kurung (akan dihapus saat validasi)

❌ **Contoh yang SALAH:**
- `""` (kosong)
- `"123456"` (tidak dimulai dengan 628/08/+628)
- `"081234"` (kurang dari 10 digit)
- `"08123456789012345"` (lebih dari 15 digit)
- `"62-812-abcd-efgh"` (mengandung huruf)
- `"+1234567890"` (kode negara salah)

✅ **Contoh yang BENAR:**
- `"081234567890"`
- `"628123456789"`
- `"+6281234567890"`
- `"0812-3456-7890"` (spasi/tanda hubung akan dihapus)
- `"0812 3456 7890"` (spasi akan dihapus)
- `"+62 812 3456 7890"` (akan divalidasi tanpa spasi)

### Email
✅ **Aturan:**
- Boleh kosong (opsional)
- Jika diisi, harus memenuhi:
  - Harus mengandung karakter `@`
  - Harus mengandung karakter `.` (titik)
  - Format umum: `nama@domain.com`
  - Hanya boleh ada satu karakter `@`
  - `@` tidak boleh di awal atau akhir
  - Setelah `@` harus ada titik untuk domain

❌ **Contoh yang SALAH:**
- `"email"` (tidak ada @ dan .)
- `"email@"` (tidak ada domain)
- `"@domain.com"` (tidak ada nama)
- `"email@@domain.com"` (lebih dari satu @)
- `"email@domain"` (tidak ada titik di domain)
- `"email.domain.com"` (tidak ada @)

✅ **Contoh yang BENAR:**
- `""` (kosong, karena opsional)
- `"john@example.com"`
- `"user.name@domain.com"`
- `"email123@subdomain.domain.com"`
- `"test_email@company.co.id"`

---

## 🪑 Validasi Meja

### Nomor Meja
✅ **Aturan:**
- Harus lebih dari 0
- Maksimal 999
- Harus berupa bilangan bulat positif
- Harus unik (tidak boleh sama dengan meja lain)

❌ **Contoh yang SALAH:**
- `0` (tidak boleh 0)
- `-5` (tidak boleh negatif)
- `1000` (lebih dari 999)

✅ **Contoh yang BENAR:**
- `1`
- `10`
- `101`
- `999`

### Kapasitas Meja
✅ **Aturan:**
- Harus lebih dari 0
- Maksimal 20 orang
- Harus berupa bilangan bulat positif

❌ **Contoh yang SALAH:**
- `0` (tidak boleh 0)
- `-2` (tidak boleh negatif)
- `25` (lebih dari 20)

✅ **Contoh yang BENAR:**
- `2` (meja untuk 2 orang)
- `4` (meja untuk 4 orang)
- `6` (meja untuk 6 orang)
- `20` (meja besar untuk 20 orang)

### Status Meja
✅ **Aturan:**
- Harus salah satu dari:
  - `tersedia` - Meja siap untuk dipesan
  - `terisi` - Meja sedang digunakan
  - `reserved` - Meja sudah direservasi

❌ **Contoh yang SALAH:**
- `"available"` (gunakan bahasa Indonesia)
- `"kosong"` (gunakan "tersedia")
- `"penuh"` (gunakan "terisi")

✅ **Contoh yang BENAR:**
- `"tersedia"`
- `"terisi"`
- `"reserved"`

---

## 📝 Validasi Pemesanan

### ID Pelanggan
✅ **Aturan:**
- Tidak boleh kosong
- Harus bilangan bulat positif (> 0)
- Harus sudah terdaftar di database

❌ **Contoh yang SALAH:**
- `0` (tidak valid)
- `-1` (negatif)
- ID yang tidak ada di database

✅ **Contoh yang BENAR:**
- `1`, `2`, `3`, dst (ID yang valid dan terdaftar)

### ID Meja
✅ **Aturan:**
- Tidak boleh kosong
- Harus bilangan bulat positif (> 0)
- Harus sudah terdaftar di database
- Meja harus dalam status "tersedia"

❌ **Contoh yang SALAH:**
- `0` (tidak valid)
- `-1` (negatif)
- ID meja yang sudah terisi/reserved

✅ **Contoh yang BENAR:**
- `1`, `2`, `3`, dst (ID meja yang valid dan tersedia)

### Tanggal Pemesanan
✅ **Aturan:**
- Format: `YYYY-MM-DD HH:MM:SS`
- Tahun: 4 digit
- Bulan: 01-12
- Tanggal: 01-31 (sesuai bulan)
- Jam: 00-23
- Menit: 00-59
- Detik: 00-59

❌ **Contoh yang SALAH:**
- `"2025/12/25 19:00:00"` (gunakan - bukan /)
- `"25-12-2025 19:00:00"` (urutan salah)
- `"2025-12-25"` (tidak ada waktu)
- `"2025-12-25 7:00:00"` (jam harus 2 digit: 07)
- `"2025-13-01 19:00:00"` (bulan tidak valid)

✅ **Contoh yang BENAR:**
- `"2025-12-25 19:00:00"`
- `"2025-01-15 12:30:00"`
- `"2025-12-31 23:59:59"`

### Jumlah Orang
✅ **Aturan:**
- Harus lebih dari 0
- Maksimal 20 orang
- Tidak boleh melebihi kapasitas meja yang dipilih

❌ **Contoh yang SALAH:**
- `0` (tidak valid)
- `-1` (negatif)
- `25` (lebih dari 20)
- `10` (jika kapasitas meja hanya 4)

✅ **Contoh yang BENAR:**
- `1` (untuk 1 orang)
- `4` (untuk 4 orang)
- `10` (jika kapasitas meja >= 10)

### Catatan
✅ **Aturan:**
- Opsional (boleh kosong)
- Maksimal 500 karakter
- Boleh berisi huruf, angka, dan karakter khusus

❌ **Contoh yang SALAH:**
- Teks lebih dari 500 karakter

✅ **Contoh yang BENAR:**
- `""` (kosong)
- `"Dekat jendela"`
- `"Perlu high chair untuk anak"`
- `"Ulang tahun, tolong siapkan kue"`

### Status Pemesanan
✅ **Aturan:**
- Harus salah satu dari:
  - `pending` - Menunggu konfirmasi
  - `confirmed` - Sudah dikonfirmasi
  - `completed` - Sudah selesai
  - `cancelled` - Dibatalkan

---

## ✅ Contoh Input yang Valid

### Menambah Pelanggan
```
Nama: Siti Nurhaliza
Telepon: 081234567890
Email: siti@example.com
```

```
Nama: Ahmad Dhani
Telepon: +6285678901234
Email: ahmad.dhani@mail.co.id
```

```
Nama: John O'Brien
Telepon: 0812-3456-7890
Email: 
```

### Menambah Meja
```
Nomor Meja: 5
Kapasitas: 4
Status: tersedia
```

```
Nomor Meja: 101
Kapasitas: 8
Status: tersedia
```

### Membuat Pemesanan
```
ID Pelanggan: 1
ID Meja: 3
Tanggal: 2025-12-25 19:00:00
Jumlah Orang: 4
Catatan: Dekat jendela
```

```
ID Pelanggan: 2
ID Meja: 5
Tanggal: (kosongkan untuk hari ini)
Jumlah Orang: 2
Catatan: 
```

---

## ❌ Contoh Input yang Tidak Valid

### Pelanggan - AKAN DITOLAK
```
❌ Nama: John123
   Error: Nama pelanggan tidak boleh mengandung angka

❌ Nama: A
   Error: Nama pelanggan minimal 2 karakter

❌ Telepon: 123456789
   Error: Nomor telepon harus dimulai dengan 628, 08, atau +628

❌ Telepon: 081234
   Error: Nomor telepon harus antara 10-15 digit

❌ Email: emaildomain.com
   Error: Email harus mengandung karakter @ dan . (titik)

❌ Email: user@@domain.com
   Error: Email hanya boleh mengandung satu karakter @
```

### Meja - AKAN DITOLAK
```
❌ Nomor Meja: 0
   Error: Nomor meja harus lebih dari 0

❌ Nomor Meja: 1000
   Error: Nomor meja tidak boleh lebih dari 999

❌ Kapasitas: 0
   Error: Kapasitas harus lebih dari 0

❌ Kapasitas: 25
   Error: Kapasitas meja tidak boleh lebih dari 20 orang

❌ Status: available
   Error: Status harus salah satu dari: tersedia, terisi, reserved
```

### Pemesanan - AKAN DITOLAK
```
❌ Jumlah Orang: 0
   Error: Jumlah orang harus lebih dari 0

❌ Jumlah Orang: 25
   Error: Jumlah orang tidak boleh lebih dari 20

❌ Tanggal: 2025/12/25 19:00:00
   Error: Format tanggal tidak valid (gunakan: YYYY-MM-DD HH:MM:SS)

❌ Catatan: [Teks lebih dari 500 karakter...]
   Error: Catatan tidak boleh lebih dari 500 karakter
```

---

## 🔍 Tips Penggunaan

1. **Nama Pelanggan**: Gunakan nama asli tanpa angka
2. **Nomor Telepon**: Pastikan menggunakan format Indonesia yang benar
3. **Email**: Periksa ada @ dan titik sebelum submit
4. **Nomor Meja**: Gunakan angka yang wajar (1-999)
5. **Kapasitas**: Sesuaikan dengan ukuran meja yang realistis
6. **Tanggal**: Ikuti format YYYY-MM-DD HH:MM:SS dengan tepat
7. **Jumlah Orang**: Pastikan tidak melebihi kapasitas meja

---

## 🛠️ Troubleshooting

**Q: Mengapa nomor telepon saya ditolak?**
A: Pastikan nomor dimulai dengan 628, 08, atau +628 dan memiliki 10-15 digit.

**Q: Email saya valid tapi ditolak?**
A: Periksa apakah email mengandung @ dan titik (.) di posisi yang benar.

**Q: Nama dengan apostrof (') ditolak?**
A: Nama dengan apostrof seharusnya diterima. Pastikan tidak ada angka dalam nama.

**Q: Tanggal pemesanan terus error?**
A: Gunakan format YYYY-MM-DD HH:MM:SS (contoh: 2025-12-25 19:00:00) dengan lengkap.

**Q: Kapasitas meja saya wajar tapi ditolak?**
A: Maksimal kapasitas adalah 20 orang. Jika butuh lebih, gunakan beberapa meja.

---

**Terakhir diupdate:** Desember 2025
