"""
Unit Tests untuk Sistem Pemesanan Restoran
Module ini berisi pengujian unit untuk semua komponen sistem.
"""

import unittest
from models.pelanggan import Pelanggan
from models.meja import Meja
from models.pemesanan import Pemesanan
from datetime import datetime


class TestPelanggan(unittest.TestCase):
    """
    Test case untuk kelas Pelanggan.
    Menguji validasi data dan method-method pelanggan.
    """
    
    def setUp(self):
        """Setup sebelum setiap test dijalankan."""
        self.pelanggan = Pelanggan(
            id=1,
            nama="John Doe",
            telepon="081234567890",
            email="john@example.com"
        )
    
    def test_create_pelanggan(self):
        """Test pembuatan objek pelanggan."""
        self.assertEqual(self.pelanggan.id, 1)
        self.assertEqual(self.pelanggan.nama, "John Doe")
        self.assertEqual(self.pelanggan.telepon, "081234567890")
        self.assertEqual(self.pelanggan.email, "john@example.com")
    
    def test_display_info(self):
        """Test method display_info (polymorphism)."""
        info = self.pelanggan.display_info()
        self.assertIn("John Doe", info)
        self.assertIn("081234567890", info)
    
    def test_validate_data_success(self):
        """Test validasi data pelanggan yang benar."""
        is_valid, error_msg = self.pelanggan.validate_data()
        self.assertTrue(is_valid)
        self.assertEqual(error_msg, "")
    
    def test_validate_data_empty_nama(self):
        """Test validasi dengan nama kosong."""
        pelanggan = Pelanggan(nama="", telepon="081234567890")
        is_valid, error_msg = pelanggan.validate_data()
        self.assertFalse(is_valid)
        self.assertIn("Nama", error_msg)
    
    def test_validate_data_empty_telepon(self):
        """Test validasi dengan telepon kosong."""
        pelanggan = Pelanggan(nama="John", telepon="")
        is_valid, error_msg = pelanggan.validate_data()
        self.assertFalse(is_valid)
        self.assertIn("Telepon", error_msg)
    
    def test_get_set_nama(self):
        """Test getter dan setter nama."""
        self.pelanggan.set_nama("Jane Doe")
        self.assertEqual(self.pelanggan.get_nama(), "Jane Doe")


class TestMeja(unittest.TestCase):
    """
    Test case untuk kelas Meja.
    Menguji validasi data dan method-method meja.
    """
    
    def setUp(self):
        """Setup sebelum setiap test dijalankan."""
        self.meja = Meja(
            id=1,
            nomor_meja=5,
            kapasitas=4,
            status='tersedia'
        )
    
    def test_create_meja(self):
        """Test pembuatan objek meja."""
        self.assertEqual(self.meja.id, 1)
        self.assertEqual(self.meja.nomor_meja, 5)
        self.assertEqual(self.meja.kapasitas, 4)
        self.assertEqual(self.meja.status, 'tersedia')
    
    def test_display_info(self):
        """Test method display_info (polymorphism)."""
        info = self.meja.display_info()
        self.assertIn("5", info)
        self.assertIn("4", info)
        self.assertIn("tersedia", info)
    
    def test_is_tersedia(self):
        """Test method is_tersedia."""
        self.assertTrue(self.meja.is_tersedia())
        
        self.meja.status = 'terisi'
        self.assertFalse(self.meja.is_tersedia())
    
    def test_set_status_valid(self):
        """Test set status dengan nilai yang valid."""
        result = self.meja.set_status('terisi')
        self.assertTrue(result)
        self.assertEqual(self.meja.status, 'terisi')
    
    def test_set_status_invalid(self):
        """Test set status dengan nilai yang tidak valid."""
        result = self.meja.set_status('invalid_status')
        self.assertFalse(result)
        self.assertEqual(self.meja.status, 'tersedia')  # Status tetap sama
    
    def test_validate_data_success(self):
        """Test validasi data meja yang benar."""
        is_valid, error_msg = self.meja.validate_data()
        self.assertTrue(is_valid)
        self.assertEqual(error_msg, "")
    
    def test_validate_data_invalid_nomor(self):
        """Test validasi dengan nomor meja tidak valid."""
        meja = Meja(nomor_meja=0, kapasitas=4)
        is_valid, error_msg = meja.validate_data()
        self.assertFalse(is_valid)
        self.assertIn("Nomor meja", error_msg)
    
    def test_validate_data_invalid_kapasitas(self):
        """Test validasi dengan kapasitas tidak valid."""
        meja = Meja(nomor_meja=5, kapasitas=0)
        is_valid, error_msg = meja.validate_data()
        self.assertFalse(is_valid)
        self.assertIn("Kapasitas", error_msg)
    
    def test_validate_data_invalid_status(self):
        """Test validasi dengan status tidak valid."""
        meja = Meja(nomor_meja=5, kapasitas=4, status='invalid')
        is_valid, error_msg = meja.validate_data()
        self.assertFalse(is_valid)
        self.assertIn("Status", error_msg)


