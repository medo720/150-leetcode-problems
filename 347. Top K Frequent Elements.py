class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            dic [i] = 1+dic.get(i,0)

        sorted_list = sorted(dic.items(),key = lambda item:item[1],reverse = True)
        ans =[]
        for i in range(k):
            ans.append(sorted_list[i][0])
        return ans
            
