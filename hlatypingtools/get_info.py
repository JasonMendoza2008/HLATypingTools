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
    if "DRB3" in allele or "DRB4" in allele or "DRB5" in allele:
        return "HLA_DRB345"
    return "HLA_" + allele.split("*")[0]


def get_locus_from_low_res(low_res: str) -> str:
    """
    Get locus from low resolution
    :param low_res: low resolution
    :return: locus
    """
    if low_res.startswith("A"):
        return "HLA_A"
    elif low_res.startswith("B"):
        return "HLA_B"
    elif low_res.startswith("C"):
        return "HLA_C"
    elif low_res in ["DR52", "DR53", "DR51"]:
        return "HLA_DRB345"
    elif low_res.startswith("DR"):
        # DRB345 already dealt with
        return "HLA_DRB1"
    elif low_res.startswith("DQA1"):
        return "HLA_DQA1"
    elif low_res.startswith("DQ"):
        # DQA1 already dealt with
        return "HLA_DQB1"
    elif low_res.startswith("DPB"):
        return "HLA_DPB1"
    elif low_res.startswith("DPA"):
        return "HLA_DPA1"
    else:
        logging.error("Error 3: low_res not valid")
        exit(1)


def get_allele_info(
    allele: str,
    type_info: str,
) -> str:
    """
    Get allele info, for a given type of info
    :param allele: allele
    :param type_info: can be one of the following: ["% locus", "% first-field", ,"% individuals",
    "Expert", "WHO", "NN", "G Group", "P Group", "Broad", "Assigned Type"]

    :return: info asked
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


def get_same_low_res_broad(low_res: str) -> list[str]:
    """
    Get all the alleles that share the same Broad Type
    :param low_res: broad type (e.g. A1, B7, Cw1, DR1, DQ3, DQA1*01, DR52, DPB1*01, DPA1*01)
    :return: list of alleles that share the same broad type
    """

    locus = get_locus_from_low_res(low_res)
    rows_same_broad = DATA[locus][DATA[locus]["Broad"] == low_res]
    return rows_same_broad.index.tolist()


def get_same_low_res_assigned_type(low_res: str) -> list[str]:
    """
    Get all the alleles that share the same Assigned Type
    :param low_res: broad type (e.g. A1, B7, Cw1, DR1, DQ7, DQA1*01, DR52, DPB1*01, DPA1*01)
    :return: list of alleles that share the same broad type
    """

    locus = get_locus_from_low_res(low_res)
    rows_same_broad = DATA[locus][DATA[locus]["Assigned Type"] == low_res]
    return rows_same_broad.index.tolist()

