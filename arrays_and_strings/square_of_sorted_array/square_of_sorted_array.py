class Solution:
    def sortedSquares(self, nums):
      start = 0
      while start <= len(nums) - 1:
        nums[start] *= nums[start]
        start += 1
      return nums.sort()
    
    def betterSortedSquares(self, nums):
      n = len(nums)
      res = [0] * n
      
      start = 0
      end = n - 1
      n -= 1
      
      while start <= end:
        if (abs(nums[start]) < abs(nums[end])):
          res[n] = nums[end] * nums[end]
          end -= 1
        else:
          res[n] = nums[start] * nums[start]
          start += 1
        
        n -= 1
      return res
    
    def dequeSolution(self, nums):
      from collections import deque
      res = deque()
      start, end = 0, len(nums) - 1
      
      while start <= end:
        if (abs(nums[start]) < abs(nums[end])):
          res.appendleft(nums[end] * nums[end])
          end -= 1
        else:
          res.appendleft(nums[start] * nums[start])
          start += 1
        
      return res
      
        
        
        

if __name__ == "__main__":
  s = Solution()
  print("Time complexity: O(n log(n) \nSpace complexity: O(1) ")
  arr = [-4,-1,0,3,10]
  s.sortedSquares(arr)
  print(arr)
  
  print("\nTime complexity O(N), Space O(N)")
  print(s.betterSortedSquares([-4,-1,0,3,10]))
  
  print("Deque Solution")
  print(s.dequeSolution([-4,-1,0,3,10]))
  
  