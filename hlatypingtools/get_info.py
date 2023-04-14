import hlatypingtools.decrypt_file
import logging
import pandas as pd


try:
    DATA: dict[str, pd.DataFrame] = hlatypingtools.decrypt_file.open_pickle_file()
except FileNotFoundError:
    logging.error("Error 1: Decrypt the file first")
    exit(1)


def get_locus(allele: str) -> str:
    """
    Get locus from allele
    :param allele: allele
    :return: locus
    """
    return "HLA_" + allele.split("*")[0]


def get_allele_info(allele: str) -> str:
    return allele
