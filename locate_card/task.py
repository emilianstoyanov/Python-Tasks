def locate_card(cards, query):
    index = 0

    while True:
        if cards[index] == query:
            return index
        index += 1
        if index == len(cards):
            return -1


print(locate_card([9, 5, 4, 7, 0, 11, 6, 1], 1))
