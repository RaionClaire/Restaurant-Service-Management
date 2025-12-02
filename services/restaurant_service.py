"""
Restaurant Service Module
Module ini berisi fungsi-fungsi untuk operasi bisnis restoran.
"""

from database.db_manager import DatabaseManager
from models.pelanggan import Pelanggan
from models.meja import Meja
from models.pemesanan import Pemesanan
from typing import Optional, List, Dict


def init_database(db_config: Dict = None) -> DatabaseManager:
    """
    Inisialisasi koneksi database dan buat tabel jika belum ada.
    
    Args:
        db_config (dict, optional): Konfigurasi database. Default None.
    
    Returns:
        DatabaseManager: Instance database manager yang sudah terkoneksi
    """
    if db_config:
        db = DatabaseManager(**db_config)
    else:
        # Gunakan konfigurasi default
        db = DatabaseManager()
    
    # Coba koneksi ke database
    if db.connect():
        print("✓ Berhasil terhubung ke database")
        # Buat tabel jika belum ada
        if db.create_tables():
            print("✓ Tabel database siap digunakan")
        return db
    else:
        print("✗ Gagal terhubung ke database")
        return None


# ========== FUNGSI PELANGGAN ==========

def tambah_pelanggan(db: DatabaseManager, nama: str, telepon: str, email: str = "") -> Optional[int]:
    """
    Menambahkan pelanggan baru.
    
    Args:
        db (DatabaseManager): Instance database manager
        nama (str): Nama pelanggan
        telepon (str): Nomor telepon
        email (str, optional): Email pelanggan. Default "".
    
    Returns:
        int: ID pelanggan baru, atau None jika gagal
    """
    # Validasi input menggunakan objek Pelanggan
    pelanggan = Pelanggan(nama=nama, telepon=telepon, email=email)
    is_valid, error_msg = pelanggan.validate_data()
    
    if not is_valid:
        print(f"✗ Validasi gagal: {error_msg}")
        return None
    
    # Simpan ke database
    pelanggan_id = db.create_pelanggan(nama, telepon, email)
    
    if pelanggan_id:
        print(f"✓ Pelanggan '{nama}' berhasil ditambahkan dengan ID: {pelanggan_id}")
        return pelanggan_id
    else:
        print("✗ Gagal menambahkan pelanggan")
        return None


def lihat_pelanggan(db: DatabaseManager, pelanggan_id: int = None) -> Optional[List[Dict]]:
    """
    Melihat data pelanggan.
    
    Args:
        db (DatabaseManager): Instance database manager
        pelanggan_id (int, optional): ID pelanggan spesifik. Default None (semua).
    
    Returns:
        list: List dictionary data pelanggan, atau None jika gagal
    """
    pelanggan_list = db.read_pelanggan(pelanggan_id)
    
    if pelanggan_list:
        return pelanggan_list
    else:
        if pelanggan_id:
            print(f"✗ Pelanggan dengan ID {pelanggan_id} tidak ditemukan")
        else:
            print("✗ Tidak ada data pelanggan")
        return None


def update_pelanggan(db: DatabaseManager, pelanggan_id: int, nama: str, 
                    telepon: str, email: str) -> bool:
    """
    Mengupdate data pelanggan.
    
    Args:
        db (DatabaseManager): Instance database manager
        pelanggan_id (int): ID pelanggan
        nama (str): Nama baru
        telepon (str): Telepon baru
        email (str): Email baru
    
    Returns:
        bool: True jika berhasil, False jika gagal
    """
    # Validasi input
    pelanggan = Pelanggan(id=pelanggan_id, nama=nama, telepon=telepon, email=email)
    is_valid, error_msg = pelanggan.validate_data()
    
    if not is_valid:
        print(f"✗ Validasi gagal: {error_msg}")
        return False
    
    # Update database
    if db.update_pelanggan(pelanggan_id, nama, telepon, email):
        print(f"✓ Data pelanggan ID {pelanggan_id} berhasil diupdate")
        return True
    else:
        print(f"✗ Gagal mengupdate pelanggan ID {pelanggan_id}")
        return False


def hapus_pelanggan(db: DatabaseManager, pelanggan_id: int) -> bool:
    """
    Menghapus pelanggan.
    
    Args:
        db (DatabaseManager): Instance database manager
        pelanggan_id (int): ID pelanggan yang akan dihapus
    
    Returns:
        bool: True jika berhasil, False jika gagal
    """
    if db.delete_pelanggan(pelanggan_id):
        print(f"✓ Pelanggan ID {pelanggan_id} berhasil dihapus")
        return True
    else:
        print(f"✗ Gagal menghapus pelanggan ID {pelanggan_id}")
        return False


