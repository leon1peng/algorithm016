
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = dict()
        for char in strs:
            temp = "".join(sorted(list(char)))
            if temp in hash_map.keys():
                hash_map[temp].append(char)
            else:
                hash_map[temp] = [char]
        return list(hash_map.values())
