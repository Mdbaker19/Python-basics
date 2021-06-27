xyz = [i for i in range(5)]  # this is stored as a list, list comprehension, more memory but faster

# same as

xyz = []
for i in range(5):
    xyz.append(i)

xyz = (i for i in range(5))  # this is a generator to be iterated over, not stored into memory but is slower
for i in xyz:
    print(i)

input_list = [5, 6, 15, 25, 9, 8, 3, 30]


def div_by_five(num):
    return num % 5 == 0


xyz = (i for i in input_list if div_by_five(i))  # not making a list
for i in xyz:
    print(i)

xyz = []  # list version same thing
for i in input_list:
    if div_by_five(i):
        xyz.append(i)

print(xyz)

[print(i) for i in xyz]  # list comprehension -> "one liner for loop"


[[print(i,ii) for ii in range(5)] for i in range(5)]  # 0 0, 0 1, 0 2, .... 1 0, 1 1, 1 2,...5 4, 5 5
#  SAME THING
for i in range(5):
    for ii in range(5):
        print(i, ii)