class TestPemesanan(unittest.TestCase):
    """
    Test case untuk kelas Pemesanan.
    Menguji validasi data dan method-method pemesanan.
    """
    
    def setUp(self):
        """Setup sebelum setiap test dijalankan."""
        self.pemesanan = Pemesanan(
            id=1,
            pelanggan_id=1,
            meja_id=1,
            tanggal_pemesanan="2025-12-01 19:00:00",
            jumlah_orang=4,
            status='pending',
            catatan="Mohon tempat dekat jendela"
        )
    
    def test_create_pemesanan(self):
        """Test pembuatan objek pemesanan."""
        self.assertEqual(self.pemesanan.id, 1)
        self.assertEqual(self.pemesanan.pelanggan_id, 1)
        self.assertEqual(self.pemesanan.meja_id, 1)
        self.assertEqual(self.pemesanan.jumlah_orang, 4)
        self.assertEqual(self.pemesanan.status, 'pending')
    
    def test_display_info(self):
        """Test method display_info (polymorphism)."""
        info = self.pemesanan.display_info()
        self.assertIn("1", info)
        self.assertIn("4", info)
        self.assertIn("pending", info)
    
    def test_update_status_valid(self):
        """Test update status dengan nilai yang valid."""
        result = self.pemesanan.update_status('confirmed')
        self.assertTrue(result)
        self.assertEqual(self.pemesanan.status, 'confirmed')
    
    def test_update_status_invalid(self):
        """Test update status dengan nilai yang tidak valid."""
        result = self.pemesanan.update_status('invalid_status')
        self.assertFalse(result)
        self.assertEqual(self.pemesanan.status, 'pending')  # Status tetap sama
    
    def test_validate_data_success(self):
        """Test validasi data pemesanan yang benar."""
        is_valid, error_msg = self.pemesanan.validate_data()
        self.assertTrue(is_valid)
        self.assertEqual(error_msg, "")
    
    def test_validate_data_missing_pelanggan(self):
        """Test validasi tanpa pelanggan_id."""
        pemesanan = Pemesanan(pelanggan_id=None, meja_id=1, jumlah_orang=2)
        is_valid, error_msg = pemesanan.validate_data()
        self.assertFalse(is_valid)
        self.assertIn("Pelanggan", error_msg)
    
    def test_validate_data_missing_meja(self):
        """Test validasi tanpa meja_id."""
        pemesanan = Pemesanan(pelanggan_id=1, meja_id=None, jumlah_orang=2)
        is_valid, error_msg = pemesanan.validate_data()
        self.assertFalse(is_valid)
        self.assertIn("Meja", error_msg)
    
    def test_validate_data_invalid_jumlah_orang(self):
        """Test validasi dengan jumlah orang tidak valid."""
        pemesanan = Pemesanan(pelanggan_id=1, meja_id=1, jumlah_orang=0)
        is_valid, error_msg = pemesanan.validate_data()
        self.assertFalse(is_valid)
        self.assertIn("Jumlah orang", error_msg)
    
    def test_validate_data_invalid_status(self):
        """Test validasi dengan status tidak valid."""
        pemesanan = Pemesanan(
            pelanggan_id=1, 
            meja_id=1, 
            jumlah_orang=2, 
            status='invalid'
        )
        is_valid, error_msg = pemesanan.validate_data()
        self.assertFalse(is_valid)
        self.assertIn("Status", error_msg)
    
    def test_default_tanggal_pemesanan(self):
        """Test default tanggal pemesanan menggunakan waktu sekarang."""
        pemesanan = Pemesanan(pelanggan_id=1, meja_id=1, jumlah_orang=2)
        self.assertIsNotNone(pemesanan.tanggal_pemesanan)
        # Cek apakah tanggal pemesanan adalah hari ini
        today = datetime.now().strftime('%Y-%m-%d')
        self.assertIn(today, pemesanan.tanggal_pemesanan)


