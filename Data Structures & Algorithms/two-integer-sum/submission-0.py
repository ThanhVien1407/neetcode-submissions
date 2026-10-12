class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            phan_bu = target - n
            if phan_bu in hashmap:
                return [hashmap[phan_bu], i]
            else:
                hashmap[nums[i]] = i