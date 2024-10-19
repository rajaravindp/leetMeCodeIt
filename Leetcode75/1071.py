class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        arr = list()
        def hm(s):
            hashmap = {}
            for c in s:
                if c in hashmap:
                    hashmap[c] += 1
                else:
                    hashmap[c] = 1
            return hashmap
        a = hm(str1)
        b = hm(str2)
        print(a, b)
        print(a.keys() == b.keys())
        if a.keys() == b.keys():
            for i in a.keys():
                   arr.append(i) 
            return "".join(arr)
        else:
            return ""
                    

str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"

s = Solution()
print(s.gcdOfStrings(str1, str2))