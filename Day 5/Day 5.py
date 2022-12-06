
def get_moves():
    shit = []
    moves = []
    with open("moves.txt", "r") as f:
        for line in f:
            shit.append(line)
    for x in shit:
        print(type(x))
        x.replace("move ", "")
        x.replace("from ", "")
        x.replace("to ", "")
        x.replace("\n", "")
        moves.append(x)

    print(moves)


get_moves()