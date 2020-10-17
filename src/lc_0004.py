""" Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false

Example 3:

Input: matrix = [], target = 0
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
0 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
"""
from typing import List

import pytest


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """The solution can be improved by using binary search."""
        n = len(matrix)
        if not n:
            return False
        m = len(matrix[0])
        if not m:
            return False

        for i in range(n):
            if matrix[i][0] <= target <= matrix[i][m - 1]:
                for j in range(m):
                    if matrix[i][j] == target:
                        return True
                return False
        return False


@pytest.mark.parametrize(
    "matrix, target, expected",
    [
        ([], 0, False),
        ([[]], 1, False),
        ([[1]], 1, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 13, False),
    ],
)
def test_example(matrix, target, expected):
    assert Solution().searchMatrix(matrix, target) is expected
