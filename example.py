def sweap_max(items: list) -> list:
    max_item = items[0]
    max_pos = 0
    for i in range(len(items)):
        if items[i] >= max_item:
            max_item = items[i]
            max_pos = i
    temp = items[0]
    items[0] = items[max_pos]
    items[max_pos] = temp
    return items
a = [2, 4, 6, 19, 7, 43, 9, 3]
result = sweap_max(a)
print(result)
