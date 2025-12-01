"""
Demo Script - Quick Test untuk Sistem Pemesanan Restoran
Script ini untuk testing cepat tanpa perlu menjalankan aplikasi lengkap.
"""

from database.db_manager import DatabaseManager
from services.restaurant_service import *
from models.pelanggan import Pelanggan
from models.meja import Meja
from models.pemesanan import Pemesanan


def demo_oop_concepts():
    """Demo konsep OOP: Inheritance dan Polymorphism"""
    print("\n" + "="*60)
    print("DEMO 1: KONSEP OOP (INHERITANCE & POLYMORPHISM)")
    print("="*60)
    
    # Buat objek dari berbagai kelas
    pelanggan = Pelanggan(id=1, nama="Alice", telepon="081234567890", email="alice@example.com")
    meja = Meja(id=1, nomor_meja=5, kapasitas=4, status='tersedia')
    pemesanan = Pemesanan(id=1, pelanggan_id=1, meja_id=1, jumlah_orang=4)
    
    # Demonstrasi Inheritance
    print("\n--- INHERITANCE (Semua kelas mewarisi BaseEntity) ---")
    from models.base_entity import BaseEntity
    
    print(f"Pelanggan adalah instance dari BaseEntity: {isinstance(pelanggan, BaseEntity)}")
    print(f"Meja adalah instance dari BaseEntity: {isinstance(meja, BaseEntity)}")
    print(f"Pemesanan adalah instance dari BaseEntity: {isinstance(pemesanan, BaseEntity)}")
    
    # Demonstrasi Polymorphism
    print("\n--- POLYMORPHISM (Method display_info berbeda per kelas) ---")
    entities = [pelanggan, meja, pemesanan]
    
    for entity in entities:
        print(f"\n{entity.__class__.__name__}:")
        print(entity.display_info())
    
    # Demonstrasi Validasi
    print("\n--- VALIDASI DATA ---")
    is_valid, error = pelanggan.validate_data()
    print(f"Pelanggan valid: {is_valid}")
    
    # Pelanggan invalid
    pelanggan_invalid = Pelanggan(nama="", telepon="")
    is_valid, error = pelanggan_invalid.validate_data()
    print(f"Pelanggan invalid: {is_valid}, Error: {error}")


def demo_structured_programming():
    """Demo pemrograman terstruktur dengan fungsi-fungsi"""
    print("\n" + "="*60)
    print("DEMO 2: PEMROGRAMAN TERSTRUKTUR")
    print("="*60)
    
    print("\nDemonstrasi fungsi-fungsi modular:")
    print("✓ init_database() - Inisialisasi database")
    print("✓ tambah_pelanggan() - Menambah pelanggan")
    print("✓ tambah_meja() - Menambah meja")
    print("✓ tambah_pemesanan() - Menambah pemesanan")
    print("✓ konfirmasi_pemesanan() - Konfirmasi pemesanan")
    print("✓ selesaikan_pemesanan() - Selesaikan pemesanan")
    print("✓ generate_laporan_pemesanan() - Generate laporan")
    
    print("\nSetiap fungsi memiliki:")
    print("- Parameter yang jelas")
    print("- Return value yang terdefinisi")
    print("- Validasi input")
    print("- Error handling")
    print("- Dokumentasi lengkap")


def demo_database_crud(db):
    """Demo operasi CRUD database"""
    print("\n" + "="*60)
    print("DEMO 3: OPERASI DATABASE (CRUD)")
    print("="*60)
    
    # CREATE
    print("\n--- CREATE ---")
    pelanggan_id = tambah_pelanggan(db, "Demo User", "081111111111", "demo@test.com")
    meja_id = tambah_meja(db, 99, 4, 'tersedia')
    
    # READ
    print("\n--- READ ---")
    pelanggan_list = lihat_pelanggan(db, pelanggan_id)
    if pelanggan_list:
        print(f"Data Pelanggan: {pelanggan_list[0]['nama']}")
    
    meja_list = lihat_meja(db, meja_id)
    if meja_list:
        print(f"Data Meja: Nomor {meja_list[0]['nomor_meja']}, Kapasitas {meja_list[0]['kapasitas']}")
    
    # UPDATE
    print("\n--- UPDATE ---")
    update_pelanggan(db, pelanggan_id, "Demo User Updated", "082222222222", "updated@test.com")
    
    # READ lagi untuk verifikasi update
    pelanggan_list = lihat_pelanggan(db, pelanggan_id)
    if pelanggan_list:
        print(f"Data Pelanggan Setelah Update: {pelanggan_list[0]['nama']}")
    
    # DELETE
    print("\n--- DELETE ---")
    hapus_pelanggan(db, pelanggan_id)
    hapus_meja(db, meja_id)
    print("Data berhasil dihapus")


