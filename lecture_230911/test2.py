class Solution:
    def towSum(self, nums, target):
        sorted_nums = nums[:]
        sorted_nums.sort()
        print(sorted_nums)
        print(nums)
        
        while left < right :
            left = 0
            right = len(sorted_nums)-1 
            if sorted_nums[left] + sorted_nums[right] == target:
                return
s= Solution()
s.twoSum(nums=[4, 1, 9, 7, 5, 3, 16], target=4)