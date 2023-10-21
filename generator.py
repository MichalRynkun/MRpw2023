# evens = []
# for x in range (20):
#     if x % 2 == 0:
#         evens.append(x)
# print(evens)

# evens = [
#     x for x in range(20) if x % 2 == 0
# ]
#
# print(evens)

items = [1, 2, 3, 4, 5]
pairs = (
    x ** 2
    for x in items
    # a: b
    # for a in items
    # for b in items
    # if a < b
)
# for a in items:
#     for b in items:
#         pairs.append((a,b))
for pair in pairs:
    print(pair)

for pair in pairs:
    print(pair)