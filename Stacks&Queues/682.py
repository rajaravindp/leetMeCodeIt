class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in operations:
            if i == "C":
                res = res[:-1]
            if i == "D":
                res.append(int(res[-1]) * 2)
            if i == "+":
                res.append(int(res[-1]) + int(res[-2]))
            if i not in ['C', 'D', '+']:
                res.append(int(i))

        cnt = 0
        for i in res:
            cnt += i
        return cnt