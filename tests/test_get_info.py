from hlatypingtools.get_info import get_allele_info, get_locus

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

def test_get_locus_c() -> None:
    allele = "C*07:01"
    expected_locus = "HLA_C"
    assert get_locus(allele) == expected_locus

def test_get_info_a0101() -> None:
    allele = "A*01:01"
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
