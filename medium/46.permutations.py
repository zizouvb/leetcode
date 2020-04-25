class Solution:
    def permute(self, nums):
        permutations_list = []
        def permuteTail(current_index):
            if current_index == len(nums)-1:
                permutations_list.append(nums[:])
            for i in range(current_index, len(nums)):
                nums[current_index], nums[i] = nums[i], nums[current_index]
                permuteTail(current_index+1)
                nums[current_index], nums[i] = nums[i], nums[current_index]
        permuteTail(0)
        return permutations_list


print(Solution().permute([1, 2, 3]))
