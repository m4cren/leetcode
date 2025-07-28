class Solution(object):

    def removeElement(self, nums, val):

        expectedNum = nums
        
        for i in nums[:]:
            
            if i == val:
                expectedNum.remove(val)

        k = len(expectedNum)

        for i in range(k):
             nums[i] = expectedNum[i] 
   
        return k


def main():
    sol = Solution()
    print(sol.removeElement([3,2,2,3], 3))

main()