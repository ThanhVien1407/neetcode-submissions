class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        product = 1
        i, j = 0, 0

        while j < len(nums):
            if (nums[j] == nums[i]) and (j == len(nums) - 1):
                ans.append(product)
                break

            if nums[j] == nums[i]:
                i += 1
                continue
            product *= nums[i]
            i += 1
            
            if i == len(nums):
                ans.append(product)
                product = 1
                i = 0
                j += 1

        return ans