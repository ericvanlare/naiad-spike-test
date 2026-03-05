"""
3Sum Problem
============
Given an integer array `nums`, return all the triplets
[nums[i], nums[j], nums[k]] such that:
  - i != j, i != k, and j != k
  - nums[i] + nums[j] + nums[k] == 0

The solution set must not contain duplicate triplets.

Example 1:
  Input:  nums = [-1, 0, 1, 2, -1, -4]
  Output: [[-1, -1, 2], [-1, 0, 1]]

Example 2:
  Input:  nums = [0, 1, 1]
  Output: []

Example 3:
  Input:  nums = [0, 0, 0]
  Output: [[0, 0, 0]]
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets in `nums` that sum to zero.

    Strategy (Sort + Two-Pointer Approach):
    ----------------------------------------
    1. **Sort** the array.  Sorting lets us:
       - Skip duplicate values easily (adjacent duplicates are next to
         each other).
       - Use a two-pointer technique on the remaining sub-array, which
         relies on the sorted order to decide whether to move the left
         pointer right or the right pointer left.

    2. **Fix one element** (`nums[i]`) and reduce the problem to Two Sum
       on the rest of the array (`nums[i+1 .. n-1]`).

    3. For each fixed `nums[i]`:
       a. If `nums[i] > 0`, we can stop early — since the array is sorted,
          no three positive numbers can sum to zero.
       b. Skip `nums[i]` if it equals `nums[i-1]` (avoids duplicate
          triplets that share the same first element).
       c. Set two pointers:
              left  = i + 1        (just after the fixed element)
              right = len(nums) - 1 (end of the array)
       d. While `left < right`:
          - Compute `current_sum = nums[i] + nums[left] + nums[right]`.
          - If `current_sum < 0`:  we need a larger sum → move `left`
            to the right.
          - If `current_sum > 0`:  we need a smaller sum → move `right`
            to the left.
          - If `current_sum == 0`: we found a valid triplet!
            * Record it.
            * Advance `left` past any duplicates.
            * Advance `right` past any duplicates.
            * Move both pointers inward to continue searching.

    Why this works
    --------------
    Sorting costs O(n log n).  For each of the n elements we do at most
    an O(n) two-pointer scan, giving O(n²) overall — far better than the
    naïve O(n³) brute-force.

    Duplicate avoidance is handled at two levels:
      • Outer loop: skip repeated values of `nums[i]`.
      • Inner loop: after finding a valid triplet, skip repeated values
        of `nums[left]` and `nums[right]`.

    Time complexity:  O(n²)  — one pass per fixed element.
    Space complexity: O(n)   — for the sort (depending on the language /
                               sort implementation) plus the output list.

    Parameters
    ----------
    nums : List[int]
        The list of integers to search.

    Returns
    -------
    List[List[int]]
        A list of all unique triplets [a, b, c] where a + b + c == 0,
        sorted in non-descending order within each triplet.
    """

    # --- Step 1: Sort the array ---
    # Sorting enables both duplicate-skipping and the two-pointer technique.
    nums.sort()

    n = len(nums)
    result: List[List[int]] = []

    # --- Step 2: Iterate over each element as the "fixed" first value ---
    for i in range(n):

        # Early termination: if the smallest remaining number is positive,
        # no valid triplet can be formed (all subsequent sums will be > 0).
        if nums[i] > 0:
            break

        # Skip duplicate values for the first element of the triplet.
        # We only process the first occurrence of each value in the
        # outer loop to avoid producing duplicate triplets.
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # --- Step 3: Two-pointer search in nums[i+1 .. n-1] ---
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum < 0:
                # Sum is too small — we need a larger value on the left.
                left += 1

            elif current_sum > 0:
                # Sum is too large — we need a smaller value on the right.
                right -= 1

            else:
                # Found a valid triplet!
                result.append([nums[i], nums[left], nums[right]])

                # Move `left` forward past duplicate values so we don't
                # record the same triplet again.
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Move `right` backward past duplicate values.
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Advance both pointers inward to look for more triplets
                # with the same fixed element nums[i].
                left += 1
                right -= 1

    return result


# ---------------------------------------------------------------------------
# Quick demo / manual tests
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # --- Test case 1 ---
    # Classic example with two valid triplets.
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = three_sum(nums1)
    print(f"Input: nums={[-1, 0, 1, 2, -1, -4]}")
    print(f"Output: {result1}")
    # Expected: [[-1, -1, 2], [-1, 0, 1]]
    assert result1 == [[-1, -1, 2], [-1, 0, 1]], f"Test 1 failed: got {result1}"
    print("✓ Test 1 passed\n")

    # --- Test case 2 ---
    # No triplet sums to zero.
    nums2 = [0, 1, 1]
    result2 = three_sum(nums2)
    print(f"Input: nums={[0, 1, 1]}")
    print(f"Output: {result2}")
    # Expected: []
    assert result2 == [], f"Test 2 failed: got {result2}"
    print("✓ Test 2 passed\n")

    # --- Test case 3 ---
    # Three zeros sum to zero.
    nums3 = [0, 0, 0]
    result3 = three_sum(nums3)
    print(f"Input: nums={[0, 0, 0]}")
    print(f"Output: {result3}")
    # Expected: [[0, 0, 0]]
    assert result3 == [[0, 0, 0]], f"Test 3 failed: got {result3}"
    print("✓ Test 3 passed\n")

    # --- Test case 4 ---
    # Multiple triplets with negative numbers.
    nums4 = [-2, 0, 1, 1, 2]
    result4 = three_sum(nums4)
    print(f"Input: nums={[-2, 0, 1, 1, 2]}")
    print(f"Output: {result4}")
    # Expected: [[-2, 0, 2], [-2, 1, 1]]
    assert result4 == [[-2, 0, 2], [-2, 1, 1]], f"Test 4 failed: got {result4}"
    print("✓ Test 4 passed\n")

    # --- Test case 5 ---
    # Array too short — no triplet possible.
    nums5 = [1, 2]
    result5 = three_sum(nums5)
    print(f"Input: nums={[1, 2]}")
    print(f"Output: {result5}")
    # Expected: []
    assert result5 == [], f"Test 5 failed: got {result5}"
    print("✓ Test 5 passed\n")

    # --- Test case 6 ---
    # All zeros (more than three) — only one unique triplet.
    nums6 = [0, 0, 0, 0]
    result6 = three_sum(nums6)
    print(f"Input: nums={[0, 0, 0, 0]}")
    print(f"Output: {result6}")
    # Expected: [[0, 0, 0]]
    assert result6 == [[0, 0, 0]], f"Test 6 failed: got {result6}"
    print("✓ Test 6 passed\n")

    # --- Test case 7 ---
    # Larger example with several valid triplets.
    nums7 = [-4, -2, -1, 0, 1, 2, 3, 4]
    result7 = three_sum(nums7)
    print(f"Input: nums={[-4, -2, -1, 0, 1, 2, 3, 4]}")
    print(f"Output: {result7}")
    # Expected: [[-4, 0, 4], [-4, 1, 3], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
    assert result7 == [[-4, 0, 4], [-4, 1, 3], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]], \
        f"Test 7 failed: got {result7}"
    print("✓ Test 7 passed\n")

    # --- Test case 8 ---
    # Empty array.
    nums8: List[int] = []
    result8 = three_sum(nums8)
    print(f"Input: nums={[]}")
    print(f"Output: {result8}")
    # Expected: []
    assert result8 == [], f"Test 8 failed: got {result8}"
    print("✓ Test 8 passed\n")

    print("All tests passed! 🎉")
