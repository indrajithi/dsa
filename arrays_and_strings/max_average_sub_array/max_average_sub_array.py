class Solution:
    def findMaxAverage(self, nums, k):
        currSum = maxSum = sum(nums[:k])
        
        for i in range(k, len(nums)):
          currSum += nums[i] - nums[i - k]
          
          maxSum = max(maxSum, currSum)
        
        print(maxSum / k)
s = Solution()
s.findMaxAverage([1, 12, -5, -6, 50, 3], 4)