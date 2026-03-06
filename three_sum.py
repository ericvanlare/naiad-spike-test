from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Given an array of integers nums, return all unique triplets
    [nums[i], nums[j], nums[k]] such that i != j != k and
    nums[i] + nums[j] + nums[k] == 0.

    The solution set must not contain duplicate triplets.

    Time:  O(n^2)
    Space: O(n) (ignoring the output)
    """
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for the second element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for the third element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return result


if __name__ == "__main__":
    # Example cases
    print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
    print(three_sum([0, 1, 1]))                # []
    print(three_sum([0, 0, 0]))                # [[0, 0, 0]]
