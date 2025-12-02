"""
Aplikasi Sistem Pemesanan Restoran
Aplikasi untuk mengelola pemesanan meja restoran dengan interface console.

Author: Adinda Salsabila
Date: December 2025
"""

import os
import sys
from datetime import datetime
from services.restaurant_service import *
from database.db_manager import DatabaseManager


class RestaurantApp:
    """
    Kelas utama aplikasi restoran.
    Mengelola user interface dan alur program.
    """
    
    def __init__(self):
        """Inisialisasi aplikasi."""
        self.db = None
        self.running = True
    
    def clear_screen(self):
        """Membersihkan layar console."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def tampilkan_header(self):
        """Menampilkan header aplikasi."""
        print("\n" + "="*60)
        print(" "*10 + "🍽️  SISTEM PEMESANAN RESTORAN  🍽️")
        print("="*60)
    
    def tampilkan_menu_utama(self):
        """Menampilkan menu utama aplikasi."""
        self.clear_screen()
        self.tampilkan_header()
        print("\n📋 MENU UTAMA:")
        print("1. 👤 Kelola Pelanggan")
        print("2. 🪑 Kelola Meja")
        print("3. 📝 Kelola Pemesanan")
        print("4. 📊 Laporan & Analisis")
        print("5. 🧪 Jalankan Unit Tests")
        print("0. 🚪 Keluar")
        print("-"*60)
    
    def tampilkan_menu_pelanggan(self):
        """Menampilkan menu kelola pelanggan."""
        self.clear_screen()
        self.tampilkan_header()
        print("\n👤 KELOLA PELANGGAN:")
        print("1. ➕ Tambah Pelanggan")
        print("2. 📋 Lihat Semua Pelanggan")
        print("3. 🔍 Cari Pelanggan (by ID)")
        print("4. ✏️  Update Pelanggan")
        print("5. 🗑️  Hapus Pelanggan")
        print("0. ⬅️  Kembali")
        print("-"*60)
    
    def tampilkan_menu_meja(self):
        """Menampilkan menu kelola meja."""
        self.clear_screen()
        self.tampilkan_header()
        print("\n🪑 KELOLA MEJA:")
        print("1. ➕ Tambah Meja")
        print("2. 📋 Lihat Semua Meja")
        print("3. ✅ Lihat Meja Tersedia")
        print("4. ✏️  Update Meja")
        print("5. 🗑️  Hapus Meja")
        print("0. ⬅️  Kembali")
        print("-"*60)
    
    def tampilkan_menu_pemesanan(self):
        """Menampilkan menu kelola pemesanan."""
        self.clear_screen()
        self.tampilkan_header()
        print("\n📝 KELOLA PEMESANAN:")
        print("1. ➕ Buat Pemesanan Baru")
        print("2. 📋 Lihat Semua Pemesanan")
        print("3. 🔍 Lihat Pemesanan (by Status)")
        print("4. ✅ Konfirmasi Pemesanan")
        print("5. 🎉 Selesaikan Pemesanan")
        print("6. ❌ Batalkan Pemesanan")
        print("7. 🗑️  Hapus Pemesanan")
        print("0. ⬅️  Kembali")
        print("-"*60)
    
    def tampilkan_menu_laporan(self):
        """Menampilkan menu laporan."""
        self.clear_screen()
        self.tampilkan_header()
        print("\n📊 LAPORAN & ANALISIS:")
        print("1. 📋 Laporan Semua Pemesanan")
        print("2. 📌 Laporan by Status")
        print("3. 📅 Laporan by Tanggal")
        print("4. 📈 Analisis Statistik Lengkap")
        print("0. ⬅️  Kembali")
        print("-"*60)
    
    # ========== HANDLER PELANGGAN ==========
    
    def handle_tambah_pelanggan(self):
        """Handler untuk menambah pelanggan."""
        print("\n➕ --- TAMBAH PELANGGAN ---")
        print("📋 Aturan Input:")
        print("   • Nama: Tidak boleh mengandung angka, minimal 2 karakter")
        print("   • Telepon: Harus dimulai dengan 628/08/+628, 10-15 digit")
        print("   • Email: Harus mengandung @ dan . (contoh: nama@domain.com)\n")
        
        nama = input("👤 Nama: ").strip()
        telepon = input("📱 Telepon (628xxx/08xxx/+628xxx): ").strip()
        email = input("📧 Email (opsional): ").strip()
        
        tambah_pelanggan(self.db, nama, telepon, email)
        input("\n⏎ Tekan Enter untuk melanjutkan...")
    
    def handle_lihat_pelanggan(self):
        """Handler untuk melihat semua pelanggan."""
        print("\n📋 --- DAFTAR PELANGGAN ---")
        pelanggan_list = lihat_pelanggan(self.db)
        
        if pelanggan_list:
            print(f"\n{'ID':<5} {'👤 Nama':<27} {'📱 Telepon':<17} {'📧 Email':<30}")
            print("-"*79)
            for p in pelanggan_list:
                print(f"{p['id']:<5} {p['nama']:<27} {p['telepon']:<17} {p['email'] or '-':<30}")
        
        input("\n⏎ Tekan Enter untuk melanjutkan...")
    
    def handle_cari_pelanggan(self):
        """Handler untuk mencari pelanggan by ID."""
        print("\n--- CARI PELANGGAN ---")
        try:
            pelanggan_id = int(input("Masukkan ID Pelanggan: "))
            pelanggan_list = lihat_pelanggan(self.db, pelanggan_id)
            
            if pelanggan_list and len(pelanggan_list) > 0:
                p = pelanggan_list[0]
                print(f"\nID: {p['id']}")
                print(f"Nama: {p['nama']}")
                print(f"Telepon: {p['telepon']}")
                print(f"Email: {p['email'] or '-'}")
        except ValueError:
            print("✗ ID harus berupa angka")
        
        input("\nTekan Enter untuk melanjutkan...")
    
    def handle_update_pelanggan(self):
        """Handler untuk update pelanggan."""
        print("\n--- UPDATE PELANGGAN ---")
        print("📋 Aturan Input:")
        print("   • Nama: Tidak boleh mengandung angka, minimal 2 karakter")
        print("   • Telepon: Harus dimulai dengan 628/08/+628, 10-15 digit")
        print("   • Email: Harus mengandung @ dan . (contoh: nama@domain.com)\n")
        
        try:
            pelanggan_id = int(input("Masukkan ID Pelanggan: "))
            nama = input("Nama baru: ").strip()
            telepon = input("Telepon baru (628xxx/08xxx/+628xxx): ").strip()
            email = input("Email baru (opsional): ").strip()
            
            update_pelanggan(self.db, pelanggan_id, nama, telepon, email)
        except ValueError:
            print("✗ ID harus berupa angka")
        
        input("\nTekan Enter untuk melanjutkan...")
    
    def handle_hapus_pelanggan(self):
        """Handler untuk hapus pelanggan."""
        print("\n--- HAPUS PELANGGAN ---")
        try:
            pelanggan_id = int(input("Masukkan ID Pelanggan: "))
            konfirmasi = input(f"Yakin ingin menghapus pelanggan ID {pelanggan_id}? (y/n): ")
            
            if konfirmasi.lower() == 'y':
                hapus_pelanggan(self.db, pelanggan_id)
        except ValueError:
            print("✗ ID harus berupa angka")
        
        input("\nTekan Enter untuk melanjutkan...")
    
    # ========== HANDLER MEJA ==========
    
    def handle_tambah_meja(self):
        """Handler untuk menambah meja."""
        print("\n➕ --- TAMBAH MEJA ---")
        print("📋 Aturan Input:")
        print("   • Nomor Meja: 1-999")
        print("   • Kapasitas: 1-20 orang\n")
        
        try:
            nomor_meja = int(input("🪑 Nomor Meja (1-999): "))
            kapasitas = int(input("👥 Kapasitas (1-20 orang): "))
            print("\n📌 Status: 1) ✅ tersedia, 2) 🔴 terisi, 3) ⏳ reserved")
            status_choice = input("Pilih status (1-3, default 1): ").strip() or "1"
            
            status_map = {'1': 'tersedia', '2': 'terisi', '3': 'reserved'}
            status = status_map.get(status_choice, 'tersedia')
            
            tambah_meja(self.db, nomor_meja, kapasitas, status)
        except ValueError:
            print("✗ Input harus berupa angka")
        
        input("\n⏎ Tekan Enter untuk melanjutkan...")
    
    def handle_lihat_meja(self):
        """Handler untuk melihat semua meja."""
        print("\n📋 --- DAFTAR MEJA ---")
        meja_list = lihat_meja(self.db)
        
        if meja_list:
            status_symbol = {'tersedia': '✅', 'terisi': '🔴', 'reserved': '⏳'}
            print(f"\n{'ID':<5} {'🪑 Nomor':<14} {'👥 Kapasitas':<14} {'📌 Status':<17}")
            print("-"*50)
            for m in meja_list:
                symbol = status_symbol.get(m['status'], '•')
                status_display = f"{symbol} {m['status']}"
                print(f"{m['id']:<5} #{m['nomor_meja']:<13} {m['kapasitas']:<14} {status_display:<17}")
        
        input("\n⏎ Tekan Enter untuk melanjutkan...")
    
    def handle_lihat_meja_tersedia(self):
        """Handler untuk melihat meja tersedia."""
        print("\n✅ --- MEJA TERSEDIA ---")
        meja_list = lihat_meja_tersedia(self.db)
        
        if meja_list:
            print(f"\n{'ID':<5} {'🪑 Nomor Meja':<14} {'👥 Kapasitas':<14}")
            print("-"*33)
            for m in meja_list:
                print(f"{m['id']:<5} #{m['nomor_meja']:<13} {m['kapasitas']:<14}")
        
        input("\n⏎ Tekan Enter untuk melanjutkan...")
    
    def handle_update_meja(self):
        """Handler untuk update meja."""
        print("\n✏️  --- UPDATE MEJA ---")
        print("📋 Aturan Input:")
        print("   • Nomor Meja: 1-999")
        print("   • Kapasitas: 1-20 orang\n")
        
        try:
            meja_id = int(input("🔢 Masukkan ID Meja: "))
            nomor_meja = int(input("🪑 Nomor Meja baru (1-999): "))
            kapasitas = int(input("👥 Kapasitas baru (1-20 orang): "))
            print("\n📌 Status: 1) ✅ tersedia, 2) 🔴 terisi, 3) ⏳ reserved")
            status_choice = input("Pilih status (1-3): ").strip()
            
            status_map = {'1': 'tersedia', '2': 'terisi', '3': 'reserved'}
            status = status_map.get(status_choice, 'tersedia')
            
            update_meja(self.db, meja_id, nomor_meja, kapasitas, status)
        except ValueError:
            print("✗ Input harus berupa angka")
        
        input("\n⏎ Tekan Enter untuk melanjutkan...")
    
    def handle_hapus_meja(self):
        """Handler untuk hapus meja."""
        print("\n🗑️  --- HAPUS MEJA ---")
        try:
            meja_id = int(input("🔢 Masukkan ID Meja: "))
            konfirmasi = input(f"⚠️  Yakin ingin menghapus meja ID {meja_id}? (y/n): ")
            
            if konfirmasi.lower() == 'y':
                hapus_meja(self.db, meja_id)
        except ValueError:
            print("✗ ID harus berupa angka")
        
        input("\nTekan Enter untuk melanjutkan...")
    
    # ========== HANDLER PEMESANAN ==========
    
    def handle_tambah_pemesanan(self):
        """Handler untuk membuat pemesanan baru."""
        print("\n--- BUAT PEMESANAN BARU ---")
        print("📋 Aturan Input:")
        print("   • Jumlah Orang: 1-20 orang")
        print("   • Tanggal: Format YYYY-MM-DD HH:MM:SS (contoh: 2025-12-25 19:00:00)")
        print("   • Catatan: Maksimal 500 karakter\n")
        
        try:
            pelanggan_id = int(input("ID Pelanggan: "))
            meja_id = int(input("ID Meja: "))
            
            print("\nTanggal Pemesanan (kosongkan untuk hari ini):")
            tanggal_input = input("Format: YYYY-MM-DD HH:MM:SS atau kosongkan: ").strip()
            
            if not tanggal_input:
                tanggal_pemesanan = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            else:
                tanggal_pemesanan = tanggal_input
            
            jumlah_orang = int(input("Jumlah Orang (1-20): "))
            catatan = input("Catatan (opsional, max 500 karakter): ").strip()
            
            tambah_pemesanan(self.db, pelanggan_id, meja_id, tanggal_pemesanan, 
                           jumlah_orang, catatan)
        except ValueError:
            print("✗ Input ID dan jumlah orang harus berupa angka")
        
        input("\nTekan Enter untuk melanjutkan...")
    
    def handle_lihat_pemesanan(self):
        """Handler untuk melihat semua pemesanan."""
        print("\n--- DAFTAR PEMESANAN ---")
        pemesanan_list = lihat_pemesanan(self.db)
        
        if pemesanan_list:
            print(f"\n{'ID':<5} {'Pelanggan':<20} {'Meja':<6} {'Tanggal':<20} {'Orang':<7} {'Status':<12}")
            print("-"*70)
            for p in pemesanan_list:
                print(f"{p['id']:<5} {p['nama_pelanggan'][:19]:<20} "
                      f"#{p['nomor_meja']:<5} {str(p['tanggal_pemesanan'])[:19]:<20} "
                      f"{p['jumlah_orang']:<7} {p['status']:<12}")
        
        input("\nTekan Enter untuk melanjutkan...")
    
    def handle_lihat_pemesanan_by_status(self):
        """Handler untuk melihat pemesanan by status."""
        print("\n--- FILTER PEMESANAN BY STATUS ---")
        print("Status: 1) pending, 2) confirmed, 3) completed, 4) cancelled")
        status_choice = input("Pilih status (1-4): ").strip()
        
        status_map = {
            '1': 'pending',
            '2': 'confirmed',
            '3': 'completed',
            '4': 'cancelled'
        }
        
        status = status_map.get(status_choice)
        if not status:
            print("✗ Pilihan tidak valid")
            input("\nTekan Enter untuk melanjutkan...")
            return
        
        pemesanan_list = lihat_pemesanan(self.db, status=status)
        
        if pemesanan_list:
            print(f"\n{'ID':<5} {'Pelanggan':<20} {'Meja':<6} {'Tanggal':<20} {'Orang':<7}")
            print("-"*58)
            for p in pemesanan_list:
                print(f"{p['id']:<5} {p['nama_pelanggan'][:19]:<20} "
                      f"#{p['nomor_meja']:<5} {str(p['tanggal_pemesanan'])[:19]:<20} "
                      f"{p['jumlah_orang']:<7}")
        
        input("\nTekan Enter untuk melanjutkan...")
    
    def handle_konfirmasi_pemesanan(self):
        """Handler untuk konfirmasi pemesanan."""
        print("\n--- KONFIRMASI PEMESANAN ---")
        try:
            pemesanan_id = int(input("Masukkan ID Pemesanan: "))
            konfirmasi_pemesanan(self.db, pemesanan_id)
        except ValueError:
            print("✗ ID harus berupa angka")
        
        input("\nTekan Enter untuk melanjutkan...")
    
    def handle_selesaikan_pemesanan(self):
        """Handler untuk menyelesaikan pemesanan."""
        print("\n--- SELESAIKAN PEMESANAN ---")
        try:
            pemesanan_id = int(input("Masukkan ID Pemesanan: "))
            selesaikan_pemesanan(self.db, pemesanan_id)
        except ValueError:
            print("✗ ID harus berupa angka")
        
        input("\nTekan Enter untuk melanjutkan...")
    
    def handle_batalkan_pemesanan(self):
        """Handler untuk membatalkan pemesanan."""
        print("\n--- BATALKAN PEMESANAN ---")
        try:
            pemesanan_id = int(input("Masukkan ID Pemesanan: "))
            konfirmasi = input(f"Yakin ingin membatalkan pemesanan ID {pemesanan_id}? (y/n): ")
            
            if konfirmasi.lower() == 'y':
                batalkan_pemesanan(self.db, pemesanan_id)
        except ValueError:
            print("✗ ID harus berupa angka")
        
        input("\nTekan Enter untuk melanjutkan...")
    
    def handle_hapus_pemesanan(self):
        """Handler untuk menghapus pemesanan."""
        print("\n--- HAPUS PEMESANAN ---")
        try:
            pemesanan_id = int(input("Masukkan ID Pemesanan: "))
            konfirmasi = input(f"Yakin ingin menghapus pemesanan ID {pemesanan_id}? (y/n): ")
            
            if konfirmasi.lower() == 'y':
                hapus_pemesanan(self.db, pemesanan_id)
        except ValueError:
            print("✗ ID harus berupa angka")
        
        input("\nTekan Enter untuk melanjutkan...")
    
    # ========== HANDLER LAPORAN ==========
    
    def handle_laporan_semua(self):
        """Handler untuk laporan semua pemesanan."""
        print("\n--- LAPORAN SEMUA PEMESANAN ---")
        laporan = generate_laporan_pemesanan(self.db)
        
        if laporan:
            print_laporan(laporan)
        
        input("\nTekan Enter untuk melanjutkan...")
    
    def handle_laporan_by_status(self):
        """Handler untuk laporan by status."""
        print("\n--- LAPORAN BY STATUS ---")
        print("Status: 1) pending, 2) confirmed, 3) completed, 4) cancelled")
        status_choice = input("Pilih status (1-4): ").strip()
        
        status_map = {
            '1': 'pending',
            '2': 'confirmed',
            '3': 'completed',
            '4': 'cancelled'
        }
        
        status = status_map.get(status_choice)
        if not status:
            print("✗ Pilihan tidak valid")
            input("\nTekan Enter untuk melanjutkan...")
            return
        
        laporan = generate_laporan_pemesanan(self.db, status=status)
        
        if laporan:
            print_laporan(laporan)
        
        input("\nTekan Enter untuk melanjutkan...")
    
    def handle_laporan_by_tanggal(self):
        """Handler untuk laporan by tanggal."""
        print("\n--- LAPORAN BY TANGGAL ---")
        tanggal_mulai = input("Tanggal Mulai (YYYY-MM-DD): ").strip()
        tanggal_akhir = input("Tanggal Akhir (YYYY-MM-DD): ").strip()
        
        laporan = generate_laporan_pemesanan(self.db, 
                                            tanggal_mulai=tanggal_mulai, 
                                            tanggal_akhir=tanggal_akhir)
        
        if laporan:
            print_laporan(laporan)
        
        input("\nTekan Enter untuk melanjutkan...")
    
    # ========== MENU LOOPS ==========
    
    def menu_pelanggan_loop(self):
        """Loop untuk menu pelanggan."""
        while True:
            self.tampilkan_menu_pelanggan()
            pilihan = input("Pilih menu: ").strip()
            
            if pilihan == '1':
                self.handle_tambah_pelanggan()
            elif pilihan == '2':
                self.handle_lihat_pelanggan()
            elif pilihan == '3':
                self.handle_cari_pelanggan()
            elif pilihan == '4':
                self.handle_update_pelanggan()
            elif pilihan == '5':
                self.handle_hapus_pelanggan()
            elif pilihan == '0':
                break
            else:
                print("✗ Pilihan tidak valid")
                input("\nTekan Enter untuk melanjutkan...")
    
    def menu_meja_loop(self):
        """Loop untuk menu meja."""
        while True:
            self.tampilkan_menu_meja()
            pilihan = input("Pilih menu: ").strip()
            
            if pilihan == '1':
                self.handle_tambah_meja()
            elif pilihan == '2':
                self.handle_lihat_meja()
            elif pilihan == '3':
                self.handle_lihat_meja_tersedia()
            elif pilihan == '4':
                self.handle_update_meja()
            elif pilihan == '5':
                self.handle_hapus_meja()
            elif pilihan == '0':
                break
            else:
                print("✗ Pilihan tidak valid")
                input("\nTekan Enter untuk melanjutkan...")
    
    def menu_pemesanan_loop(self):
        """Loop untuk menu pemesanan."""
        while True:
            self.tampilkan_menu_pemesanan()
            pilihan = input("Pilih menu: ").strip()
            
            if pilihan == '1':
                self.handle_tambah_pemesanan()
            elif pilihan == '2':
                self.handle_lihat_pemesanan()
            elif pilihan == '3':
                self.handle_lihat_pemesanan_by_status()
            elif pilihan == '4':
                self.handle_konfirmasi_pemesanan()
            elif pilihan == '5':
                self.handle_selesaikan_pemesanan()
            elif pilihan == '6':
                self.handle_batalkan_pemesanan()
            elif pilihan == '7':
                self.handle_hapus_pemesanan()
            elif pilihan == '0':
                break
            else:
                print("✗ Pilihan tidak valid")
                input("\nTekan Enter untuk melanjutkan...")
    
    def handle_analisis_statistik(self):
        """Handler untuk menampilkan analisis statistik lengkap."""
        print("\n📈 --- ANALISIS STATISTIK LENGKAP ---\n")
        
        # Ambil semua data pemesanan
        from services.restaurant_service import analisis_laporan
        laporan = generate_laporan_pemesanan(self.db)
        
        if not laporan:
            print("❌ Tidak ada data untuk dianalisis")
            input("\n⏎ Tekan Enter untuk melanjutkan...")
            return
        
        analisis = analisis_laporan(laporan)
        
        if analisis:
            print("="*70)
            print("📊 DASHBOARD STATISTIK RESTORAN")
            print("="*70)
            
            # Statistik Umum
            print("\n📌 STATISTIK UMUM:")
            print(f"   🔢 Total Pemesanan        : {analisis['total_pemesanan']} pemesanan")
            print(f"   👥 Total Tamu             : {analisis['total_orang']} orang")
            print(f"   📊 Rata-rata Tamu/Pesanan : {analisis['avg_orang']:.2f} orang")
            
            # Distribusi Status dengan Bar Chart
            print("\n📌 DISTRIBUSI STATUS:")
            status_symbol = {
                'pending': '⏳',
                'confirmed': '✅',
                'completed': '🎉',
                'cancelled': '❌'
            }
            
            for status, count in sorted(analisis['status_count'].items(), key=lambda x: x[1], reverse=True):
                symbol = status_symbol.get(status, '•')
                percentage = (count / analisis['total_pemesanan']) * 100
                bar_length = int(percentage / 2)  # Skala 50 karakter
                bar = '█' * bar_length + '░' * (50 - bar_length)
                print(f"   {symbol} {status:10} : {count:3} ({percentage:5.1f}%) [{bar}]")
            
            # Performa Restoran
            print("\n🏆 PERFORMA RESTORAN:")
            if analisis['meja_populer'][0]:
                print(f"   🪑 Meja Terpopuler       : Meja #{analisis['meja_populer'][0]} ({analisis['meja_populer'][1]} kali pemesanan)")
            if analisis['pelanggan_setia'][0]:
                print(f"   ⭐ Pelanggan Setia        : {analisis['pelanggan_setia'][0]} ({analisis['pelanggan_setia'][1]} kali pemesanan)")
            
            # Tingkat Keberhasilan
            completed = analisis['status_count'].get('completed', 0)
            cancelled = analisis['status_count'].get('cancelled', 0)
            total_selesai = completed + cancelled
            
            if total_selesai > 0:
                success_rate = (completed / total_selesai) * 100
                print(f"\n📈 TINGKAT KEBERHASILAN:")
                print(f"   🎉 Pemesanan Selesai      : {completed}")
                print(f"   ❌ Pemesanan Dibatalkan   : {cancelled}")
                print(f"   📊 Success Rate          : {success_rate:.1f}%")
                
                # Visual success rate
                success_bar = '█' * int(success_rate / 2)
                print(f"   [{success_bar:<50}]")
            
            print("\n" + "="*70)
        
        input("\n⏎ Tekan Enter untuk melanjutkan...")
    
    def menu_laporan_loop(self):
        """Loop untuk menu laporan."""
        while True:
            self.tampilkan_menu_laporan()
            pilihan = input("Pilih menu: ").strip()
            
            if pilihan == '1':
                self.handle_laporan_semua()
            elif pilihan == '2':
                self.handle_laporan_by_status()
            elif pilihan == '3':
                self.handle_laporan_by_tanggal()
            elif pilihan == '4':
                self.handle_analisis_statistik()
            elif pilihan == '0':
                break
            else:
                print("✗ Pilihan tidak valid")
                input("\n⏎ Tekan Enter untuk melanjutkan...")
    
    def handle_run_tests(self):
        """Handler untuk menjalankan unit tests."""
        self.clear_screen()
        print("\n" + "="*70)
        print(" "*20 + "MENJALANKAN UNIT TESTS")
        print("="*70 + "\n")
        
        from tests.test_models import run_tests
        run_tests()
        
        input("\nTekan Enter untuk melanjutkan...")
    
    def run(self):
        """Menjalankan aplikasi utama."""
        # Setup database
        self.clear_screen()
        print("\n" + "="*60)
        print(" "*10 + "INISIALISASI SISTEM PEMESANAN RESTORAN")
        print("="*60 + "\n")
        
        print("Konfigurasi Database:")
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
        
        self.db = init_database(db_config)
        
        if not self.db:
            print("\n✗ Gagal menginisialisasi database!")
            print("Pastikan MySQL/MariaDB sudah running dan kredensial benar.")
            input("\nTekan Enter untuk keluar...")
            return
        
        print("\n✓ Sistem siap digunakan!")
        input("\nTekan Enter untuk melanjutkan...")
        
        # Main loop
        while self.running:
            self.tampilkan_menu_utama()
            pilihan = input("Pilih menu: ").strip()
            
            if pilihan == '1':
                self.menu_pelanggan_loop()
            elif pilihan == '2':
                self.menu_meja_loop()
            elif pilihan == '3':
                self.menu_pemesanan_loop()
            elif pilihan == '4':
                self.menu_laporan_loop()
            elif pilihan == '5':
                self.handle_run_tests()
            elif pilihan == '0':
                print("\nTerima kasih telah menggunakan sistem kami!")
                self.running = False
            else:
                print("✗ Pilihan tidak valid")
                input("\nTekan Enter untuk melanjutkan...")
        
        # Tutup koneksi database
        if self.db:
            self.db.disconnect()


def main():
    """
    Fungsi main untuk menjalankan aplikasi.
    """
    app = RestaurantApp()
    app.run()


if __name__ == '__main__':
    main()
