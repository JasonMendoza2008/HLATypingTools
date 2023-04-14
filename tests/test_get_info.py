from hlatypingtools.get_info import get_allele_info, get_locus

def test_get_locus_a():
    allele = "A*01:01"
    expected_locus = "HLA_A"
    assert get_locus(allele) == expected_locus

def test_get_locus_b():
    allele = "B*07:02"
    expected_locus = "HLA_B"
    assert get_locus(allele) == expected_locus

def test_get_locus_drb1():
    allele = "DRB1*04:03"
    expected_locus = "HLA_DRB1"
    assert get_locus(allele) == expected_locus

def test_get_locus_c():
    allele = "C*07:01"
    expected_locus = "HLA_C"
    assert get_locus(allele) == expected_locus
