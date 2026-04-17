class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
           map ={}
           for i,value in enumerate(nums):
            rem = target - nums[i]
            if rem in map:
                return [map[rem],i]
            map[value]=i
