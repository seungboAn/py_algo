class Solution():
    def loop_printer(self, string: str, n: str) -> None:
        try:
            n = int(n)
        except ValueError as e:
            print(e)
        else:
            print(string * n)

if __name__ == "__main__":
    string, n = input().strip().split(' ')
    n = int(n)
    sol = Solution()
    sol.loop_printer(string, n)