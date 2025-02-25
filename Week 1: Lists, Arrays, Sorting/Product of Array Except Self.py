class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        temp = 1
        ret = [1] * n

        for i in range(1,n):
            ret[i] = ret[i-1] * nums[i-1]
        
        for j in range(n-2, -1, -1):
            temp *= nums[j+1]
            ret[j] *= temp

        return ret