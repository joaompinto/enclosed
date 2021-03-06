from ._version import get_versions
from .parser import Parser, TokenType

__version__ = get_versions()["version"]
del get_versions

__all__ = [Parser, TokenType]
