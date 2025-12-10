from __future__ import annotations

import pytest
from lgdo.types import Histogram

import lh5
from lh5.io.exceptions import LH5DecodeError


def test_read_histogram_testdata(lgnd_test_data):
    file = lgnd_test_data.get_path("lh5/lgdo-histograms.lh5")

    h1 = lh5.read("test_histogram_range", file)
    assert isinstance(h1, Histogram)
    assert h1.binning[0].is_range

    h2 = lh5.read("test_histogram_variable", file)
    assert isinstance(h2, Histogram)
    assert not h2.binning[0].is_range

    h3 = lh5.read("test_histogram_range_w_attrs", file)
    assert isinstance(h3, Histogram)
    assert h3.binning[0].is_range
    assert h3.binning[0]["binedges"].getattrs() == {"units": "m"}


def test_read_histogram_multiple(lgnd_test_data):
    file = lgnd_test_data.get_path("lh5/lgdo-histograms.lh5")
    with pytest.raises(LH5DecodeError):
        lh5.read("test_histogram_range", [file, file])
