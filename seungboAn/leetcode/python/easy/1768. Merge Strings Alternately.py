# https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
 

# Constraints:
# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 1. 길이가 작은 배열을 찾기
        lower = min(len(word1), len(word2))

        # 2. 작은 배열의 길이만큼 for문
        res = []
        for i in range(lower):
            res.append(word1[i])
            res.append(word2[i])
       
        # 3. 큰 배열의 남은 부분 추가
        res.append(word1[lower:])
        res.append(word2[lower:])

        res = "".join(res)

        # 4. 결과 반환
        return res
    
def main():
    sol = Solution()
    print(sol.mergeAlternately('abc', 'pqr'))

if __name__ == "__main__":
    main()