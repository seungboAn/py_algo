class Solution():
    def input_printer(self) -> None:
        try:
            a, b = map(int, input().strip().split(' '))
            print(f'a = {a}\nb = {b}')
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    sol = Solution()
    sol.input_printer()