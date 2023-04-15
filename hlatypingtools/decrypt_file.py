# Only needs to be run once
import logging
import pandas as pd
import os
import pickle
import pyAesCrypt  # type: ignore

def decrypt_file(password: str) -> None:
    path_this_file: str = os.path.dirname(os.path.abspath(__file__))
    try:
        pyAesCrypt.decryptFile(
            path_this_file  + "data/data.pickle.aes",
            path_this_file + "data/data.pickle",
            password
        )
        logging.info("File decrypted successfully")
    except ValueError:
        logging.error(
            "Error 0: Wrong password, please contact lhotteromain@gmail.com to request access to the product."
        )


def open_pickle_file() -> dict[str, pd.DataFrame]:
    with open("data/data.pickle", "rb") as f:
        data = pickle.load(f)
    return data