# ========== FUNGSI MEJA ==========

def tambah_meja(db: DatabaseManager, nomor_meja: int, kapasitas: int, 
               status: str = 'tersedia') -> Optional[int]:
    """
    Menambahkan meja baru.
    
    Args:
        db (DatabaseManager): Instance database manager
        nomor_meja (int): Nomor meja
        kapasitas (int): Kapasitas meja
        status (str, optional): Status meja. Default 'tersedia'.
    
    Returns:
        int: ID meja baru, atau None jika gagal
    """
    # Validasi input
    meja = Meja(nomor_meja=nomor_meja, kapasitas=kapasitas, status=status)
    is_valid, error_msg = meja.validate_data()
    
    if not is_valid:
        print(f"✗ Validasi gagal: {error_msg}")
        return None
    
    # Simpan ke database
    meja_id = db.create_meja(nomor_meja, kapasitas, status)
    
    if meja_id:
        print(f"✓ Meja nomor {nomor_meja} berhasil ditambahkan dengan ID: {meja_id}")
        return meja_id
    else:
        print("✗ Gagal menambahkan meja")
        return None


def lihat_meja(db: DatabaseManager, meja_id: int = None, status: str = None) -> Optional[List[Dict]]:
    """
    Melihat data meja.
    
    Args:
        db (DatabaseManager): Instance database manager
        meja_id (int, optional): ID meja spesifik. Default None.
        status (str, optional): Filter status. Default None.
    
    Returns:
        list: List dictionary data meja, atau None jika gagal
    """
    meja_list = db.read_meja(meja_id, status)
    
    if meja_list:
        return meja_list
    else:
        if meja_id:
            print(f"✗ Meja dengan ID {meja_id} tidak ditemukan")
        else:
            print("✗ Tidak ada data meja")
        return None


def update_meja(db: DatabaseManager, meja_id: int, nomor_meja: int, 
               kapasitas: int, status: str) -> bool:
    """
    Mengupdate data meja.
    
    Args:
        db (DatabaseManager): Instance database manager
        meja_id (int): ID meja
        nomor_meja (int): Nomor meja baru
        kapasitas (int): Kapasitas baru
        status (str): Status baru
    
    Returns:
        bool: True jika berhasil, False jika gagal
    """
    # Validasi input
    meja = Meja(id=meja_id, nomor_meja=nomor_meja, kapasitas=kapasitas, status=status)
    is_valid, error_msg = meja.validate_data()
    
    if not is_valid:
        print(f"✗ Validasi gagal: {error_msg}")
        return False
    
    # Update database
    if db.update_meja(meja_id, nomor_meja, kapasitas, status):
        print(f"✓ Data meja ID {meja_id} berhasil diupdate")
        return True
    else:
        print(f"✗ Gagal mengupdate meja ID {meja_id}")
        return False


def hapus_meja(db: DatabaseManager, meja_id: int) -> bool:
    """
    Menghapus meja.
    
    Args:
        db (DatabaseManager): Instance database manager
        meja_id (int): ID meja yang akan dihapus
    
    Returns:
        bool: True jika berhasil, False jika gagal
    """
    if db.delete_meja(meja_id):
        print(f"✓ Meja ID {meja_id} berhasil dihapus")
        return True
    else:
        print(f"✗ Gagal menghapus meja ID {meja_id}")
        return False


def lihat_meja_tersedia(db: DatabaseManager) -> Optional[List[Dict]]:
    """
    Melihat daftar meja yang tersedia.
    
    Args:
        db (DatabaseManager): Instance database manager
    
    Returns:
        list: List dictionary meja tersedia, atau None jika tidak ada
    """
    return lihat_meja(db, status='tersedia')


# ========== FUNGSI PEMESANAN ==========

