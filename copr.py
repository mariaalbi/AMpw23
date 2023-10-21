# events = []
# for x in range(20):
#     if x % 2 == 0:
#         events.append(x)
# print(events)

evens = [
    x for x in range(20) if x % 2 == 0
]
#print(evens)

items = [1, 2, 3, 4, 5]
pairs = {
    (a,b)
    for a in items
    for b in items
    if a < b
}
# for a in items:
#     for b in items:
#         pairs.append((a,b))
#
#print(pairs)

items2 = [1, 2, 3, 4, 5]
pairs2 = (
    x ** 2
    for x in items2
)
for pair2 in pairs2:
    print(pair2)

for pair2 in pairs2:
    print(pair2)