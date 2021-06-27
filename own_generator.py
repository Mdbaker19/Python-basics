# generators save memory but is slower typically
# generators yield things not return

def simple_gen():
    yield "Oh"
    yield "Hello"
    yield "there"


for i in simple_gen():
    print(i)

correct_combo = (4, 3, 8)
found = False
for c1 in range(10):
    if found:
        break
    for c2 in range(10):
        if found:
            break
        for c3 in range(10):
            if (c1, c2, c3) == correct_combo:
                print("Found Combo: {}".format((c1, c2, c3)))
                found = True
                break
            print(c1, c2, c3)


# this is the same as above, runs until found and breaks at the solve, cleaner with the gen code
def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield c1, c2, c3


for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == correct_combo:
        print("Found Combo: {}".format((c1, c2, c3)))
        break
    print(c1, c2, c3)
