
def get_data():
    raw_data = []
    with open("Puzzle Input.txt", "r") as f:
        for line in f:
            raw_data.append(line.replace("\n", ""))
    print(raw_data)

    data_def = []
    for n in raw_data:
        lol = n.split(",")
        print(n)
        for y in n:
            data_def.append(lol[y])
    print(lol)
    print(data_def)


get_data()