class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        def hm(s):
            hashmap = {}
            for c in s:
                if c in hashmap:
                    hashmap[c] += 1
                else:
                    hashmap[c] = 1
            return hashmap.values()
        a = hm(str1)
        b = hm(str2)

        return a, b