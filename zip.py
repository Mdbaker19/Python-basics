# aggregates lists into one sharing the idx

x = [1, 2, 3, 4]
y = [6, 4, 3, 2]
z = ["a", "b", "c", "d"]

for i, j in zip(x, y):
    print(i, j)

for i, j, k in zip(x, y, z):
    print(i, j, k)

for i in zip(x, y, z):
    print(i)

l = list(zip(x, y, z))
print(l)

dict = dict(zip(x, y))
print(dict)
# creates key value dictionary of lists

[print(x, y) for x, y in zip(x, y)]


for a, b in zip(x, y):
    print(a, b)
print("a is accessable still : ", a)  # a is stored

# when writing a loop like this values can be overwritten
print("x is: ", x)
for x, y in zip(x, y):
    print(x, y)
print("x is now: ", x)  # this x is now no longer the list it was but the last value in the
# list like the "a" above, just something to keep in mind with loops

