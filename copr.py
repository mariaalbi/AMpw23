# events = []
# for x in range(20):
#     if x % 2 == 0:
#         events.append(x)
# print(events)

evens = [
    x for x in range(20) if x % 2 == 0
]
print(evens)

items = [1, 2, 3, 4, 5]
pairs = [
    (a,b)
    for a in items
    for b in items

]
# for a in items:
#     for b in items:
#         pairs.append((a,b))
#
print(pairs)