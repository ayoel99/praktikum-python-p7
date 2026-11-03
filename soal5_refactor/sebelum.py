def proses(data, tipe):
    # long method + deep nesting + magic number
    if data:
        if tipe == 1:
            if data["nilai"] > 0:
                if data["sks"] > 0:
                    if data["nilai"] >= 85:
                        h = "A"
                    elif data["nilai"] >= 70:
                        h = "B"
                    else:
                        h = "C"
                    print("Nama:", data["nama"], "Huruf:", h)
                    return h
    # duplikasi
    if not data["nim"].isdigit() or len(data["nim"]) != 10:
        raise ValueError("NIM tidak valid")


def update(data):
    if not data["nim"].isdigit() or len(data["nim"]) != 10:
        raise ValueError("NIM tidak valid")  # duplikasi


def fungsi_lama():  # dead code, tidak pernah dipanggil
    return "tidak terpakai"


if __name__ == "__main__":
    mhs = {"nama": "Devina", "nim": "2021001234", "nilai": 90, "sks": 3}
    proses(mhs, 1)
    update(mhs)