def demo_business_logic(db):
    """Demo logika bisnis pemesanan"""
    print("\n" + "="*60)
    print("DEMO 4: ALUR BISNIS PEMESANAN")
    print("="*60)
    
    # Setup data
    print("\n--- SETUP DATA ---")
    pelanggan_id = tambah_pelanggan(db, "Business Demo", "083333333333", "business@test.com")
    meja_id = tambah_meja(db, 88, 4, 'tersedia')
    
    # Buat pemesanan
    print("\n--- BUAT PEMESANAN ---")
    from datetime import datetime
    tanggal = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    pemesanan_id = tambah_pemesanan(db, pelanggan_id, meja_id, tanggal, 4, "Demo pemesanan")
    
    # Cek status meja (harus reserved)
    meja_list = lihat_meja(db, meja_id)
    if meja_list:
        print(f"Status Meja Setelah Pemesanan: {meja_list[0]['status']}")
    
    # Konfirmasi pemesanan
    print("\n--- KONFIRMASI PEMESANAN ---")
    konfirmasi_pemesanan(db, pemesanan_id)
    
    # Cek status meja (harus terisi)
    meja_list = lihat_meja(db, meja_id)
    if meja_list:
        print(f"Status Meja Setelah Konfirmasi: {meja_list[0]['status']}")
    
    # Selesaikan pemesanan
    print("\n--- SELESAIKAN PEMESANAN ---")
    selesaikan_pemesanan(db, pemesanan_id)
    
    # Cek status meja (harus tersedia)
    meja_list = lihat_meja(db, meja_id)
    if meja_list:
        print(f"Status Meja Setelah Selesai: {meja_list[0]['status']}")
    
    # Cleanup
    print("\n--- CLEANUP ---")
    hapus_pemesanan(db, pemesanan_id)
    hapus_pelanggan(db, pelanggan_id)
    hapus_meja(db, meja_id)
    print("Demo selesai, data dibersihkan")


def demo_reporting(db):
    """Demo laporan"""
    print("\n" + "="*60)
    print("DEMO 5: LAPORAN")
    print("="*60)
    
    # Generate laporan
    print("\n--- LAPORAN SEMUA PEMESANAN ---")
    laporan = generate_laporan_pemesanan(db)
    
    if laporan and len(laporan) > 0:
        print_laporan(laporan[:5])  # Tampilkan 5 record pertama
    else:
        print("Tidak ada data pemesanan untuk ditampilkan")


def run_demo():
    """Menjalankan semua demo"""
    print("\n" + "="*70)
    print(" "*15 + "DEMO SISTEM PEMESANAN RESTORAN")
    print("="*70)
    
    # Demo 1: OOP (tidak perlu database)
    demo_oop_concepts()
    
    # Demo 2: Structured Programming (tidak perlu database)
    demo_structured_programming()
    
    # Demo 3-5 memerlukan koneksi database
    print("\n" + "="*60)
    print("KONEKSI DATABASE")
    print("="*60)
    
    print("\nMasukkan kredensial database untuk melanjutkan demo:")
    host = input("Host (default: localhost): ").strip() or 'localhost'
    database = input("Database (default: restaurant_db): ").strip() or 'restaurant_db'
    user = input("User (default: root): ").strip() or 'root'
    password = input("Password: ").strip()
    
    db_config = {
        'host': host,
        'database': database,
        'user': user,
        'password': password
    }
    
    db = init_database(db_config)
    
    if db:
        try:
            # Demo dengan database
            demo_database_crud(db)
            demo_business_logic(db)
            demo_reporting(db)
            
            print("\n" + "="*70)
            print(" "*20 + "DEMO SELESAI!")
            print("="*70)
            print("\nUntuk menggunakan aplikasi lengkap, jalankan: python main.py")
            print("Untuk menjalankan unit tests, jalankan: python -m tests.test_models")
            
        finally:
            db.disconnect()
    else:
        print("\n✗ Tidak dapat terhubung ke database")
        print("Demo yang memerlukan database dilewati")
        print("\nPastikan:")
        print("1. MySQL/MariaDB sudah running")
        print("2. Database 'restaurant_db' sudah dibuat")
        print("3. Kredensial database benar")


if __name__ == '__main__':
    run_demo()
