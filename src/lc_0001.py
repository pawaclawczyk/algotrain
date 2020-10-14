""" House Robber II

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected,
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = dict()

        if n < 4:
            return max(nums)

        def f(house: int, n: int, depth: int):
            if (house, n) in cache:
                return cache[(house, n)]

            if house >= n:
                return 0

            result = max(f(house + 2, n, depth + 1),
                         f(house + 3, n, depth + 1)) + nums[house]

            cache[(house, n)] = result

            return result

        return max(f(0, n - 1, 0), f(1, n, 0), f(2, n, 0))


if __name__ == "__main__":
    examples = [
        [2, 3, 2],
        [1, 2, 3, 1],
        [1, 2, 1, 1],
        [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
        [94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61, 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397, 52,
         72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]
    ]

    for e in examples:
        r = Solution().rob(e)
        print(f"Example: f({e}) = {r}")
