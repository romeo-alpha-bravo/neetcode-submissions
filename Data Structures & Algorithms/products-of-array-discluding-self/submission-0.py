class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #initial nums = [1,2,4,6]
        res = [1] * len(nums)

        left_product = 1
        for i in range(len(nums)):
            res[i] *= left_product
            left_product *= nums[i]  # 1 1 2 8 left portion

        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]

        return res
