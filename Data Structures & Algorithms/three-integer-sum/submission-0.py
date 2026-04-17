from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res: List[List[int]] = []

        for i in range(n - 2):
            # Skip duplicate 'i' to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Optional early stop: since nums is sorted
            if nums[i] > 0:
                break

            left, right = i + 1, n - 1
            target = -nums[i]

            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[i], nums[left], nums[right]])

                    # Move left forward and skip duplicates
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Move right backward and skip duplicates
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif s < target:
                    left += 1
                else:
                    right -= 1

        return res