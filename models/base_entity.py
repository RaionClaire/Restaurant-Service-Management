"""
Base Entity Module
Module ini berisi kelas dasar untuk semua entitas dalam sistem.
"""


class BaseEntity:
    """
    Kelas dasar untuk semua entitas dalam sistem.
    Menyediakan atribut dan metode umum yang dapat diwarisi.
    
    Attributes:
        id (int): ID unik untuk entitas
        created_at (str): Waktu pembuatan entitas
    """
    
    def __init__(self, id=None):
        """
        Inisialisasi BaseEntity.
        
        Args:
            id (int, optional): ID unik entitas. Default None.
        """
        self.id = id
        self.created_at = None
    
    def get_id(self):
        """
        Mendapatkan ID entitas.
        
        Returns:
            int: ID entitas
        """
        return self.id
    
    def set_id(self, id):
        """
        Mengatur ID entitas.
        
        Args:
            id (int): ID baru untuk entitas
        """
        self.id = id
    
    def display_info(self):
        """
        Menampilkan informasi entitas (polymorphic method).
        Method ini akan di-override oleh kelas turunan.
        
        Returns:
            str: Informasi entitas
        """
        return f"Entity ID: {self.id}"
