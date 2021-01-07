class Solution:
    def firstUniqChar(self, s: str) -> int:
        container = []
        for i in s:
            container.append(i)
        test = container[:]
        dellist = []
        for i in test:
            container.remove(i)
            if (i in container) or (i in dellist):
                dellist.append(i)
            else:
                return test.index(i)
        return -1
