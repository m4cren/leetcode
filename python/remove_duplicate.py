class Solution(object):

    def removeDuplicates(self, nums):
        expectedNums = []
        if isinstance(nums, list):

            for i in nums:
                if i not in expectedNums:
                    expectedNums.append(i)

            
            

            k = len(expectedNums)

            for i in range(k):
                nums[i] = expectedNums[i]

            print(nums)
            return k

        else:
            print('invalid type of parameter')
            return
    



def main():
    sol = Solution()
    sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])

main()