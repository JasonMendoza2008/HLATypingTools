# Only needs to be run once
import pyAesCrypt  # type: ignore

def decrypt_file(password: str) -> None:
    try:
        pyAesCrypt.decryptFile("data/data.pickle.aes", f"data/data.pickle", password)
    except ValueError:
        print("Wrong password, please contact lhotteromain@gmail.com to purchase the product")
