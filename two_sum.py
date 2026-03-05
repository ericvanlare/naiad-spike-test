from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.

    Assumes exactly one solution exists and the same element
    cannot be used twice.

    Time:  O(n)
    Space: O(n)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    # Example cases
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(two_sum([3, 2, 4], 6))         # [1, 2]
    print(two_sum([3, 3], 6))            # [0, 1]
