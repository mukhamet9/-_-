class Building:
    total = 0
    def __init__(self):
        Building.total += 1

for n in range(40):
    print(Building())
