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

```

#### Exit codes
```
0: Wrong password.
1: Tried to acess the functions of the package without decrypting the data first.
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
