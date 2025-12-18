class Solution(object):
    def maxProduct(self, nums):
        res = max(nums)
        minp = maxp = 1
        for i in nums: 
            curr = i * maxp
            maxp = max(curr, i * minp, i)
            minp = min(curr, i* minp, i)

            res = max(res, maxp)
        
        return res

        