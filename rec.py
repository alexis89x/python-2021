def recursive(x):
    print(x)
    print(recursive(x+1))
    if x >= 10:
        return


recursive(0)