def tambah_pemesanan(db: DatabaseManager, pelanggan_id: int, meja_id: int,
                    tanggal_pemesanan: str, jumlah_orang: int, 
                    catatan: str = "") -> Optional[int]:
    """
    Menambahkan pemesanan baru.
    
    Args:
        db (DatabaseManager): Instance database manager
        pelanggan_id (int): ID pelanggan
        meja_id (int): ID meja
        tanggal_pemesanan (str): Tanggal dan waktu pemesanan
        jumlah_orang (int): Jumlah orang
        catatan (str, optional): Catatan tambahan. Default "".
    
    Returns:
        int: ID pemesanan baru, atau None jika gagal
    """
    # Validasi input
    pemesanan = Pemesanan(pelanggan_id=pelanggan_id, meja_id=meja_id,
                         tanggal_pemesanan=tanggal_pemesanan, 
                         jumlah_orang=jumlah_orang, catatan=catatan)
    is_valid, error_msg = pemesanan.validate_data()
    
    if not is_valid:
        print(f"✗ Validasi gagal: {error_msg}")
        return None
    
    # Cek apakah meja tersedia
    meja = db.read_meja(meja_id)
    if not meja or len(meja) == 0:
        print(f"✗ Meja dengan ID {meja_id} tidak ditemukan")
        return None
    
    if meja[0]['status'] != 'tersedia':
        print(f"✗ Meja nomor {meja[0]['nomor_meja']} tidak tersedia (status: {meja[0]['status']})")
        return None
    
    # Cek kapasitas meja
    if jumlah_orang > meja[0]['kapasitas']:
        print(f"✗ Jumlah orang ({jumlah_orang}) melebihi kapasitas meja ({meja[0]['kapasitas']})")
        return None
    
    # Simpan pemesanan
    pemesanan_id = db.create_pemesanan(pelanggan_id, meja_id, tanggal_pemesanan,
                                       jumlah_orang, 'pending', catatan)
    
    if pemesanan_id:
        # Update status meja menjadi reserved
        db.update_meja_status(meja_id, 'reserved')
        print(f"✓ Pemesanan berhasil dibuat dengan ID: {pemesanan_id}")
        return pemesanan_id
    else:
        print("✗ Gagal membuat pemesanan")
        return None


def lihat_pemesanan(db: DatabaseManager, pemesanan_id: int = None, 
                   status: str = None) -> Optional[List[Dict]]:
    """
    Melihat data pemesanan.
    
    Args:
        db (DatabaseManager): Instance database manager
        pemesanan_id (int, optional): ID pemesanan spesifik. Default None.
        status (str, optional): Filter status. Default None.
    
    Returns:
        list: List dictionary data pemesanan, atau None jika gagal
    """
    pemesanan_list = db.read_pemesanan(pemesanan_id, status)
    
    if pemesanan_list:
        return pemesanan_list
    else:
        if pemesanan_id:
            print(f"✗ Pemesanan dengan ID {pemesanan_id} tidak ditemukan")
        else:
            print("✗ Tidak ada data pemesanan")
        return None


def konfirmasi_pemesanan(db: DatabaseManager, pemesanan_id: int) -> bool:
    """
    Mengkonfirmasi pemesanan dan mengubah status meja menjadi terisi.
    
    Args:
        db (DatabaseManager): Instance database manager
        pemesanan_id (int): ID pemesanan
    
    Returns:
        bool: True jika berhasil, False jika gagal
    """
    # Ambil data pemesanan
    pemesanan = db.read_pemesanan(pemesanan_id)
    
    if not pemesanan or len(pemesanan) == 0:
        print(f"✗ Pemesanan ID {pemesanan_id} tidak ditemukan")
        return False
    
    # Update status pemesanan
    if db.update_pemesanan_status(pemesanan_id, 'confirmed'):
        # Update status meja menjadi terisi
        db.update_meja_status(pemesanan[0]['meja_id'], 'terisi')
        print(f"✓ Pemesanan ID {pemesanan_id} dikonfirmasi")
        return True
    else:
        print(f"✗ Gagal mengkonfirmasi pemesanan ID {pemesanan_id}")
        return False


def selesaikan_pemesanan(db: DatabaseManager, pemesanan_id: int) -> bool:
    """
    Menyelesaikan pemesanan dan membebaskan meja.
    
    Args:
        db (DatabaseManager): Instance database manager
        pemesanan_id (int): ID pemesanan
    
    Returns:
        bool: True jika berhasil, False jika gagal
    """
    # Ambil data pemesanan
    pemesanan = db.read_pemesanan(pemesanan_id)
    
    if not pemesanan or len(pemesanan) == 0:
        print(f"✗ Pemesanan ID {pemesanan_id} tidak ditemukan")
        return False
    
    # Update status pemesanan
    if db.update_pemesanan_status(pemesanan_id, 'completed'):
        # Bebaskan meja (ubah status menjadi tersedia)
        db.update_meja_status(pemesanan[0]['meja_id'], 'tersedia')
        print(f"✓ Pemesanan ID {pemesanan_id} selesai, meja nomor {pemesanan[0]['nomor_meja']} tersedia")
        return True
    else:
        print(f"✗ Gagal menyelesaikan pemesanan ID {pemesanan_id}")
        return False


