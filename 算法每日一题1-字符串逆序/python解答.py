class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 方法一：
        # s = s[::-1]
        # print(s)
        # return s

        # 方法二： 用两个指针来判断
        right = len(s)-1
        left = 0
        while left<right:
            tmp = s[right]
            s[right] = s[left]
            s[left] = tmp
            right= right - 1
            left = left + 1
        print(s)
