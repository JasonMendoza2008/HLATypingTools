from hlatypingtools.get_info import get_allele_info, get_locus, get_same_low_res_broad, get_same_low_res_assigned_type

def test_get_locus_a() -> None:
    allele = "A*01:01"
    expected_locus = "HLA_A"
    assert get_locus(allele) == expected_locus

def test_get_locus_b() -> None:
    allele = "B*07:02"
    expected_locus = "HLA_B"
    assert get_locus(allele) == expected_locus

def test_get_locus_drb1() -> None:
    allele = "DRB1*04:03"
    expected_locus = "HLA_DRB1"
    assert get_locus(allele) == expected_locus

def test_get_locus_drb3() -> None:
    allele = "DRB3*01:01"
    expected_locus = "HLA_DRB345"
    assert get_locus(allele) == expected_locus

def test_get_locus_c() -> None:
    allele = "C*07:01"
    expected_locus = "HLA_C"
    assert get_locus(allele) == expected_locus

def test_get_info_a0101() -> None:
    allele: str = "A*01:01"
    expected_info_percent_locus = 11.906
    expected_info_percent_first_field = 97.856
    expected_info_p_group = "A*01:01P"
    expected_info_broad = "A1"
    expected_info_assigned_type = "A1"
    assert get_allele_info(allele, "% locus") == expected_info_percent_locus
    assert get_allele_info(allele, "% first-field") == expected_info_percent_first_field
    assert get_allele_info(allele, "P Group") == expected_info_p_group
    assert get_allele_info(allele, "Broad") == expected_info_broad
    assert get_allele_info(allele, "Assigned Type") == expected_info_assigned_type

def test_get_info_drb3() -> None:
    allele: str = "DRB3*01:01"
    expected_info_broad = "DR52"
    assert get_allele_info(allele, "Broad") == expected_info_broad

def test_get_same_low_res_broad() -> None:
    broad = "A1"
    expected_same_low_res_broad = [
        "A*01:01",
        "A*01:02",
        "A*01:03",
        "A*01:04N",
        "A*01:06",
        "A*01:07",
        "A*01:08",
        "A*01:09",
        "A*01:13",
        "A*01:131",
        "A*01:15N",
        "A*01:190",
        "A*01:20",
        "A*01:23",
        "A*01:25",
        "A*01:274",
        "A*01:332",
        "A*01:37",
        "A*01:42",
        "A*01:44",
        "A*01:45",
        "A*01:48",
        "A*01:77",
        "A*01:79",
        "A*01:83",
    ]
    assert get_same_low_res_broad(broad) == expected_same_low_res_broad


def test_get_same_low_res_assigned_type() -> None:
    assigned_type = "A1"
    expected_same_low_res_assigned_type = [
        "A*01:01",
        "A*01:02",
        "A*01:03",
        "A*01:04N",
        "A*01:06",
        "A*01:07",
        "A*01:08",
        "A*01:09",
        "A*01:13",
        "A*01:131",
        "A*01:15N",
        "A*01:190",
        "A*01:20",
        "A*01:23",
        "A*01:25",
        "A*01:274",
        "A*01:332",
        "A*01:37",
        "A*01:42",
        "A*01:44",
        "A*01:45",
        "A*01:48",
        "A*01:77",
        "A*01:79",
        "A*01:83",
    ]
    assert get_same_low_res_assigned_type(assigned_type) == expected_same_low_res_assigned_type


def test_dq3_dq7() -> None:
    broad = "DQ3"
    assert "DQB1*03:01" in get_same_low_res_broad(broad)
    assert "DQB1*03:02" in get_same_low_res_broad(broad)

    assigned_type = "DQ7"
    assert "DQB1*03:01" in get_same_low_res_assigned_type(assigned_type)
    assert "DQB1*03:02" not in get_same_low_res_assigned_type(assigned_type)


def test_b7() -> None:
    expected_assigned_type: str = "B57"
    allele: str = "B*57:73"

    assert get_allele_info(allele, "Assigned Type") == expected_assigned_type

def test_c14() -> None:
    # Assigned Type
    expected_assigned_type: str = "Cw14"
    allele: str = "C*14:02"

    assert get_allele_info(allele, "Assigned Type") == expected_assigned_type

    # Broad
    expected_broad: str = "Cw1"

    assert get_allele_info(allele, "Broad") == expected_broad


def test_dr9() -> None:
    # Assigned Type
    expected_assigned_type: str = "DR9"
    allele: str = "DRB1*09:02"

    assert get_allele_info(allele, "Assigned Type") == expected_assigned_type

    # Scrapped date
    expected_scrapped_date: str = "YYYY/MM/DD: 2024/03/06"
    assert get_allele_info(allele, "Scrapped date") == expected_scrapped_date
    