class TestInheritance(unittest.TestCase):
    """
    Test case untuk menguji inheritance dari BaseEntity.
    """
    
    def test_pelanggan_inheritance(self):
        """Test bahwa Pelanggan mewarisi dari BaseEntity."""
        from models.base_entity import BaseEntity
        pelanggan = Pelanggan(id=1, nama="Test")
        self.assertIsInstance(pelanggan, BaseEntity)
        self.assertTrue(hasattr(pelanggan, 'get_id'))
        self.assertTrue(hasattr(pelanggan, 'set_id'))
    
    def test_meja_inheritance(self):
        """Test bahwa Meja mewarisi dari BaseEntity."""
        from models.base_entity import BaseEntity
        meja = Meja(id=1, nomor_meja=5, kapasitas=4)
        self.assertIsInstance(meja, BaseEntity)
        self.assertTrue(hasattr(meja, 'get_id'))
        self.assertTrue(hasattr(meja, 'set_id'))
    
    def test_pemesanan_inheritance(self):
        """Test bahwa Pemesanan mewarisi dari BaseEntity."""
        from models.base_entity import BaseEntity
        pemesanan = Pemesanan(id=1, pelanggan_id=1, meja_id=1, jumlah_orang=2)
        self.assertIsInstance(pemesanan, BaseEntity)
        self.assertTrue(hasattr(pemesanan, 'get_id'))
        self.assertTrue(hasattr(pemesanan, 'set_id'))


class TestPolymorphism(unittest.TestCase):
    """
    Test case untuk menguji polymorphism.
    """
    
    def test_polymorphic_display_info(self):
        """
        Test bahwa setiap kelas mengimplementasikan display_info secara berbeda.
        Ini adalah demonstrasi polymorphism.
        """
        pelanggan = Pelanggan(id=1, nama="John", telepon="081234567890")
        meja = Meja(id=1, nomor_meja=5, kapasitas=4)
        pemesanan = Pemesanan(id=1, pelanggan_id=1, meja_id=1, jumlah_orang=2)
        
        # Semua objek memiliki method display_info
        entities = [pelanggan, meja, pemesanan]
        
        for entity in entities:
            info = entity.display_info()
            self.assertIsInstance(info, str)
            self.assertGreater(len(info), 0)
        
        # Namun output-nya berbeda sesuai tipe objek
        self.assertIn("John", pelanggan.display_info())
        self.assertIn("5", meja.display_info())
        self.assertIn("2", pemesanan.display_info())


def run_tests():
    """
    Menjalankan semua unit tests dan menampilkan hasilnya.
    
    Returns:
        unittest.TestResult: Hasil dari pengujian
    """
    # Buat test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Tambahkan semua test classes
    suite.addTests(loader.loadTestsFromTestCase(TestPelanggan))
    suite.addTests(loader.loadTestsFromTestCase(TestMeja))
    suite.addTests(loader.loadTestsFromTestCase(TestPemesanan))
    suite.addTests(loader.loadTestsFromTestCase(TestInheritance))
    suite.addTests(loader.loadTestsFromTestCase(TestPolymorphism))
    
    # Jalankan tests dengan verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Tampilkan summary
    print("\n" + "="*70)
    print("SUMMARY HASIL PENGUJIAN")
    print("="*70)
    print(f"Total Tests: {result.testsRun}")
    print(f"Berhasil: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Gagal: {len(result.failures)}")
    print(f"Error: {len(result.errors)}")
    print("="*70)
    
    return result


if __name__ == '__main__':
    run_tests()
