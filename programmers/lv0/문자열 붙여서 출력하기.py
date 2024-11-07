class Solution():
    def string_merge(self, str1: str, str2: str) -> None:
        print(str1 + str2)

if __name__ == "__main__":
    str1, str2 = input().strip().split(' ')
    sol = Solution()
    sol.string_merge(str1, str2)