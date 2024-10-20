from typing import List
from collections import defaultdict

class Solution:
    def compress(self, chars: List[str]) -> int:
        # map = defaultdict(int)

        # for i in range(0, len(chars)):
        #     if chars[i] not in map:
        #         map[chars[i]] += 1
        #     else:
        #         map[chars[i]] += 1
        
        # arr = list()
        # for key, val in map.items():
        #     arr.append(key)
        #     arr.append(str(val))
        # chars = arr
        # return chars, len(arr) 



chars = ["a","a","b","b","c","c","c"]
s = Solution()
print(s.compress(chars))