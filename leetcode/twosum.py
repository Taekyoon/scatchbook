class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                print(j)
                if nums[i] + nums[j] is target:
                    return [i, j]

        return []

sol = Solution()

print(sol.twoSum([2, 7, 11, 15], 9))
