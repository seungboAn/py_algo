# flowerbed 배열에서 화분이 비어있는 경우 0, 비어있지 않은 경우 1로 표시한다.
# 꽃은 인접한 곳에 화분이 비어있지 않으면 심을 수 없다.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        lenFlowerbed = len(flowerbed)
        if lenFlowerbed == 1:
            if flowerbed[0] == 0:
                n -= 1
            return n <= 0
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1
        for i, value in enumerate(flowerbed):
            if i == 0 or i == lenFlowerbed - 1 or value == 1:
                continue
            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0