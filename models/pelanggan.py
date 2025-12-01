"""
Pelanggan Module
Module ini berisi kelas Pelanggan yang mewarisi dari BaseEntity.
"""

from .base_entity import BaseEntity


class Pelanggan(BaseEntity):
    """
    Kelas untuk merepresentasikan pelanggan restoran.
    Mewarisi dari BaseEntity dan menambahkan atribut khusus pelanggan.
    
    Attributes:
        nama (str): Nama pelanggan
        telepon (str): Nomor telepon pelanggan
        email (str): Email pelanggan
    """
    
    def __init__(self, id=None, nama="", telepon="", email=""):
        """
        Inisialisasi objek Pelanggan.
        
        Args:
            id (int, optional): ID pelanggan. Default None.
            nama (str, optional): Nama pelanggan. Default "".
            telepon (str, optional): Nomor telepon. Default "".
            email (str, optional): Email pelanggan. Default "".
        """
        super().__init__(id)
        self.nama = nama
        self.telepon = telepon
        self.email = email
    
    def display_info(self):
        """
        Override method dari BaseEntity untuk menampilkan info pelanggan.
        Implementasi polymorphism.
        
        Returns:
            str: Informasi lengkap pelanggan
        """
        return (f"Pelanggan ID: {self.id}\n"
                f"Nama: {self.nama}\n"
                f"Telepon: {self.telepon}\n"
                f"Email: {self.email}")
    
    def get_nama(self):
        """
        Mendapatkan nama pelanggan.
        
        Returns:
            str: Nama pelanggan
        """
        return self.nama
    
    def set_nama(self, nama):
        """
        Mengatur nama pelanggan.
        
        Args:
            nama (str): Nama baru pelanggan
        """
        self.nama = nama
    
    def validate_data(self):
        """
        Validasi data pelanggan.
        
        Returns:
            tuple: (bool, str) - (valid, pesan error)
        """
        if not self.nama or len(self.nama.strip()) == 0:
            return False, "Nama pelanggan tidak boleh kosong"
        
        if not self.telepon or len(self.telepon.strip()) == 0:
            return False, "Telepon tidak boleh kosong"
        
        return True, ""
