class Solution:
    # 
    # 判断一个数是否为回文数，返回True或者False
    # def huiwen(int n):
    #     res = False
    #     """
    #     回文数判断方法
    #         可以通过
    #     """
    #     # if 
    #     return res
    # 先找回文数，后找素数（回文数的范围要比素数小）
    def primePalindrome(self, N: int) -> int:
        # num = [1,2,3,4,5]
        # print(list(str(N)))
        # start = list(str(N))
        # print(start)
        # end = start[::-1]
        # if start == end:
        #     print("回文数")
        # else:
        #     print("非回文数")
        def Prime(n):
            if n == 1:
                return False
            result = True
            i = 2
            # while i <= n / 2:
            #     if n % i == 0:
            #         result = False
            #         break
            #     i = i + 1
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    result = False
                    break
            return result

        flag = True
        i = N
        while flag == True:

            if 10 ** 3 <= i < 10 ** 4:
                i = 10 ** 4
                continue
            if 10 ** 5 <= i < 10 ** 6:
                i = 10 ** 6
                continue
            if 10 ** 7 <= i < 10 ** 8:
                i = 10 ** 8
                continue
            start = list(str(i))
            end = start[::-1]
            if start == end:
                if Prime(i):
                    flag = False
                    return i
            i = i + 1
