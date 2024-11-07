class Solution():
    def user_input_add(self) -> None:
        try:
            a, b = map(int, input().strip().split(' '))
        except ValueError as e:
            print(e)
        else:
            print(f'{a} + {b} = {a + b}')

if __name__ == "__main__":
    sol = Solution()
    sol.user_input_add()