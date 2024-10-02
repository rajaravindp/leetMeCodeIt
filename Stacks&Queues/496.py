class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = []
        map = {}

        for num in nums2:
            while stk and num > stk[-1]:
                num1 = stk.pop()
                map[num1] = num
            stk.append(num)
        
        while stk: 
           num = stk.pop()
           map[num] = -1
        return [map[num] for num in nums1]