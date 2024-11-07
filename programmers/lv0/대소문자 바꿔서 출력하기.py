class Solution():
    def alphabet_converter(self, string: str) -> None:
        res = list(map(lambda x: x.lower() if 65 <= ord(x) <= 90 else x.upper(), string))
        print("".join(res))

if __name__ == "__main__":
    str = input()
    sol = Solution()
    sol.alphabet_converter(str)