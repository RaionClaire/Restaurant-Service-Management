"""
Demo Fitur Analisis - Sistem Pemesanan Restoran
Script untuk testing fitur analisis dan simbol visual yang baru ditambahkan.
"""

from database.db_manager import DatabaseManager
from services.restaurant_service import *
from datetime import datetime, timedelta


def demo_analisis():
    """Demo fitur analisis statistik."""
    print("\n" + "="*70)
    print("🎯 DEMO FITUR ANALISIS & SIMBOL VISUAL")
    print("="*70)
    
    # Setup database
    print("\n📋 Setup Database...")
    db = DatabaseManager(
        host='localhost',
        database='restaurant_db',
        user='root',
        password=''
    )
    
    if not db.connect():
        print("❌ Gagal koneksi database!")
        return
    
    print("✅ Database terkoneksi!")
    db.create_tables()
    
    # Buat data sample
    print("\n📝 Membuat data sample...")
    
    # Tambah pelanggan
    pelanggan_ids = []
    pelanggan_data = [
        ("Alice Johnson", "081234567890", "alice@email.com"),
        ("Bob Smith", "082345678901", "bob@email.com"),
        ("Charlie Brown", "083456789012", "charlie@email.com"),
        ("Diana Prince", "084567890123", "diana@email.com"),
        ("Eve Wilson", "085678901234", "eve@email.com")
    ]
    
    for nama, telepon, email in pelanggan_data:
        pid = tambah_pelanggan(db, nama, telepon, email)
        if pid:
            pelanggan_ids.append(pid)
    
    # Tambah meja
    meja_ids = []
    for i in range(1, 11):  # 10 meja
        mid = tambah_meja(db, nomor_meja=i, kapasitas=4 if i <= 5 else 6, status='tersedia')
        if mid:
            meja_ids.append(mid)
    
    # Buat pemesanan dengan berbagai status
    print("\n🎫 Membuat pemesanan sample...")
    
    pemesanan_data = [
        # (pelanggan_idx, meja_idx, jumlah_orang, days_ago, status)
        (0, 0, 4, 5, 'completed'),   # Alice, completed
        (1, 1, 3, 5, 'completed'),   # Bob, completed
        (0, 2, 4, 4, 'completed'),   # Alice lagi, completed (loyal customer)
        (2, 3, 5, 4, 'cancelled'),   # Charlie, cancelled
        (3, 4, 4, 3, 'completed'),   # Diana, completed
        (4, 5, 6, 3, 'completed'),   # Eve, completed
        (0, 6, 4, 2, 'confirmed'),   # Alice lagi (most loyal)
        (1, 7, 3, 2, 'confirmed'),   # Bob lagi
        (2, 8, 5, 1, 'pending'),     # Charlie, pending
        (3, 9, 4, 1, 'pending'),     # Diana, pending
        (4, 0, 2, 0, 'pending'),     # Eve, pending (today)
    ]
    
    for p_idx, m_idx, jumlah, days_ago, final_status in pemesanan_data:
        tanggal = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d %H:%M:%S')
        
        # Buat pemesanan
        pemesanan_id = tambah_pemesanan(
            db, 
            pelanggan_ids[p_idx], 
            meja_ids[m_idx], 
            tanggal, 
            jumlah, 
            "Sample data"
        )
        
        # Update status sesuai scenario
        if pemesanan_id:
            if final_status == 'confirmed':
                konfirmasi_pemesanan(db, pemesanan_id)
            elif final_status == 'completed':
                konfirmasi_pemesanan(db, pemesanan_id)
                selesaikan_pemesanan(db, pemesanan_id)
            elif final_status == 'cancelled':
                batalkan_pemesanan(db, pemesanan_id)
    
    print("\n✅ Data sample berhasil dibuat!")
    
    # Demo Laporan dengan Analisis
    print("\n" + "="*70)
    print("📊 LAPORAN LENGKAP DENGAN ANALISIS")
    print("="*70)
    
    laporan = generate_laporan_pemesanan(db)
    if laporan:
        print_laporan(laporan)
    
    # Demo Analisis Spesifik
    print("\n" + "="*70)
    print("📈 ANALISIS STATISTIK DETAIL")
    print("="*70)
    
    analisis = analisis_laporan(laporan)
    
    if analisis:
        print("\n🔢 METRIK KINERJA:")
        print(f"   📊 Total Pemesanan        : {analisis['total_pemesanan']}")
        print(f"   👥 Total Tamu             : {analisis['total_orang']}")
        print(f"   📈 Rata-rata per Pemesanan: {analisis['avg_orang']:.2f} orang")
        
        print("\n📌 BREAKDOWN STATUS:")
        status_symbol = {
            'pending': '⏳',
            'confirmed': '✅',
            'completed': '🎉',
            'cancelled': '❌'
        }
        
        for status, count in analisis['status_count'].items():
            symbol = status_symbol.get(status, '•')
            percentage = (count / analisis['total_pemesanan']) * 100
            print(f"   {symbol} {status:10} : {count:3} ({percentage:5.1f}%)")
        
        print("\n🏆 TOP PERFORMERS:")
        if analisis['meja_populer'][0]:
            print(f"   🪑 Meja Favorit: Meja #{analisis['meja_populer'][0]} ({analisis['meja_populer'][1]}x)")
        if analisis['pelanggan_setia'][0]:
            print(f"   ⭐ Pelanggan VIP: {analisis['pelanggan_setia'][0]} ({analisis['pelanggan_setia'][1]}x)")
    
    # Demo Laporan by Status
    print("\n" + "="*70)
    print("📋 LAPORAN PEMESANAN SELESAI (COMPLETED)")
    print("="*70)
    
    laporan_completed = generate_laporan_pemesanan(db, status='completed')
    if laporan_completed:
        print_laporan(laporan_completed)
    
    # Demo Laporan by Tanggal
    print("\n" + "="*70)
    print("📅 LAPORAN 3 HARI TERAKHIR")
    print("="*70)
    
    tanggal_akhir = datetime.now().strftime('%Y-%m-%d')
    tanggal_mulai = (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')
    
    laporan_tanggal = generate_laporan_pemesanan(db, tanggal_mulai=tanggal_mulai, tanggal_akhir=tanggal_akhir)
    if laporan_tanggal:
        print_laporan(laporan_tanggal)
    
    # Visual Summary
    print("\n" + "="*70)
    print("🎨 VISUAL SUMMARY")
    print("="*70)
    
    if analisis:
        completed = analisis['status_count'].get('completed', 0)
        cancelled = analisis['status_count'].get('cancelled', 0)
        total_final = completed + cancelled
        
        if total_final > 0:
            success_rate = (completed / total_final) * 100
            
            print(f"\n📊 Success Rate: {success_rate:.1f}%")
            
            # Bar chart ASCII
            bar_filled = int(success_rate / 2)
            bar_empty = 50 - bar_filled
            bar = '█' * bar_filled + '░' * bar_empty
            print(f"   [{bar}]")
            
            print(f"\n   🎉 Selesai   : {completed:3} pemesanan")
            print(f"   ❌ Dibatalkan: {cancelled:3} pemesanan")
    
    # Cleanup
    print("\n" + "="*70)
    print("✅ Demo selesai! Data sample tersimpan di database.")
    print("   Jalankan main.py untuk melihat fitur lengkap dengan menu interaktif.")
    print("="*70 + "\n")
    
    db.disconnect()


if __name__ == '__main__':
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   🎯 DEMO FITUR BARU - SISTEM PEMESANAN RESTORAN            ║
║                                                              ║
║   ✨ Fitur yang didemonstrasikan:                           ║
║   1. 📊 Analisis statistik otomatis di laporan              ║
║   2. 🎨 Simbol visual yang menarik                          ║
║   3. 📈 Dashboard statistik lengkap                         ║
║   4. 📊 Bar chart ASCII untuk visualisasi                   ║
║   5. 🏆 Deteksi pelanggan setia & meja populer              ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    try:
        demo_analisis()
    except KeyboardInterrupt:
        print("\n\n❌ Demo dibatalkan oleh user.")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
