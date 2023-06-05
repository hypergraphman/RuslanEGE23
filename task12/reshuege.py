for x in range(30):
    for y in range(50):
        for z in range(22):
            if x + z == 23 and x + y + 2 * z == 48 and y + 2 * z == 41:
                print(x + y + z + 2)