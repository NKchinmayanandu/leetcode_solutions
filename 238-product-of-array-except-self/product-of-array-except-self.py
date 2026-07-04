class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        left = 1
        for i,num in enumerate(nums):
            if i == 0:
                result[i] = 0
                left = num
            else:
                result[i] = left
                left *= num
        right = 0
        for i,num in enumerate(reversed(nums)):
            if i==0:
                right = num
            elif result[-i-1] == 0 and i==n-1:
                result[-i-1] = right
            else:
                result[-i-1] *= right
                right *= num
        return result
            