"""
Pemesanan Module
Module ini berisi kelas Pemesanan yang mewarisi dari BaseEntity.
"""

from .base_entity import BaseEntity
from datetime import datetime


class Pemesanan(BaseEntity):
    """
    Kelas untuk merepresentasikan pemesanan meja di restoran.
    Mewarisi dari BaseEntity dan menambahkan atribut khusus pemesanan.
    
    Attributes:
        pelanggan_id (int): ID pelanggan yang melakukan pemesanan
        meja_id (int): ID meja yang dipesan
        tanggal_pemesanan (str): Tanggal dan waktu pemesanan
        jumlah_orang (int): Jumlah orang yang akan datang
        status (str): Status pemesanan ('pending', 'confirmed', 'completed', 'cancelled')
        catatan (str): Catatan tambahan untuk pemesanan
    """
    
    # Konstanta untuk status pemesanan
    STATUS_PENDING = 'pending'
    STATUS_CONFIRMED = 'confirmed'
    STATUS_COMPLETED = 'completed'
    STATUS_CANCELLED = 'cancelled'
    
    def __init__(self, id=None, pelanggan_id=None, meja_id=None, 
                 tanggal_pemesanan=None, jumlah_orang=1, 
                 status=STATUS_PENDING, catatan=""):
        """
        Inisialisasi objek Pemesanan.
        
        Args:
            id (int, optional): ID pemesanan. Default None.
            pelanggan_id (int, optional): ID pelanggan. Default None.
            meja_id (int, optional): ID meja. Default None.
            tanggal_pemesanan (str, optional): Tanggal pemesanan. Default None.
            jumlah_orang (int, optional): Jumlah orang. Default 1.
            status (str, optional): Status pemesanan. Default 'pending'.
            catatan (str, optional): Catatan tambahan. Default "".
        """
        super().__init__(id)
        self.pelanggan_id = pelanggan_id
        self.meja_id = meja_id
        self.tanggal_pemesanan = tanggal_pemesanan or datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.jumlah_orang = jumlah_orang
        self.status = status
        self.catatan = catatan
    
    def display_info(self):
        """
        Override method dari BaseEntity untuk menampilkan info pemesanan.
        Implementasi polymorphism.
        
        Returns:
            str: Informasi lengkap pemesanan
        """
        return (f"Pemesanan ID: {self.id}\n"
                f"Pelanggan ID: {self.pelanggan_id}\n"
                f"Meja ID: {self.meja_id}\n"
                f"Tanggal: {self.tanggal_pemesanan}\n"
                f"Jumlah Orang: {self.jumlah_orang}\n"
                f"Status: {self.status}\n"
                f"Catatan: {self.catatan}")
    
    def update_status(self, new_status):
        """
        Mengupdate status pemesanan.
        
        Args:
            new_status (str): Status baru pemesanan
        
        Returns:
            bool: True jika berhasil, False jika status tidak valid
        """
        valid_status = [self.STATUS_PENDING, self.STATUS_CONFIRMED, 
                       self.STATUS_COMPLETED, self.STATUS_CANCELLED]
        if new_status in valid_status:
            self.status = new_status
            return True
        return False
    
    def validate_data(self):
        """
        Validasi data pemesanan.
        
        Returns:
            tuple: (bool, str) - (valid, pesan error)
        """
        if not self.pelanggan_id:
            return False, "Pelanggan ID tidak boleh kosong"
        
        if not self.meja_id:
            return False, "Meja ID tidak boleh kosong"
        
        if self.jumlah_orang <= 0:
            return False, "Jumlah orang harus lebih dari 0"
        
        valid_status = [self.STATUS_PENDING, self.STATUS_CONFIRMED, 
                       self.STATUS_COMPLETED, self.STATUS_CANCELLED]
        if self.status not in valid_status:
            return False, f"Status harus salah satu dari: {', '.join(valid_status)}"
        
        return True, ""
