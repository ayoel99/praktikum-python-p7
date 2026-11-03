"""Modul pemrosesan nilai mahasiswa."""

TIPE_NILAI_AKHIR = 1
BATAS_A = 85
BATAS_B = 70
PANJANG_NIM = 10


def validasi_nim(nim: str) -> None:
    """Validasi NIM harus 10 digit angka."""
    if not nim.isdigit() or len(nim) != PANJANG_NIM:
        raise ValueError(f"NIM '{nim}' tidak valid")


def tentukan_huruf(nilai: float) -> str:
    """Konversi nilai angka menjadi huruf mutu."""
    if nilai >= BATAS_A:
        return "A"
    if nilai >= BATAS_B:
        return "B"
    return "C"


def proses_nilai(data: dict, tipe: int):
    """Proses nilai mahasiswa dan kembalikan huruf mutu."""
    if not data or tipe != TIPE_NILAI_AKHIR:
        return None
    if data["nilai"] <= 0 or data["sks"] <= 0:
        return None
    huruf = tentukan_huruf(data["nilai"])
    print(f"Nama: {data['nama']}, Huruf: {huruf}")
    return huruf


def update_mahasiswa(data: dict) -> None:
    """Update data mahasiswa."""
    validasi_nim(data["nim"])


if __name__ == "__main__":
    mhs = {"nama": "Devina", "nim": "2021001234", "nilai": 90, "sks": 3}
    proses_nilai(mhs, TIPE_NILAI_AKHIR)
    update_mahasiswa(mhs)