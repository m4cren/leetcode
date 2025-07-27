


class Solution(object):
    def romanToInt(self, s):

        romanMap = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

        value = 0

        for i in range(len(s)):
            if i < len(s)-1 and romanMap[s[i]] < romanMap[s[i+1]]:
                value -= romanMap[s[i]]
            else:
                value += romanMap[s[i]]
        

        return value

def main():
    sol = Solution()
    s = 'XIV'
    print(sol.romanToInt(s))

main()