# enumerate on an iterable, returns a tuple of count along the way and object

example = ["left", "right", "up", "down"]

# for i in range(len(example)):
#     print(i, example[i])

# same output as above
for i, j in enumerate(example):
    print(i, j)


new_dict = dict(enumerate(example))

print(new_dict)

