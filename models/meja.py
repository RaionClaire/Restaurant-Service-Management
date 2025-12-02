"""
Meja Module
Module ini berisi kelas Meja yang mewarisi dari BaseEntity.
"""

from .base_entity import BaseEntity


class Meja(BaseEntity):
    """
    Kelas untuk merepresentasikan meja di restoran.
    Mewarisi dari BaseEntity dan menambahkan atribut khusus meja.
    
    Attributes:
        nomor_meja (int): Nomor meja
        kapasitas (int): Kapasitas maksimal orang yang dapat duduk
        status (str): Status meja ('tersedia', 'terisi', 'reserved')
    """
    
    # Konstanta untuk status meja
    STATUS_TERSEDIA = 'tersedia'
    STATUS_TERISI = 'terisi'
    STATUS_RESERVED = 'reserved'
    
    def __init__(self, id=None, nomor_meja=0, kapasitas=4, status=STATUS_TERSEDIA):
        """
        Inisialisasi objek Meja.
        
        Args:
            id (int, optional): ID meja. Default None.
            nomor_meja (int, optional): Nomor meja. Default 0.
            kapasitas (int, optional): Kapasitas meja. Default 4.
            status (str, optional): Status meja. Default 'tersedia'.
        """
        super().__init__(id)
        self.nomor_meja = nomor_meja
        self.kapasitas = kapasitas
        self.status = status
    
    def display_info(self):
        """
        Override method dari BaseEntity untuk menampilkan info meja.
        Implementasi polymorphism.
        
        Returns:
            str: Informasi lengkap meja
        """
        return (f"Meja ID: {self.id}\n"
                f"Nomor Meja: {self.nomor_meja}\n"
                f"Kapasitas: {self.kapasitas} orang\n"
                f"Status: {self.status}")
    
    def is_tersedia(self):
        """
        Memeriksa apakah meja tersedia.
        
        Returns:
            bool: True jika tersedia, False jika tidak
        """
        return self.status == self.STATUS_TERSEDIA
    
    def set_status(self, status):
        """
        Mengatur status meja.
        
        Args:
            status (str): Status baru ('tersedia', 'terisi', 'reserved')
        
        Returns:
            bool: True jika berhasil, False jika status tidak valid
        """
        valid_status = [self.STATUS_TERSEDIA, self.STATUS_TERISI, self.STATUS_RESERVED]
        if status in valid_status:
            self.status = status
            return True
        return False
    
    def validate_data(self):
        """
        Validasi data meja dengan exception handling.
        
        Returns:
            tuple: (bool, str) - (valid, pesan error)
        
        Raises:
            ValueError: Jika data tidak valid
        """
        # Validasi nomor meja harus positif
        if self.nomor_meja <= 0:
            return False, "Nomor meja harus lebih dari 0"
        
        # Validasi nomor meja tidak boleh terlalu besar
        if self.nomor_meja > 999:
            return False, "Nomor meja tidak boleh lebih dari 999"
        
        # Validasi kapasitas harus positif
        if self.kapasitas <= 0:
            return False, "Kapasitas harus lebih dari 0"
        
        # Validasi kapasitas wajar (minimal 1, maksimal 20 orang)
        if self.kapasitas > 20:
            return False, "Kapasitas meja tidak boleh lebih dari 20 orang"
        
        # Validasi status harus valid
        valid_status = [self.STATUS_TERSEDIA, self.STATUS_TERISI, self.STATUS_RESERVED]
        if self.status not in valid_status:
            return False, f"Status harus salah satu dari: {', '.join(valid_status)}"
        
        return True, ""
