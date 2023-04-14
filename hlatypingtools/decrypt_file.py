# Only needs to be run once
import pandas as pd
import pickle
import pyAesCrypt  # type: ignore

def decrypt_file(password: str) -> None:
    try:
        pyAesCrypt.decryptFile("data/data.pickle.aes", f"data/data.pickle", password)
        print("File decrypted successfully")
    except ValueError:
        print("Wrong password, please contact lhotteromain@gmail.com to purchase the product")


def open_pickle_file() -> dict[str, pd.DataFrame]:
    with open("data/data.pickle", "rb") as f:
        data = pickle.load(f)
    return data
