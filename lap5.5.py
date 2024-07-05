def score():
    S = (A + b + c)
    return S

A = int(input("คะเเนนเก็บ: "))
if A > 20:
    print("ห้ามเกิน20")
else:
    b = int(input("คะเเนนจิพิตสัย: "))
    if b > 10:
        print("ห้ามเกิน10")
    else:
        c = int(input("คะเเนนกลางภาค: "))
        if c > 20:
            print("ห้ามเกิน20")
        else:
            print("คะเเนนรวม %.2f" % score())

