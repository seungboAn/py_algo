class Solution():
    def odd_and_even_checker(self, n: int) -> None:
        if n % 2 == 0:
            print(f'{n} is even')
        else:
            print(f'{n} is odd')

if __name__ == "__main__":
    a = int(input())
    sol = Solution()
    sol.odd_and_even_checker(a)