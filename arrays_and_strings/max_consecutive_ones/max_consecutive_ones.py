class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
      left = 0
      print(nums)
      zero_count, max_len = 0, 0
      for right in range(len(nums)):
          if nums[right] == 0:
            zero_count += 1
          
          while (left <= right and zero_count > k):
            if nums[left] == 0:
              zero_count -= 1
            left += 1
          max_len = max(max_len, right - left + 1)
      return max_len
    
    def betterSolution(self, nums, k):
      left = 0
      for right in range(len(nums)):
          # If we included a zero in the window we reduce the value of k.
          # Since k is the maximum zeros allowed in a window.
          if(nums[right] == 0):
            k -=1
          # A negative k denotes we have consumed all allowed flips and window has
          # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
          if k < 0:
              # If the left element to be thrown out is zero we increase k.
              if(nums[left] == 0):
                k += 1
              left += 1
      return right - left + 1

s = Solution()
res = s.longestOnes([0,0,0,1,1,0, 0,0,0], 2)
print("res:", res)

print("better res:", s.betterSolution([0,0,0,1,1,0, 0,0,0], 2))