import pandas as pd
from hlatypingtools.decrypt_file import open_pickle_file

def test_open_pickle_file() -> None:
    data = open_pickle_file()
    assert isinstance(data, dict)
    assert isinstance(data["HLA_A"], pd.DataFrame)
