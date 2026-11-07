class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixs = {}
        postfixs = {}
        products = []
        prefixs[0] = 1
        l = len(nums)
        postfixs[l] = 1
        m = l 
        for n in range(len(nums)):
            if n > 0:
                prefixs[n] = prefixs[n-1] * nums[n - 1]
            if l < len(nums):
                postfixs[l] = postfixs[l+1] *  nums[l]
            l-=1
        for n in range(len(nums)):
            products.append(prefixs[n] * postfixs[n+1])
        return products