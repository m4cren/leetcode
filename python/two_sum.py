# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


class Solution(object):
 


     def twoSum(self, nums, target):
    
          
          lower_val = []


          #O(n - 1) + O(n log n)

          #sorting all the lower values than the target
          for i in range(len(nums)):
               if nums[i] < target:
                    lower_val.append(nums[i])

          

          #comparing eash sum of 2 elements
          print('Valid Answer: ')
  
          for i in range(len(lower_val) - 1):
               
               index = 0
               max_val = len(lower_val) - 1
               

               while index != max_val:
                    sum = lower_val[i] + lower_val[index + 1]
              
               
                    if sum == target:
                         
                
               
                         if  lower_val[i] == lower_val[index + 1]:
                
                              if index + 1 == len(lower_val) - 1:
                                   
                                   return [i, index + 1]
                              return [i, index + 2]
                         return [i, index + 1]
                              
                    else:
                         index += 1
               
          return 'No possible answer'



def main():
    sol = Solution()

    print(sol.twoSum([2,5,5,11], 10))


if __name__ == '__main__':
     main()


