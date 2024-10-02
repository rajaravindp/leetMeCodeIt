class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_str(z):
            res = []
            for i in z:
                if i != "#":
                    res.append(i)
                elif res:
                    res.pop()
            return res
        return process_str(s) == process_str(t)