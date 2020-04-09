class Solution:
    def twoSum(self, nums, target):
        sumDict = {}
        for n in range(len(nums)):
            sumDict[nums[n]] = n
            if target-nums[n] in sumDict:
                return [sumDict[target-nums[n]], sumDict[nums[n]]]
        pass


print(Solution().twoSum([2, 7, 11, 15], 27))
