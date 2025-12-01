# Script SQL untuk Setup Database Restaurant Management System

# 1. Buat database baru
CREATE DATABASE IF NOT EXISTS restaurant_db;

# 2. Gunakan database
USE restaurant_db;

# 3. Buat tabel pelanggan
CREATE TABLE IF NOT EXISTS pelanggan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    telepon VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_nama (nama),
    INDEX idx_telepon (telepon)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

# 4. Buat tabel meja
CREATE TABLE IF NOT EXISTS meja (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nomor_meja INT NOT NULL UNIQUE,
    kapasitas INT NOT NULL,
    status ENUM('tersedia', 'terisi', 'reserved') DEFAULT 'tersedia',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_status (status),
    INDEX idx_nomor_meja (nomor_meja)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

# 5. Buat tabel pemesanan
CREATE TABLE IF NOT EXISTS pemesanan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pelanggan_id INT NOT NULL,
    meja_id INT NOT NULL,
    tanggal_pemesanan DATETIME NOT NULL,
    jumlah_orang INT NOT NULL,
    status ENUM('pending', 'confirmed', 'completed', 'cancelled') DEFAULT 'pending',
    catatan TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (pelanggan_id) REFERENCES pelanggan(id) ON DELETE CASCADE,
    FOREIGN KEY (meja_id) REFERENCES meja(id) ON DELETE CASCADE,
    INDEX idx_status (status),
    INDEX idx_tanggal (tanggal_pemesanan),
    INDEX idx_pelanggan (pelanggan_id),
    INDEX idx_meja (meja_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

# 6. Insert data sample untuk testing (opsional)

-- Sample pelanggan
INSERT INTO pelanggan (nama, telepon, email) VALUES 
('John Doe', '081234567890', 'john@example.com'),
('Jane Smith', '082345678901', 'jane@example.com'),
('Bob Johnson', '083456789012', 'bob@example.com');

-- Sample meja
INSERT INTO meja (nomor_meja, kapasitas, status) VALUES 
(1, 2, 'tersedia'),
(2, 4, 'tersedia'),
(3, 4, 'tersedia'),
(4, 6, 'tersedia'),
(5, 8, 'tersedia'),
(6, 2, 'tersedia');

-- Sample pemesanan
INSERT INTO pemesanan (pelanggan_id, meja_id, tanggal_pemesanan, jumlah_orang, status, catatan) VALUES 
(1, 2, '2025-12-01 19:00:00', 4, 'confirmed', 'Dekat jendela'),
(2, 4, '2025-12-01 20:00:00', 6, 'pending', 'Ulang tahun'),
(3, 1, '2025-12-02 18:00:00', 2, 'confirmed', '');

# 7. Verifikasi data
SELECT 'Pelanggan:' as Info;
SELECT * FROM pelanggan;

SELECT 'Meja:' as Info;
SELECT * FROM meja;

SELECT 'Pemesanan:' as Info;
SELECT p.*, pel.nama as nama_pelanggan, m.nomor_meja 
FROM pemesanan p
JOIN pelanggan pel ON p.pelanggan_id = pel.id
JOIN meja m ON p.meja_id = m.id;

# 8. Query utility

-- Lihat meja tersedia
SELECT * FROM meja WHERE status = 'tersedia';

-- Lihat pemesanan hari ini
SELECT p.*, pel.nama as nama_pelanggan, pel.telepon, m.nomor_meja 
FROM pemesanan p
JOIN pelanggan pel ON p.pelanggan_id = pel.id
JOIN meja m ON p.meja_id = m.id
WHERE DATE(p.tanggal_pemesanan) = CURDATE();

-- Statistik pemesanan
SELECT 
    status,
    COUNT(*) as jumlah,
    SUM(jumlah_orang) as total_orang
FROM pemesanan
GROUP BY status;
