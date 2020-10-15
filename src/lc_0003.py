""" Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
"""
from typing import List


class Solution:
    def reverse(self, nums: List[int], i: int, j: int) -> None:
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def rotate_with_reverse(self, nums: List[int], k: int) -> None:
        k -= (k // len(nums)) * len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def rotate_pythonic(self, nums: List[int], k: int) -> None:
        k -= (k // len(nums)) * len(nums)
        if k == 0:
            return
        nums[0:k], nums[k:] = nums[-k:], nums[0:-k]

    def rotate(self, nums: List[int], k: int) -> None:
        self.rotate_pythonic(nums, k)
        # self.rotate_with_reverse(nums, k)


if __name__ == "__main__":
    # nums = [1, 2, 3, 4, 5, 6, 7]
    nums = [-1, -2]
    k = 3
    print(nums, k)
    Solution().rotate(nums, k)
    print(nums)
