"""
Two Sum Problem
===============
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers such that they add up to `target`.

Assumptions:
  - Each input has exactly one solution.
  - You may not use the same element twice.
  - The answer can be returned in any order.

Example:
  Input:  nums = [2, 7, 11, 15], target = 9
  Output: [0, 1]   # because nums[0] + nums[1] == 2 + 7 == 9
"""

from typing import List, Optional, Tuple


def two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Find two indices in `nums` whose corresponding values sum to `target`.

    Strategy (Hash Map / Dictionary Approach):
    ------------------------------------------
    1. Walk through the list one element at a time.
    2. For each element, compute the "complement" — the value we'd need to
       pair with the current element to reach `target`.
           complement = target - current_element
    3. Check whether that complement has already been seen (i.e. it's stored
       in our dictionary). If yes, we've found our pair — return both indices.
    4. If not, record the current element and its index in the dictionary so
       that a future element can find it as its complement.

    Time complexity:  O(n)  — single pass through the list.
    Space complexity: O(n)  — in the worst case every element is stored in
                              the dictionary before we find a match.

    Parameters
    ----------
    nums : List[int]
        The list of integers to search.
    target : int
        The target sum we're looking for.

    Returns
    -------
    Tuple[int, int] | None
        A tuple of the two indices whose values sum to `target`,
        or None if no valid pair exists.
    """

    # Dictionary that maps each seen value to its index.
    # Key:   a number from `nums`
    # Value: the index at which that number appears
    seen: dict[int, int] = {}

    # Iterate over every element together with its index.
    for index, number in enumerate(nums):

        # Calculate what value we'd need to pair with `number`
        # in order to hit the target sum.
        complement = target - number

        # Have we already encountered the complement earlier in the list?
        if complement in seen:
            # Yes! Return the earlier index (from the dict) and the current
            # index. Together they form the solution.
            return (seen[complement], index)

        # We haven't found a match yet, so store this number → index
        # mapping for future look-ups.
        seen[number] = index

    # If we exhaust the list without finding a pair, return None.
    # (Per the classic problem statement this shouldn't happen when
    # the input guarantees exactly one solution.)
    return None


# ---------------------------------------------------------------------------
# Quick demo / manual tests
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # --- Test case 1 ---
    # The pair (2, 7) at indices 0 and 1 sums to 9.
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = two_sum(nums1, target1)
    print(f"Input: nums={nums1}, target={target1}")
    print(f"Output: {result1}")          # Expected: (0, 1)
    assert result1 == (0, 1), f"Test 1 failed: got {result1}"
    print("✓ Test 1 passed\n")

    # --- Test case 2 ---
    # The pair (3, 3) at indices 0 and 1 sums to 6.
    nums2 = [3, 3]
    target2 = 6
    result2 = two_sum(nums2, target2)
    print(f"Input: nums={nums2}, target={target2}")
    print(f"Output: {result2}")          # Expected: (0, 1)
    assert result2 == (0, 1), f"Test 2 failed: got {result2}"
    print("✓ Test 2 passed\n")

    # --- Test case 3 ---
    # The pair (2, 4) at indices 1 and 2 sums to 6.
    nums3 = [3, 2, 4]
    target3 = 6
    result3 = two_sum(nums3, target3)
    print(f"Input: nums={nums3}, target={target3}")
    print(f"Output: {result3}")          # Expected: (1, 2)
    assert result3 == (1, 2), f"Test 3 failed: got {result3}"
    print("✓ Test 3 passed\n")

    # --- Test case 4 ---
    # Negative numbers: (-1) + 1 = 0 at indices 0 and 2.
    nums4 = [-1, -2, 1, 4]
    target4 = 0
    result4 = two_sum(nums4, target4)
    print(f"Input: nums={nums4}, target={target4}")
    print(f"Output: {result4}")          # Expected: (0, 2)
    assert result4 == (0, 2), f"Test 4 failed: got {result4}"
    print("✓ Test 4 passed\n")

    # --- Test case 5 (no solution) ---
    # Demonstrates the None return when no pair exists.
    nums5 = [1, 2, 3]
    target5 = 100
    result5 = two_sum(nums5, target5)
    print(f"Input: nums={nums5}, target={target5}")
    print(f"Output: {result5}")          # Expected: None
    assert result5 is None, f"Test 5 failed: got {result5}"
    print("✓ Test 5 passed\n")

    print("All tests passed! 🎉")
