class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        ans =[]
        for s1 in strs:
            ans1 =[]
            for s2 in strs:
                if (sorted(s1))==(sorted(s2)):
                    ans1.append(s2)
            if(ans1) not in ans:
                ans.append(ans1)
        return ans
        """
        dict_str = {}
        for s in strs:
            if(dict_str.get("".join(sorted(s)),0)):
                dict_str["".join(sorted(s))].append(s)
            else:
                dict_str["".join(sorted(s))] = [s]

        return [l for l in dict_str.values()]
