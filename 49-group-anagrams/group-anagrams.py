class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        result = []
        for i,num in enumerate(strs):
            result.append(sorted(num))
            result[i] = "".join(result[i])
            if result[i] in my_dict:
                my_dict[result[i]].append(num)
            else:
                my_dict[result[i]] = [num]
        return list(my_dict.values())