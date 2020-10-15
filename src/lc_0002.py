""" Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Constraints:

* 1 <= m, n <= 100
* It's guaranteed that the answer will be less than or equal to 2 * 10^9.
"""
import functools


class Solution:
    @functools.lru_cache()
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1:
            return 1
        if n == 1:
            return 1
        return self.uniquePaths(m, n - 1) + self.uniquePaths(m - 1, n)


if __name__ == "__main__":
    examples = [
        ((1, 4), 1),
        ((4, 1), 1),
        ((2, 2), 2),
        ((3, 7), 28),
        ((3, 2), 3),
        ((7, 3), 28),
        ((3, 3), 6),
    ]

    for (m, n), expected in examples:
        result = Solution().uniquePaths(m, n)
        assert result == expected, f"{result} != {expected}"
