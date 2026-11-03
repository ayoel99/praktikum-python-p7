class PerpustakaanError(Exception):
    """Base exception sistem perpustakaan."""


class BukuNotFoundError(PerpustakaanError):
    def __init__(self, kode):
        self.kode = kode
        super().__init__(f"Buku dengan kode '{kode}' tidak ditemukan")


class BukuTidakTersediaError(PerpustakaanError):
    def __init__(self, judul):
        self.judul = judul
        super().__init__(f"Buku '{judul}' sedang dipinjam")


class AnggotaNotFoundError(PerpustakaanError):
    def __init__(self, id_anggota):
        self.id_anggota = id_anggota
        super().__init__(f"Anggota '{id_anggota}' tidak terdaftar")


BUKU = {
    "B001": {"judul": "Pemrograman Python", "tersedia": True},
    "B002": {"judul": "Basis Data", "tersedia": False},
}
ANGGOTA = {"A01": "Devina", "A02": "Khanaya"}


def pinjam_buku(id_anggota, kode_buku):
    if id_anggota not in ANGGOTA:
        raise AnggotaNotFoundError(id_anggota)
    if kode_buku not in BUKU:
        raise BukuNotFoundError(kode_buku)
    buku = BUKU[kode_buku]
    if not buku["tersedia"]:
        raise BukuTidakTersediaError(buku["judul"])
    buku["tersedia"] = False
    return f"{ANGGOTA[id_anggota]} berhasil meminjam '{buku['judul']}'"


if __name__ == "__main__":
    skenario = [
        ("A01", "B001"),  # sukses
        ("A01", "B002"),  # buku tidak tersedia
        ("A01", "B999"),  # buku tidak ada
        ("A99", "B001"),  # anggota tidak ada
    ]
    for anggota, buku in skenario:
        try:
            print(pinjam_buku(anggota, buku))
        except BukuNotFoundError as e:
            print(f"[Buku tidak ada] {e}")
        except BukuTidakTersediaError as e:
            print(f"[Tidak tersedia] {e}")
        except AnggotaNotFoundError as e:
            print(f"[Anggota tidak ada] {e}")
        except PerpustakaanError as e:
            print(f"[Error umum] {e}")