"""
Database Manager Module
Module ini menangani koneksi database dan operasi CRUD.
Menggunakan MySQL/MariaDB dengan library mysql-connector-python.
"""

import mysql.connector
from mysql.connector import Error
from typing import Optional, List, Tuple, Any


class DatabaseManager:
    """
    Kelas untuk mengelola koneksi dan operasi database.
    Menyediakan fungsi-fungsi CRUD untuk semua entitas.
    """
    
    def __init__(self, host='localhost', database='restaurant_db', 
                 user='root', password=''):
        """
        Inisialisasi DatabaseManager dengan kredensial database.
        
        Args:
            host (str): Host database. Default 'localhost'.
            database (str): Nama database. Default 'restaurant_db'.
            user (str): Username database. Default 'root'.
            password (str): Password database. Default ''.
        """
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
    
    def connect(self):
        """
        Membuat koneksi ke database MySQL/MariaDB.
        
        Returns:
            bool: True jika berhasil terhubung, False jika gagal
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            
            if self.connection.is_connected():
                return True
            return False
            
        except Error as e:
            print(f"Error saat koneksi ke database: {e}")
            return False
    
    def disconnect(self):
        """
        Menutup koneksi database.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
    
    def create_tables(self):
        """
        Membuat tabel-tabel yang diperlukan dalam database.
        Tabel: pelanggan, meja, pemesanan.
        
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        try:
            cursor = self.connection.cursor()
            
            # Tabel pelanggan
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS pelanggan (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nama VARCHAR(100) NOT NULL,
                    telepon VARCHAR(20) NOT NULL,
                    email VARCHAR(100),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Tabel meja
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS meja (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nomor_meja INT NOT NULL UNIQUE,
                    kapasitas INT NOT NULL,
                    status ENUM('tersedia', 'terisi', 'reserved') DEFAULT 'tersedia',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Tabel pemesanan
            cursor.execute("""
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
                    FOREIGN KEY (meja_id) REFERENCES meja(id) ON DELETE CASCADE
                )
            """)
            
            self.connection.commit()
            cursor.close()
            return True
            
        except Error as e:
            print(f"Error saat membuat tabel: {e}")
            return False
    
    def execute_query(self, query: str, params: Tuple = None, fetch: bool = False) -> Any:
        """
        Mengeksekusi query SQL.
        
        Args:
            query (str): Query SQL yang akan dieksekusi
            params (tuple, optional): Parameter untuk query. Default None.
            fetch (bool, optional): Apakah perlu fetch hasil. Default False.
        
        Returns:
            Any: Hasil query jika fetch=True, None jika fetch=False atau error
        """
        try:
            cursor = self.connection.cursor(dictionary=True)
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            if fetch:
                result = cursor.fetchall()
                cursor.close()
                return result
            else:
                self.connection.commit()
                last_id = cursor.lastrowid
                cursor.close()
                return last_id
                
        except Error as e:
            print(f"Error saat eksekusi query: {e}")
            return None
    
    # ========== CRUD PELANGGAN ==========
    
    def create_pelanggan(self, nama: str, telepon: str, email: str = "") -> Optional[int]:
        """
        Menambahkan pelanggan baru ke database.
        
        Args:
            nama (str): Nama pelanggan
            telepon (str): Nomor telepon
            email (str, optional): Email pelanggan. Default "".
        
        Returns:
            int: ID pelanggan yang baru dibuat, atau None jika gagal
        """
        query = "INSERT INTO pelanggan (nama, telepon, email) VALUES (%s, %s, %s)"
        return self.execute_query(query, (nama, telepon, email))
    
    def read_pelanggan(self, pelanggan_id: int = None) -> Optional[List[dict]]:
        """
        Membaca data pelanggan dari database.
        
        Args:
            pelanggan_id (int, optional): ID pelanggan spesifik. Default None (semua pelanggan).
        
        Returns:
            list: List dictionary berisi data pelanggan, atau None jika gagal
        """
        if pelanggan_id:
            query = "SELECT * FROM pelanggan WHERE id = %s"
            return self.execute_query(query, (pelanggan_id,), fetch=True)
        else:
            query = "SELECT * FROM pelanggan ORDER BY id DESC"
            return self.execute_query(query, fetch=True)
    
    def update_pelanggan(self, pelanggan_id: int, nama: str, telepon: str, email: str) -> bool:
        """
        Mengupdate data pelanggan.
        
        Args:
            pelanggan_id (int): ID pelanggan yang akan diupdate
            nama (str): Nama baru
            telepon (str): Nomor telepon baru
            email (str): Email baru
        
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        query = "UPDATE pelanggan SET nama = %s, telepon = %s, email = %s WHERE id = %s"
        result = self.execute_query(query, (nama, telepon, email, pelanggan_id))
        return result is not None
    
    def delete_pelanggan(self, pelanggan_id: int) -> bool:
        """
        Menghapus pelanggan dari database.
        
        Args:
            pelanggan_id (int): ID pelanggan yang akan dihapus
        
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        query = "DELETE FROM pelanggan WHERE id = %s"
        result = self.execute_query(query, (pelanggan_id,))
        return result is not None
    
    # ========== CRUD MEJA ==========
    
    def create_meja(self, nomor_meja: int, kapasitas: int, status: str = 'tersedia') -> Optional[int]:
        """
        Menambahkan meja baru ke database.
        
        Args:
            nomor_meja (int): Nomor meja
            kapasitas (int): Kapasitas meja
            status (str, optional): Status meja. Default 'tersedia'.
        
        Returns:
            int: ID meja yang baru dibuat, atau None jika gagal
        """
        query = "INSERT INTO meja (nomor_meja, kapasitas, status) VALUES (%s, %s, %s)"
        return self.execute_query(query, (nomor_meja, kapasitas, status))
    
    def read_meja(self, meja_id: int = None, status: str = None) -> Optional[List[dict]]:
        """
        Membaca data meja dari database.
        
        Args:
            meja_id (int, optional): ID meja spesifik. Default None.
            status (str, optional): Filter berdasarkan status. Default None.
        
        Returns:
            list: List dictionary berisi data meja, atau None jika gagal
        """
        if meja_id:
            query = "SELECT * FROM meja WHERE id = %s"
            return self.execute_query(query, (meja_id,), fetch=True)
        elif status:
            query = "SELECT * FROM meja WHERE status = %s ORDER BY nomor_meja"
            return self.execute_query(query, (status,), fetch=True)
        else:
            query = "SELECT * FROM meja ORDER BY nomor_meja"
            return self.execute_query(query, fetch=True)
    
    def update_meja(self, meja_id: int, nomor_meja: int, kapasitas: int, status: str) -> bool:
        """
        Mengupdate data meja.
        
        Args:
            meja_id (int): ID meja yang akan diupdate
            nomor_meja (int): Nomor meja baru
            kapasitas (int): Kapasitas baru
            status (str): Status baru
        
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        query = "UPDATE meja SET nomor_meja = %s, kapasitas = %s, status = %s WHERE id = %s"
        result = self.execute_query(query, (nomor_meja, kapasitas, status, meja_id))
        return result is not None
    
    def update_meja_status(self, meja_id: int, status: str) -> bool:
        """
        Mengupdate status meja saja.
        
        Args:
            meja_id (int): ID meja
            status (str): Status baru
        
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        query = "UPDATE meja SET status = %s WHERE id = %s"
        result = self.execute_query(query, (status, meja_id))
        return result is not None
    
    def delete_meja(self, meja_id: int) -> bool:
        """
        Menghapus meja dari database.
        
        Args:
            meja_id (int): ID meja yang akan dihapus
        
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        query = "DELETE FROM meja WHERE id = %s"
        result = self.execute_query(query, (meja_id,))
        return result is not None
    
    # ========== CRUD PEMESANAN ==========
    
    def create_pemesanan(self, pelanggan_id: int, meja_id: int, 
                        tanggal_pemesanan: str, jumlah_orang: int,
                        status: str = 'pending', catatan: str = "") -> Optional[int]:
        """
        Menambahkan pemesanan baru ke database.
        
        Args:
            pelanggan_id (int): ID pelanggan
            meja_id (int): ID meja
            tanggal_pemesanan (str): Tanggal dan waktu pemesanan
            jumlah_orang (int): Jumlah orang
            status (str, optional): Status pemesanan. Default 'pending'.
            catatan (str, optional): Catatan tambahan. Default "".
        
        Returns:
            int: ID pemesanan yang baru dibuat, atau None jika gagal
        """
        query = """INSERT INTO pemesanan 
                   (pelanggan_id, meja_id, tanggal_pemesanan, jumlah_orang, status, catatan) 
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        return self.execute_query(query, (pelanggan_id, meja_id, tanggal_pemesanan, 
                                         jumlah_orang, status, catatan))
    
    def read_pemesanan(self, pemesanan_id: int = None, status: str = None) -> Optional[List[dict]]:
        """
        Membaca data pemesanan dari database dengan JOIN ke tabel pelanggan dan meja.
        
        Args:
            pemesanan_id (int, optional): ID pemesanan spesifik. Default None.
            status (str, optional): Filter berdasarkan status. Default None.
        
        Returns:
            list: List dictionary berisi data pemesanan, atau None jika gagal
        """
        base_query = """
            SELECT p.*, pel.nama as nama_pelanggan, pel.telepon, 
                   m.nomor_meja, m.kapasitas
            FROM pemesanan p
            JOIN pelanggan pel ON p.pelanggan_id = pel.id
            JOIN meja m ON p.meja_id = m.id
        """
        
        if pemesanan_id:
            query = base_query + " WHERE p.id = %s"
            return self.execute_query(query, (pemesanan_id,), fetch=True)
        elif status:
            query = base_query + " WHERE p.status = %s ORDER BY p.tanggal_pemesanan DESC"
            return self.execute_query(query, (status,), fetch=True)
        else:
            query = base_query + " ORDER BY p.tanggal_pemesanan DESC"
            return self.execute_query(query, fetch=True)
    
    def update_pemesanan(self, pemesanan_id: int, pelanggan_id: int, meja_id: int,
                        tanggal_pemesanan: str, jumlah_orang: int, 
                        status: str, catatan: str) -> bool:
        """
        Mengupdate data pemesanan.
        
        Args:
            pemesanan_id (int): ID pemesanan yang akan diupdate
            pelanggan_id (int): ID pelanggan
            meja_id (int): ID meja
            tanggal_pemesanan (str): Tanggal pemesanan
            jumlah_orang (int): Jumlah orang
            status (str): Status pemesanan
            catatan (str): Catatan
        
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        query = """UPDATE pemesanan 
                   SET pelanggan_id = %s, meja_id = %s, tanggal_pemesanan = %s,
                       jumlah_orang = %s, status = %s, catatan = %s
                   WHERE id = %s"""
        result = self.execute_query(query, (pelanggan_id, meja_id, tanggal_pemesanan,
                                           jumlah_orang, status, catatan, pemesanan_id))
        return result is not None
    
    def update_pemesanan_status(self, pemesanan_id: int, status: str) -> bool:
        """
        Mengupdate status pemesanan saja.
        
        Args:
            pemesanan_id (int): ID pemesanan
            status (str): Status baru
        
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        query = "UPDATE pemesanan SET status = %s WHERE id = %s"
        result = self.execute_query(query, (status, pemesanan_id))
        return result is not None
    
    def delete_pemesanan(self, pemesanan_id: int) -> bool:
        """
        Menghapus pemesanan dari database.
        
        Args:
            pemesanan_id (int): ID pemesanan yang akan dihapus
        
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        query = "DELETE FROM pemesanan WHERE id = %s"
        result = self.execute_query(query, (pemesanan_id,))
        return result is not None
    
    # ========== LAPORAN ==========
    
    def get_laporan_pemesanan(self, status: str = None, tanggal_mulai: str = None, 
                              tanggal_akhir: str = None) -> Optional[List[dict]]:
        """
        Mendapatkan laporan pemesanan dengan filter.
        
        Args:
            status (str, optional): Filter status pemesanan. Default None.
            tanggal_mulai (str, optional): Filter tanggal mulai (YYYY-MM-DD). Default None.
            tanggal_akhir (str, optional): Filter tanggal akhir (YYYY-MM-DD). Default None.
        
        Returns:
            list: List dictionary berisi data laporan, atau None jika gagal
        """
        query = """
            SELECT p.*, pel.nama as nama_pelanggan, pel.telepon, 
                   m.nomor_meja, m.kapasitas
            FROM pemesanan p
            JOIN pelanggan pel ON p.pelanggan_id = pel.id
            JOIN meja m ON p.meja_id = m.id
            WHERE 1=1
        """
        
        params = []
        
        # Tambahkan filter status jika ada
        if status:
            query += " AND p.status = %s"
            params.append(status)
        
        # Tambahkan filter tanggal jika ada
        if tanggal_mulai:
            query += " AND DATE(p.tanggal_pemesanan) >= %s"
            params.append(tanggal_mulai)
        
        if tanggal_akhir:
            query += " AND DATE(p.tanggal_pemesanan) <= %s"
            params.append(tanggal_akhir)
        
        query += " ORDER BY p.tanggal_pemesanan DESC"
        
        if params:
            return self.execute_query(query, tuple(params), fetch=True)
        else:
            return self.execute_query(query, fetch=True)
