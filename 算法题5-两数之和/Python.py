class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # num_left = nums[1:]
        index = []
        flag = False
        count = 0  # 用于记录第二个数字的下标
        # 遍历nums数组
        for i in nums:
            # 遍历除了这个数字以外的其他数字
            num_left = nums[nums.index(i)+1:]
            count = count + 1
            # print(num_left)
            for j in num_left:
                if i+j==target:
                    flag = True
                    index.append(nums.index(i))
                    # n = j
                    # 如果i和j相等的话，可能会出现下标一样
                    index.append(num_left.index(j) + count)
                    break
            if flag == True:
                break
        return index
