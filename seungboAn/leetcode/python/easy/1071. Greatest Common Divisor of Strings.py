# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 
# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

# Constraints:
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.

import math

class Solution():
    def gcd(self, str1, str2):
        # s = str1 if len(str1) > len(str2) else str2
        if len(str1) > len(str2):
            s = str1
            t = str2
        else:
            s = str2
            t = str1
        flag = False
        divider = []
        # while True:
        #     if flag == True:
        #         break
        #     for i in range(len(t)):
        #         divider.append(t[i])
        'a' 'aaa'
                
        res = "".join(divider)
        return res
            

def main():
    sol = Solution()
    print(sol.gcd('abc', 'abcabcd'))

if __name__ == '__main__':
    main()