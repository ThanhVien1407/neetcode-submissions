class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * 2 * len(nums)
        i, j = 0, 0

        while j < 2 * len(nums) :
            ans[j] = nums[i]
            j += 1
            i += 1

            if i == len(nums):
                i = 0

        return ans

