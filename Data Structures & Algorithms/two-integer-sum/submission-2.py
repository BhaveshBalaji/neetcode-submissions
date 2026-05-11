class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen_dict and seen_dict[complement] != i:
                return [seen_dict[complement], i]
            seen_dict[num] = i
        