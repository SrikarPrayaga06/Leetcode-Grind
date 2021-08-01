def twoSum(self, nums, target):
    # approach 1: brute force O(n^2) O(n) space * if there are for loops then o(n) space if no loops/recursion then its o(1)
    for x in range(len(nums)):
        for y in range(len(nums)):
            if nums[x]+nums[y]==target and x!=y:
                return [x,y]
    # approach 2: O(n) time and o(n) space
    for x in range(len(nums)):
        xda=set()
        if target-nums[x] in xda:
            return [x,nums.index(target-nums[x])]
        else:
            xda.add(nums[x])


    
    