""" Course Schedule (Medium)

https://leetcode.com/problems/course-schedule/

Note: The solution is to iteratively remove terminating nodes
with their edges. A terminating node is a node without ingress
or egress edges. The solution is slow (faster than 18% of other solutions).
"""
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def delete_terminators(edges):
            while edges:
                ingress, egress = set(), set()
                for e in edges:
                    ingress.add(e[1])
                    egress.add(e[0])
                terminators = egress.difference(ingress).union(
                    ingress.difference(egress)
                )
                if not terminators:
                    return False
                edges = [
                    e
                    for e in edges
                    if e[0] not in terminators and e[1] not in terminators
                ]
            return True

        return delete_terminators(prerequisites)


def test_empty_graph():
    assert Solution().canFinish(0, []) is True


def test_singular_graph():
    assert Solution().canFinish(1, []) is True


def test_chain_graph():
    assert Solution().canFinish(4, [[0, 1], [1, 2], [2, 3]]) is True


def test_singular_loop_graph():
    assert Solution().canFinish(1, [[0, 0]]) is False


def test_loop_graph():
    assert Solution().canFinish(4, [[0, 1], [1, 2], [2, 3], [3, 0]]) is False


def test_dense_graph():
    assert (
        Solution().canFinish(
            6, [[0, 2], [0, 3], [1, 2], [1, 3], [2, 4], [2, 5], [3, 4], [3, 5]]
        )
        is True
    )


def test_inner_loop_graph():
    assert Solution().canFinish(4, [[0, 1], [1, 2], [2, 3], [2, 1]]) is False
