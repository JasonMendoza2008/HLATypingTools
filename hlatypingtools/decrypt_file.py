# Only needs to be run once
import logging
import pandas as pd
import os
import pickle
import pyAesCrypt  # type: ignore

PATH_THIS_FILE: str = os.path.dirname(os.path.abspath(__file__))


def decrypt_file(password: str) -> None:
    try:
        pyAesCrypt.decryptFile(
            PATH_THIS_FILE + "/data/data.pickle.aes",
            PATH_THIS_FILE + "/data/data.pickle",
            password
        )
        logging.info("File decrypted successfully")
    except ValueError:
        logging.error(
            "Error 0: Wrong password, please contact lhotteromain@gmail.com to request access to the product."
        )


def open_pickle_file() -> dict[str, pd.DataFrame]:
    with open(PATH_THIS_FILE + "/data/data.pickle", "rb") as f:
        data = pickle.load(f)
    return data
