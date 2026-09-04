class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash_map = {}

        t_hash_map = {}

        for char in s:
            if char in s_hash_map:
                s_hash_map[char] += 1
            else:
                s_hash_map[char] = 1

        for char in t:
            if char in t_hash_map:
                t_hash_map[char] += 1
            else:
                t_hash_map[char] = 1

        return t_hash_map == s_hash_map
