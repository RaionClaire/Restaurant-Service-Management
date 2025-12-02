"""
Pelanggan Module
Module ini berisi kelas Pelanggan yang mewarisi dari BaseEntity.
"""

import re
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
        Validasi data pelanggan dengan exception handling.
        
        Returns:
            tuple: (bool, str) - (valid, pesan error)
        
        Raises:
            ValueError: Jika data tidak valid
        """
        # Validasi nama tidak boleh kosong
        if not self.nama or len(self.nama.strip()) == 0:
            return False, "Nama pelanggan tidak boleh kosong"
        
        # Validasi nama tidak boleh mengandung angka
        if re.search(r'\d', self.nama):
            return False, "Nama pelanggan tidak boleh mengandung angka"
        
        # Validasi nama minimal 2 karakter
        if len(self.nama.strip()) < 2:
            return False, "Nama pelanggan minimal 2 karakter"
        
        # Validasi telepon tidak boleh kosong
        if not self.telepon or len(self.telepon.strip()) == 0:
            return False, "Nomor telepon tidak boleh kosong"
        
        # Hapus spasi dan karakter non-digit dari telepon untuk validasi
        telepon_clean = re.sub(r'[\s\-\(\)]', '', self.telepon)
        
        # Validasi format telepon harus dimulai dengan 628, 08, atau +628
        if not (telepon_clean.startswith('628') or 
                telepon_clean.startswith('08') or 
                telepon_clean.startswith('+628')):
            return False, "Nomor telepon harus dimulai dengan 628, 08, atau +628"
        
        # Validasi telepon harus berisi hanya angka (setelah menghapus +)
        telepon_digits = telepon_clean.replace('+', '')
        if not telepon_digits.isdigit():
            return False, "Nomor telepon hanya boleh berisi angka"
        
        # Validasi panjang telepon (minimal 10 digit, maksimal 15 digit)
        if len(telepon_digits) < 10 or len(telepon_digits) > 15:
            return False, "Nomor telepon harus antara 10-15 digit"
        
        # Validasi email jika diisi
        if self.email and len(self.email.strip()) > 0:
            # Email harus mengandung @ dan .
            if '@' not in self.email or '.' not in self.email:
                return False, "Email harus mengandung karakter @ dan . (titik)"
            
            # Validasi format email menggunakan regex
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, self.email):
                return False, "Format email tidak valid (contoh: nama@domain.com)"
            
            # Validasi @ tidak boleh di awal atau akhir
            if self.email.startswith('@') or self.email.endswith('@'):
                return False, "Karakter @ tidak boleh di awal atau akhir email"
            
            # Validasi hanya boleh ada satu @
            if self.email.count('@') != 1:
                return False, "Email hanya boleh mengandung satu karakter @"
            
            # Validasi bagian setelah @ harus ada titik
            email_parts = self.email.split('@')
            if len(email_parts) == 2 and '.' not in email_parts[1]:
                return False, "Domain email harus mengandung titik (.)"
        
        return True, ""
