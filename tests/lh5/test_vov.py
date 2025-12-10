from __future__ import annotations

import awkward as ak

import lh5


def test_lh5_iterator_view_as(lgnd_test_data):
    it = lh5.LH5Iterator(
        lgnd_test_data.get_path("lh5/l200-p03-r000-phy-20230312T055349Z-tier_psp.lh5"),
        "ch1067205/dsp/energies",
    )

    for obj in it:
        assert ak.is_valid(obj.view_as("ak"))
