def hitung_ipk(nilai_list):
    if not nilai_list:
        return 0.0
    total_bobot = sum(n["bobot"] * n["sks"] for n in nilai_list)
    total_sks = sum(n["sks"] for n in nilai_list)
    if total_sks == 0:
        return 0.0
    return total_bobot / total_sks


def validasi_nim(nim):
    return isinstance(nim, str) and len(nim) == 10 and nim.isdigit()


def konversi_nilai_huruf(angka):
    if not isinstance(angka, (int, float)) or not 0 <= angka <= 100:
        raise ValueError("Nilai harus angka 0-100")
    if angka >= 85:
        return "A"
    if angka >= 80:
        return "A-"
    if angka >= 75:
        return "B+"
    if angka >= 70:
        return "B"
    if angka >= 65:
        return "C+"
    if angka >= 60:
        return "C"
    if angka >= 50:
        return "D"
    return "E"