def batalkan_pemesanan(db: DatabaseManager, pemesanan_id: int) -> bool:
    """
    Membatalkan pemesanan dan membebaskan meja.
    
    Args:
        db (DatabaseManager): Instance database manager
        pemesanan_id (int): ID pemesanan
    
    Returns:
        bool: True jika berhasil, False jika gagal
    """
    # Ambil data pemesanan
    pemesanan = db.read_pemesanan(pemesanan_id)
    
    if not pemesanan or len(pemesanan) == 0:
        print(f"✗ Pemesanan ID {pemesanan_id} tidak ditemukan")
        return False
    
    # Update status pemesanan
    if db.update_pemesanan_status(pemesanan_id, 'cancelled'):
        # Bebaskan meja jika belum selesai
        if pemesanan[0]['status'] != 'completed':
            db.update_meja_status(pemesanan[0]['meja_id'], 'tersedia')
        print(f"✓ Pemesanan ID {pemesanan_id} dibatalkan")
        return True
    else:
        print(f"✗ Gagal membatalkan pemesanan ID {pemesanan_id}")
        return False


def hapus_pemesanan(db: DatabaseManager, pemesanan_id: int) -> bool:
    """
    Menghapus pemesanan dari database.
    
    Args:
        db (DatabaseManager): Instance database manager
        pemesanan_id (int): ID pemesanan yang akan dihapus
    
    Returns:
        bool: True jika berhasil, False jika gagal
    """
    # Ambil data pemesanan terlebih dahulu untuk bebaskan meja jika perlu
    pemesanan = db.read_pemesanan(pemesanan_id)
    
    if pemesanan and len(pemesanan) > 0:
        # Bebaskan meja jika pemesanan masih aktif
        if pemesanan[0]['status'] in ['pending', 'confirmed']:
            db.update_meja_status(pemesanan[0]['meja_id'], 'tersedia')
    
    if db.delete_pemesanan(pemesanan_id):
        print(f"✓ Pemesanan ID {pemesanan_id} berhasil dihapus")
        return True
    else:
        print(f"✗ Gagal menghapus pemesanan ID {pemesanan_id}")
        return False


# ========== FUNGSI LAPORAN ==========

def generate_laporan_pemesanan(db: DatabaseManager, status: str = None,
                               tanggal_mulai: str = None, 
                               tanggal_akhir: str = None) -> Optional[List[Dict]]:
    """
    Menghasilkan laporan pemesanan dengan filter.
    
    Args:
        db (DatabaseManager): Instance database manager
        status (str, optional): Filter status. Default None.
        tanggal_mulai (str, optional): Filter tanggal mulai. Default None.
        tanggal_akhir (str, optional): Filter tanggal akhir. Default None.
    
    Returns:
        list: List dictionary laporan pemesanan, atau None jika gagal
    """
    laporan = db.get_laporan_pemesanan(status, tanggal_mulai, tanggal_akhir)
    
    if laporan:
        print(f"✓ Laporan berhasil dihasilkan: {len(laporan)} record")
        return laporan
    else:
        print("✗ Tidak ada data untuk laporan")
        return None


def print_laporan(laporan: List[Dict]):
    """
    Mencetak laporan pemesanan dengan format yang rapi.
    
    Args:
        laporan (list): List dictionary data pemesanan
    """
    if not laporan or len(laporan) == 0:
        print("Tidak ada data untuk ditampilkan")
        return
    
    print("\n" + "="*100)
    print("LAPORAN PEMESANAN RESTORAN")
    print("="*100)
    
    # Header tabel
    print(f"{'ID':<5} {'Pelanggan':<20} {'Meja':<6} {'Tanggal':<20} {'Orang':<7} {'Status':<12} {'Catatan':<20}")
    print("-"*100)
    
    # Data
    for item in laporan:
        pemesanan_id = str(item['id'])
        nama = item['nama_pelanggan'][:19]  # Batasi panjang
        meja = f"#{item['nomor_meja']}"
        tanggal = str(item['tanggal_pemesanan'])[:19]
        orang = str(item['jumlah_orang'])
        status = item['status']
        catatan = item['catatan'][:19] if item['catatan'] else "-"
        
        print(f"{pemesanan_id:<5} {nama:<20} {meja:<6} {tanggal:<20} {orang:<7} {status:<12} {catatan:<20}")
    
    print("="*100)
    print(f"Total: {len(laporan)} pemesanan\n")
