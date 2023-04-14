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


def get_allele_info(
    allele: str,
    type_info: str,
) -> str:
    """
    Get allele info, for a given type of info
    :param allele: allele
    :param type_info: can be one of the following: ["% locus", "% first-field", ,"% individuals",
    "Expert", "WHO", "NN", "G Group", "P Group", "Broad", "Assigned Type"]

    :return:
    """
    if type_info not in [
        "% locus",
        "% first-field",
        "% individuals",
        "Expert",
        "WHO",
        "NN",
        "G Group",
        "P Group",
        "Broad",
        "Assigned Type",
    ]:
        logging.error("Error 2: type_info not valid")
    return DATA[get_locus(allele)].loc[allele][type_info]
