# Only needs to be run once
import logging
import pandas as pd
import pickle
import pyAesCrypt  # type: ignore

def decrypt_file(password: str) -> None:
    try:
        pyAesCrypt.decryptFile("data/data.pickle.aes", f"data/data.pickle", password)
        logging.info("File decrypted successfully")
    except ValueError:
        logging.error(
            "Error 0: Wrong password, please contact lhotteromain@gmail.com to request access to the product."
        )


def open_pickle_file() -> dict[str, pd.DataFrame]:
    with open("data/data.pickle", "rb") as f:
        data = pickle.load(f)
    return data
