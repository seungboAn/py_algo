# 요구사항
# 문자열 속 모음 알파벳들을 reverse해서 반환
# 영어 모음은 a, e, i, o, u이다

# 풀이 과정
# 1. vowels를 set 자료형으로 만든다.
# 문자열의 각 문자가 vowels에 해당하는 지 탐색할 때 시간복잡도는 list의 경우 O(n), set은 O(1)이다.

# 2. 투 포인터를 사용해서 앞, 뒤에서 동시에 시작한다. 모음을 찾게 되는 경우, 두 요소의 위치를 바꾼다.
# 투 포인터를 사용하면 1개의 포인터를 사용해서 모음에 해당하는 요소를 배열로 다시 만들고 reverse 시킨 후 다시 문자열로 만드는 과정보다 공간 복잡도가 낮다.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        start, end = 0, len(s) - 1
        s = list(s)

        # continue를 사용해서 투 포인터를 모음에 해당될 때까지 이동시킨다.
        while start < end:
            if s[start] not in vowels:
                start += 1
                continue
            elif s[end] not in vowels:
                end -= 1
                continue
            else:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        s = ''.join(s)
        return s
            
