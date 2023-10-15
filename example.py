def sweap_max(items: list) -> list:
  max_pos = items.index(max(items))
    # max_item = items[0]
    # max_pos = 0
    # for i in range(len(items)):
    #     if items[i] >= max_item:
    #         max_item = items[i]
    #         max_pos = i
    # temp = items[0]
    # items[0] = items[max_pos]
    # items[max_pos] = temp
  items[0], items[max_pos] = items[max_pos], items[0]
return items
a = [2, 4, 6, 19, 7, 43, 9, 3]
print(result)
