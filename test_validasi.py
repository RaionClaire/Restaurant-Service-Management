"""
Script untuk testing validasi input
Menguji semua aturan validasi yang baru ditambahkan
"""

from models.pelanggan import Pelanggan
from models.meja import Meja
from models.pemesanan import Pemesanan


def test_pelanggan_validasi():
    """Test validasi pelanggan"""
    print("\n" + "="*70)
    print("TEST VALIDASI PELANGGAN")
    print("="*70)
    
    # Test 1: Nama dengan angka (HARUS GAGAL)
    print("\n1. Test nama dengan angka:")
    p1 = Pelanggan(nama="John123", telepon="081234567890", email="john@test.com")
    valid, msg = p1.validate_data()
    print(f"   Nama: {p1.nama}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert not valid, "Seharusnya gagal karena nama mengandung angka"
    
    # Test 2: Nama terlalu pendek (HARUS GAGAL)
    print("\n2. Test nama terlalu pendek:")
    p2 = Pelanggan(nama="A", telepon="081234567890", email="john@test.com")
    valid, msg = p2.validate_data()
    print(f"   Nama: {p2.nama}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert not valid, "Seharusnya gagal karena nama kurang dari 2 karakter"
    
    # Test 3: Telepon tidak dimulai dengan 628/08/+628 (HARUS GAGAL)
    print("\n3. Test telepon format salah:")
    p3 = Pelanggan(nama="John Doe", telepon="123456789", email="john@test.com")
    valid, msg = p3.validate_data()
    print(f"   Telepon: {p3.telepon}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert not valid, "Seharusnya gagal karena format telepon salah"
    
    # Test 4: Telepon terlalu pendek (HARUS GAGAL)
    print("\n4. Test telepon terlalu pendek:")
    p4 = Pelanggan(nama="John Doe", telepon="081234", email="john@test.com")
    valid, msg = p4.validate_data()
    print(f"   Telepon: {p4.telepon}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert not valid, "Seharusnya gagal karena telepon terlalu pendek"
    
    # Test 5: Email tanpa @ (HARUS GAGAL)
    print("\n5. Test email tanpa @:")
    p5 = Pelanggan(nama="John Doe", telepon="081234567890", email="johndomain.com")
    valid, msg = p5.validate_data()
    print(f"   Email: {p5.email}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert not valid, "Seharusnya gagal karena email tidak mengandung @"
    
    # Test 6: Email tanpa titik (HARUS GAGAL)
    print("\n6. Test email tanpa titik:")
    p6 = Pelanggan(nama="John Doe", telepon="081234567890", email="john@domain")
    valid, msg = p6.validate_data()
    print(f"   Email: {p6.email}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert not valid, "Seharusnya gagal karena email tidak mengandung titik di domain"
    
    # Test 7: Data valid dengan format 08 (HARUS BERHASIL)
    print("\n7. Test data valid dengan 08:")
    p7 = Pelanggan(nama="John Doe", telepon="081234567890", email="john@example.com")
    valid, msg = p7.validate_data()
    print(f"   Nama: {p7.nama}, Telepon: {p7.telepon}, Email: {p7.email}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert valid, "Seharusnya berhasil dengan data valid"
    
    # Test 8: Data valid dengan format 628 (HARUS BERHASIL)
    print("\n8. Test data valid dengan 628:")
    p8 = Pelanggan(nama="Ahmad", telepon="6281234567890", email="ahmad@test.co.id")
    valid, msg = p8.validate_data()
    print(f"   Nama: {p8.nama}, Telepon: {p8.telepon}, Email: {p8.email}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert valid, "Seharusnya berhasil dengan data valid"
    
    # Test 9: Data valid dengan format +628 (HARUS BERHASIL)
    print("\n9. Test data valid dengan +628:")
    p9 = Pelanggan(nama="Siti Nurhaliza", telepon="+6281234567890", email="siti@mail.com")
    valid, msg = p9.validate_data()
    print(f"   Nama: {p9.nama}, Telepon: {p9.telepon}, Email: {p9.email}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert valid, "Seharusnya berhasil dengan data valid"
    
    # Test 10: Email kosong (HARUS BERHASIL karena opsional)
    print("\n10. Test email kosong (opsional):")
    p10 = Pelanggan(nama="Budi", telepon="081234567890", email="")
    valid, msg = p10.validate_data()
    print(f"   Nama: {p10.nama}, Telepon: {p10.telepon}, Email: '{p10.email}'")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert valid, "Seharusnya berhasil karena email opsional"
    
    print("\n✅ Semua test validasi pelanggan LULUS!")


def test_meja_validasi():
    """Test validasi meja"""
    print("\n" + "="*70)
    print("TEST VALIDASI MEJA")
    print("="*70)
    
    # Test 1: Nomor meja 0 (HARUS GAGAL)
    print("\n1. Test nomor meja 0:")
    m1 = Meja(nomor_meja=0, kapasitas=4)
    valid, msg = m1.validate_data()
    print(f"   Nomor: {m1.nomor_meja}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert not valid, "Seharusnya gagal karena nomor meja 0"
    
    # Test 2: Nomor meja > 999 (HARUS GAGAL)
    print("\n2. Test nomor meja > 999:")
    m2 = Meja(nomor_meja=1000, kapasitas=4)
    valid, msg = m2.validate_data()
    print(f"   Nomor: {m2.nomor_meja}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert not valid, "Seharusnya gagal karena nomor meja > 999"
    
    # Test 3: Kapasitas 0 (HARUS GAGAL)
    print("\n3. Test kapasitas 0:")
    m3 = Meja(nomor_meja=1, kapasitas=0)
    valid, msg = m3.validate_data()
    print(f"   Kapasitas: {m3.kapasitas}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert not valid, "Seharusnya gagal karena kapasitas 0"
    
    # Test 4: Kapasitas > 20 (HARUS GAGAL)
    print("\n4. Test kapasitas > 20:")
    m4 = Meja(nomor_meja=1, kapasitas=25)
    valid, msg = m4.validate_data()
    print(f"   Kapasitas: {m4.kapasitas}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert not valid, "Seharusnya gagal karena kapasitas > 20"
    
    # Test 5: Status tidak valid (HARUS GAGAL)
    print("\n5. Test status tidak valid:")
    m5 = Meja(nomor_meja=1, kapasitas=4, status="available")
    valid, msg = m5.validate_data()
    print(f"   Status: {m5.status}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert not valid, "Seharusnya gagal karena status tidak valid"
    
    # Test 6: Data valid (HARUS BERHASIL)
    print("\n6. Test data meja valid:")
    m6 = Meja(nomor_meja=5, kapasitas=4, status="tersedia")
    valid, msg = m6.validate_data()
    print(f"   Nomor: {m6.nomor_meja}, Kapasitas: {m6.kapasitas}, Status: {m6.status}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert valid, "Seharusnya berhasil dengan data valid"
    
    # Test 7: Data valid batas atas (HARUS BERHASIL)
    print("\n7. Test data meja valid (batas atas):")
    m7 = Meja(nomor_meja=999, kapasitas=20, status="terisi")
    valid, msg = m7.validate_data()
    print(f"   Nomor: {m7.nomor_meja}, Kapasitas: {m7.kapasitas}, Status: {m7.status}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert valid, "Seharusnya berhasil dengan data valid"
    
    print("\n✅ Semua test validasi meja LULUS!")


def test_pemesanan_validasi():
    """Test validasi pemesanan"""
    print("\n" + "="*70)
    print("TEST VALIDASI PEMESANAN")
    print("="*70)
    
    # Test 1: Pelanggan ID 0 (HARUS GAGAL)
    print("\n1. Test pelanggan ID 0:")
    pm1 = Pemesanan(pelanggan_id=0, meja_id=1, jumlah_orang=4)
    valid, msg = pm1.validate_data()
    print(f"   Pelanggan ID: {pm1.pelanggan_id}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert not valid, "Seharusnya gagal karena pelanggan ID 0"
    
    # Test 2: Meja ID 0 (HARUS GAGAL)
    print("\n2. Test meja ID 0:")
    pm2 = Pemesanan(pelanggan_id=1, meja_id=0, jumlah_orang=4)
    valid, msg = pm2.validate_data()
    print(f"   Meja ID: {pm2.meja_id}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert not valid, "Seharusnya gagal karena meja ID 0"
    
    # Test 3: Jumlah orang 0 (HARUS GAGAL)
    print("\n3. Test jumlah orang 0:")
    pm3 = Pemesanan(pelanggan_id=1, meja_id=1, jumlah_orang=0)
    valid, msg = pm3.validate_data()
    print(f"   Jumlah Orang: {pm3.jumlah_orang}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert not valid, "Seharusnya gagal karena jumlah orang 0"
    
    # Test 4: Jumlah orang > 20 (HARUS GAGAL)
    print("\n4. Test jumlah orang > 20:")
    pm4 = Pemesanan(pelanggan_id=1, meja_id=1, jumlah_orang=25)
    valid, msg = pm4.validate_data()
    print(f"   Jumlah Orang: {pm4.jumlah_orang}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert not valid, "Seharusnya gagal karena jumlah orang > 20"
    
    # Test 5: Format tanggal salah (HARUS GAGAL)
    print("\n5. Test format tanggal salah:")
    pm5 = Pemesanan(pelanggan_id=1, meja_id=1, jumlah_orang=4, 
                    tanggal_pemesanan="2025/12/25 19:00:00")
    valid, msg = pm5.validate_data()
    print(f"   Tanggal: {pm5.tanggal_pemesanan}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert not valid, "Seharusnya gagal karena format tanggal salah"
    
    # Test 6: Catatan terlalu panjang (HARUS GAGAL)
    print("\n6. Test catatan terlalu panjang:")
    pm6 = Pemesanan(pelanggan_id=1, meja_id=1, jumlah_orang=4,
                    catatan="X" * 501)  # 501 karakter
    valid, msg = pm6.validate_data()
    print(f"   Panjang Catatan: {len(pm6.catatan)}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert not valid, "Seharusnya gagal karena catatan > 500 karakter"
    
    # Test 7: Data valid (HARUS BERHASIL)
    print("\n7. Test data pemesanan valid:")
    pm7 = Pemesanan(pelanggan_id=1, meja_id=1, jumlah_orang=4,
                    tanggal_pemesanan="2025-12-25 19:00:00",
                    catatan="Dekat jendela")
    valid, msg = pm7.validate_data()
    print(f"   Pelanggan: {pm7.pelanggan_id}, Meja: {pm7.meja_id}, Orang: {pm7.jumlah_orang}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert valid, "Seharusnya berhasil dengan data valid"
    
    # Test 8: Data valid tanpa catatan (HARUS BERHASIL)
    print("\n8. Test data valid tanpa catatan:")
    pm8 = Pemesanan(pelanggan_id=2, meja_id=3, jumlah_orang=2,
                    tanggal_pemesanan="2025-12-31 20:00:00",
                    catatan="")
    valid, msg = pm8.validate_data()
    print(f"   Pelanggan: {pm8.pelanggan_id}, Meja: {pm8.meja_id}, Orang: {pm8.jumlah_orang}")
    print(f"   Valid: {valid}, Pesan: {msg}")
    assert valid, "Seharusnya berhasil dengan data valid"
    
    print("\n✅ Semua test validasi pemesanan LULUS!")


def main():
    """Menjalankan semua test"""
    print("\n" + "="*70)
    print("TESTING SISTEM VALIDASI INPUT")
    print("="*70)
    
    try:
        test_pelanggan_validasi()
        test_meja_validasi()
        test_pemesanan_validasi()
        
        print("\n" + "="*70)
        print("🎉 SEMUA TEST VALIDASI BERHASIL! 🎉")
        print("="*70)
        print("\n✓ Validasi nama pelanggan: OK")
        print("✓ Validasi nomor telepon: OK")
        print("✓ Validasi email: OK")
        print("✓ Validasi nomor meja: OK")
        print("✓ Validasi kapasitas meja: OK")
        print("✓ Validasi status meja: OK")
        print("✓ Validasi ID pemesanan: OK")
        print("✓ Validasi jumlah orang: OK")
        print("✓ Validasi format tanggal: OK")
        print("✓ Validasi catatan: OK")
        print("\nSistem validasi siap digunakan!")
        
    except AssertionError as e:
        print(f"\n❌ TEST GAGAL: {e}")
        return False
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True


if __name__ == "__main__":
    main()
