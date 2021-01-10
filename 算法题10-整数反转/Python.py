class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            num = list(str(x))
            num.reverse()
            # print("".join(num))
            if int("".join(num)) > 2**31 -1 :
                return 0
            return int("".join(num))
        else:
            num = list(str(-x))
            num.reverse()
            if int("".join(num)) > 2**31 + 1 :
                return 0
            return int("-" + "".join(num) )
