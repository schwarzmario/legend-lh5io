from __future__ import annotations
from ._version import version as __version__

# import this so users can transparently decode data compressed with hdf5plugin
# filters
import hdf5plugin  # noqa: F401

from .io import LH5Iterator, LH5Store, ls, read, read_as, read_n_rows, show, write

__all__ = [
    "__version__",
    "LH5Iterator",
    "LH5Store",
    "ls",
    "read",
    "read_as",
    "read_n_rows",
    "show",
    "write",
]
