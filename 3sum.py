def threeSum(nums: list[int]):
        l = len(nums) 
        lst = []
        lst2 = []
        for i in range(l):
            for j in range(i+1, l):
                for k in range(j+1, l):
                    if (nums[i]+nums[j]+nums[k] == 0) and not all(x in lst2 for x in [nums[i], nums[j], nums[k]]):
                        lst.append([nums[i], nums[j], nums[k]])
                        lst2.extend([nums[i], nums[j], nums[k]])

        return lst
