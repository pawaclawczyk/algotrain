"""
Note: Working, but terribly slow comparing to other solutions!
"""

from typing import List

import pytest


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        collision = True
        while collision:
            collision = False
            i = None
            for j in range(0, len(asteroids)):
                if asteroids[j] > 0:
                    i = j
                elif i is not None and asteroids[j] < 0:
                    if abs(asteroids[j]) == asteroids[i]:
                        asteroids[i] = 0
                        asteroids[j] = 0
                        collision = True
                        break

                    if abs(asteroids[j]) > asteroids[i]:
                        asteroids[i] = 0
                        collision = True
                        break

                    if abs(asteroids[j]) < asteroids[i]:
                        asteroids[j] = 0
                        collision = True

        return [a for a in asteroids if a]


def test_all_left():
    assert Solution().asteroidCollision([-1, -3, -2]) == [-1, -3, -2]


def test_all_right():
    assert Solution().asteroidCollision([1, 3, 2]) == [1, 3, 2]


@pytest.mark.parametrize(
    "a, r",
    [
        ([1, -1], []),
        ([2, -1], [2]),
        ([1, -2], [-2]),
    ],
)
def test_collisions(a, r):
    assert Solution().asteroidCollision(a) == r


def test_revers_crash():
    assert Solution().asteroidCollision([3, 2, 1, -1, -1, -4]) == [-4]
