# 요구사항
# i번째 어린이가 extraCandies를 받았을 때 사탕을 가장 많이 가진 어린이보다 많거나 같은 경우 True, 적은 경우 False를 담은 배열 반환.
# candies : i번째 어린이가 가지고 있는 사탕 갯수를 표시한 배열
# extraCandies: 남는 사탕 갯수

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        greatestCandy = maxCandy - extraCandies
        res = [candy >= greatestCandy for candy in candies]
        return res