import csv


def baca_data_mahasiswa(path):
    file = None
    try:
        file = open(path, newline="", encoding="utf-8")
        reader = csv.DictReader(file)
        data = []
        for baris in reader:
            baris["ipk"] = float(baris["ipk"])  # bisa ValueError
            data.append(baris)
    except FileNotFoundError:
        print(f"File '{path}' tidak ditemukan")
        return None
    except csv.Error as e:
        print(f"Format CSV bermasalah: {e}")
        return None
    except ValueError as e:
        print(f"Nilai IPK tidak valid: {e}")
        return None
    else:
        # hanya jalan kalau tidak ada exception
        print(f"Berhasil membaca {len(data)} data")
        rata = sum(m["ipk"] for m in data) / len(data)
        print(f"Rata-rata IPK: {rata:.2f}")
        return data
    finally:
        # selalu jalan
        if file:
            file.close()
            print("File ditutup")


if __name__ == "__main__":
    baca_data_mahasiswa("data_mahasiswa.csv")  # berhasil
    baca_data_mahasiswa("tidak_ada.csv")  # FileNotFoundError