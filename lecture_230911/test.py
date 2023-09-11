# list 구조형

def solution(nums, target) :
    n = len(nums)
    for i in range(n) :
        for j in range(i + 1, n) :
            if nums[i] + nums[j] == target :
                return[i, j]

print(solution(nums = [4, 1, 9, 7, 5, 3, 16], target=14))



# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             num2 = target - nums[i]
#             if num2 in nums[i+1:]:
#                 j = nums[i+1:].index(num2) + (i+1)
#                 return [i, j]