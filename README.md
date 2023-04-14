# HLATypingTools

## Getting Started
#### Install from PyPI (recommended)
To use `HLATypingTools`, run `pip install HLATypingTools` in your terminal.

#### Usage
If you haven't decrypted the data yet (first time you are using the package and you did request access to the product),
run:
```py
from hlatypingtools.decrypt_file import decrypt_file

password: str = "___"   # Replace with password provided by the author 
decrypt_file(password)
```
It should print `File decrypted successfully`.

Then you can use the package as follows:
```py
from hlatypingtools.get_info import get_allele_info

allele: str = "A*01:01"
print(get_allele_info(allele, "Broad"))  # will output A1
print(get_allele_info(allele, "G Group"))  # will output A*01:01:01G
print(get_allele_info(allele, "P Group"))  # will output A*01:01P
print(get_allele_info(allele, "% locus"))  # will output 11.906
```

Or as follows:
```py
from hlatypingtools.get_info import get_locus
print(get_locus("A*01:01"))  # will output HLA_A
```

Or as follows to output all possible high-resolution alleles for a given low-resolution typing:
```py
from hlatypingtools.get_info import get_same_low_res_broad, get_same_low_res_assigned_type
broad = "DQ3"
print("DQB1*03:01" in get_same_low_res_broad(broad))  # will output True
print("DQB1*03:02" in get_same_low_res_broad(broad))  # will output True

assigned_type = "DQ7"
print("DQB1*03:01" in get_same_low_res_assigned_type(assigned_type))  # will output True
print("DQB1*03:02" in get_same_low_res_assigned_type(assigned_type))  # will output False
```
Note:
- Broad = something like A1, B7, Cw1, DR1, **DQ3** (!!!), DQA1&ast;01, DR52, DPB1&ast;01, or DPA1&ast;01,
- Assigned Type = something like A1, B7, Cw1, DR1, **DQ7** (!!!), DQA1&ast;01, DR52, DPB1&ast;01, or DPA1&ast;01

#### Exit codes
```
0: Wrong password.
1: Tried to acess the functions of the package without decrypting the data first.
2: type_info requested is not available.
3: wrong format for a low-resolution input. Has to be of the form A1, B7, Cw1, DR1, DQ3, DQA1*01, DR52, DPB1*01, or 
DPA1*01.
```

## About the source code
- Follows [PEP8](https://peps.python.org/pep-0008/) Style Guidelines.
- All functions are unit-tested with [pytest](https://docs.pytest.org/en/stable/).
- All variables are correctly type-hinted, reviewed with [static type checker](https://mypy.readthedocs.io/en/stable/)
`mypy`.
- All functions are documented with [docstrings](https://www.python.org/dev/peps/pep-0257/).


## Useful links:
- [Corresponding GitHub repository](https://github.com/JasonMendoza2008/HLATypingTools)
- [Corresponding PyPI page](https://pypi.org/project/HLATypingTools)
