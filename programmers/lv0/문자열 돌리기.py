class Solution():
    def string_rotator(self, string: str) -> None:
        res = [char + '\n' for char in string]
        print("".join(res))

if __name__ == "__main__":
    str = input()
    sol = Solution()
    sol.string_rotator(str)