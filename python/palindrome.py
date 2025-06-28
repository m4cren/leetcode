class Solution(object):


    def isPalindrome(self, number):

        num_string = str(number)

        num_array = [num_string[i] for i in range(len(num_string))]

        reverse_array = [num_string[len(num_string)-1 - i] for i in range(len(num_string))]

        
        



        if num_array == reverse_array:
            return True
        else: 
            return False


        

    
def main():

    sol = Solution()

    sol.isPalindrome(1221)

main()