class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        ans =[1 for i in nums]
        for i in range (len(nums)):
            ans = [nums[i] * ans[x] if i != x else ans[x] for x in range(len(ans))]
        return ans
        """
        [1,2,3,4]
        [4,3,2,1]

        ans = [1]*len(nums)
        prefix =1
        postfix = 1
        nums_r = list(reversed(nums))
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *=nums[i]

        for i in range(len(nums_r)):
            ans[-1-i]*=postfix
            postfix*=nums_r[i]
        return ans
