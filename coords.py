def coords(x, y):
    if x > 0 and y > 0:
        print("|")
    if x < 0 < y:
        print('||')
    if x < 0 and y < 0:
        print("|||")
    else:
        print("|V")

coords(4, -3)
