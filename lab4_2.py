#ชนิดข้อมูลแบบTuple --> Immutable
person = ("Weerachart",17,181,61,"6529011026@cdti.ac.th")
print(person)
#person[1] = 40
print("อายุ %d " % person[1])
print("ส่วนสูง %d น้ำหนัก %d " % (person[2],person[3]))
print("email %s "% person[4])

print(person[0:3])
print(person[2:4])
print(person[2:])
print(person[:4])
print(person[-4:-1])

