def solution(order):
    order_dict = {
        "americano": [["iceamericano", "americanoice", "hotamericano", "americanohot", "americano", "anything"], 4500],
        "cafelatte": [["icecafelatte", "hotcafelatte", "cafelattehot", "cafelatteice", "cafelatte"], 5000],
    }
    answer = 0
    for ele in order:
        if ele in order_dict['americano'][0]:
            answer += order_dict['americano'][1]
        elif ele in order_dict['cafelatte'][0]:
            answer += order_dict['cafelatte'][1]
        else:
            print("메뉴에 존재하지 않는 상품입니다.")
    return answer