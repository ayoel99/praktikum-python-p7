import unittest

from akademik import hitung_ipk, konversi_nilai_huruf, validasi_nim


class TestHitungIPK(unittest.TestCase):
    def test_normal(self):
        nilai = [
            {"bobot": 4.0, "sks": 3},
            {"bobot": 3.0, "sks": 2},
            {"bobot": 3.7, "sks": 3},
        ]
        self.assertAlmostEqual(hitung_ipk(nilai), 3.6375)

    def test_list_kosong(self):
        self.assertEqual(hitung_ipk([]), 0.0)

    def test_total_sks_nol(self):
        self.assertEqual(hitung_ipk([{"bobot": 4.0, "sks": 0}]), 0.0)


class TestValidasiNIM(unittest.TestCase):
    def test_benar(self):
        self.assertTrue(validasi_nim("2021001234"))

    def test_ada_huruf(self):
        self.assertFalse(validasi_nim("2021AB1234"))

    def test_kurang_digit(self):
        self.assertFalse(validasi_nim("202100123"))

    def test_bukan_string(self):
        self.assertFalse(validasi_nim(2021001234))


class TestKonversiNilai(unittest.TestCase):
    def test_happy_path(self):
        self.assertEqual(konversi_nilai_huruf(90), "A")
        self.assertEqual(konversi_nilai_huruf(77), "B+")

    def test_batas(self):
        self.assertEqual(konversi_nilai_huruf(85), "A")
        self.assertEqual(konversi_nilai_huruf(0), "E")
        self.assertEqual(konversi_nilai_huruf(100), "A")

    def test_tidak_valid(self):
        with self.assertRaises(ValueError):
            konversi_nilai_huruf(101)
        with self.assertRaises(ValueError):
            konversi_nilai_huruf(-1)
        with self.assertRaises(ValueError):
            konversi_nilai_huruf("A")


if __name__ == "__main__":
    unittest.main()