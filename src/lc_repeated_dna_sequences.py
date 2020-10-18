""" Repeated DNA Sequences

All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T',
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

Constraints:

0 <= s.length <= 105
s[i] is 'A', 'C', 'G', or 'T'.
"""
from typing import List

import pytest


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen_once = set()
        seen_more = set()

        for i in range(len(s) - 9):
            sequence = s[i : i + 10]
            if sequence in seen_once:
                seen_more.add(sequence)
            else:
                seen_once.add(sequence)

        return seen_more


def test_shared_part():
    s = "AAAAAAAAAAAAA"
    assert Solution().findRepeatedDnaSequences(s) == ["AAAAAAAAAA"]


def test_distinct_with_common_piece():
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    assert sorted(Solution().findRepeatedDnaSequences(s)) == sorted(
        ["AAAAACCCCC", "CCCCCAAAAA"]
    )


def test_distinct():
    s = "AAAAACCCCCAAAAACCCCC"
    assert Solution().findRepeatedDnaSequences(s) == ["AAAAACCCCC"]


@pytest.mark.parametrize(
    "s",
    [
        ("",),
        ("AAAAACCCC",),
    ],
)
def test_too_short(s):
    assert Solution().findRepeatedDnaSequences(s) == []
