import itertools
B = (False, True)
with open("output.txt", "w") as file:
    for x1,x2,x3 in itertools.product(B, B, B):
        if (((not x1) and x2 and (not x3)) or ((not x1) and x2 and x3) or (x1 and (not x2) and (not x3))):
            print(f"{x1} {x2} {x3}", file=file)