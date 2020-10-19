""" Minimum Domino Rotations For Equal Row

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

Example 1:

Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation:
In this case, it is not possible to rotate the dominoes to make one row of values equal.


Constraints:

2 <= A.length == B.length <= 2 * 104
1 <= A[i], B[i] <= 6
"""
from typing import List

import pytest


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        a, b = A[0], B[0]

        def count_rotations(value, base_line, other_line):
            rotations = 0

            for i in range(len(base_line)):
                if value != base_line[i] and value != other_line[i]:
                    return -1
                if value != base_line[i] and value == other_line[i]:
                    rotations += 1

            return rotations

        valid_result = []
        for v, base, other in [(a, A, B), (a, B, A), (b, A, B), (b, B, A)]:
            res = count_rotations(v, base, other)
            if res >= 0:
                valid_result.append(res)

        return min(valid_result) if valid_result else -1


@pytest.mark.parametrize(
    "a, b, rotations",
    [
        ([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2], 2),
        ([3, 5, 1, 2, 3], [3, 6, 3, 3, 4], -1),
        ([1], [1], 0),
        ([1], [2], 0),
        ([1, 2], [3, 3], 0),
        ([1, 1], [2, 3], 0),
        ([1, 2, 1], [2, 1, 4], 1),
        ([1, 2, 3], [4, 1, 1], 1),
        ([1, 2, 2], [2, 3, 4], 1),
        ([2, 3, 4], [5, 2, 2], 1),
    ],
)
def test_examples(a, b, rotations):
    assert Solution().minDominoRotations(a, b) == rotations
