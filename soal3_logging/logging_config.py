import logging
from logging.handlers import RotatingFileHandler


def setup_logger(nama="si_akademik"):
    logger = logging.getLogger(nama)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # (a) File handler: DEBUG ke atas, rotasi 5MB, simpan 3 backup
    file_handler = RotatingFileHandler(
        "si_akademik.log", maxBytes=5 * 1024 * 1024, backupCount=3
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # (b) Console handler: WARNING ke atas
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


if __name__ == "__main__":
    log = setup_logger()
    log.debug("Query SQL: SELECT * FROM mahasiswa")
    log.info("User admin berhasil login")
    log.warning("Penggunaan memori mencapai 85%")
    log.error("Gagal mengirim email notifikasi")
    log.critical("Koneksi database terputus!")