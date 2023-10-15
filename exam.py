def sweap_max(items: list) -> list:
    max_pos = items.index(max(items))
    for i in range(len(items)):
        if items[i] >= max_item:
            max_item = items[i]
            max_pos = i
    # temp = items[0]
    # items[0] = items[max_pos]
    # items[max_pos] = temp
    items[0], items[max_pos] = items[max_pos], items[0]
    return items

a = [5, 6, 2, 3, 4, 21, 13]
result = sweap_max(a)
print(result)
