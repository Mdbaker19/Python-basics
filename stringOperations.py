import os


def string_methods():
    names = ["matt", "mandy", "nemo"]

    for name in names:
        print(name + ", ")

    print(", ".join(names))

    location_of_files = "C:\\Users\\H\\Desktop\\Intermediate Python"
    file_name = "example.txt"

    print(location_of_files + "\\" + file_name)

    # with open(os.path.join(location_of_files, file_name)) as f:
    #     print(f.read())

    who = "matt"
    how_many = 12

    print(who, "bought", how_many, "apples")
    print("{} bought {} apples".format(who, how_many))
