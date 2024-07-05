def fahrenheit (C):
    F = (9/5) *C + 32
    return F

def kelvin (C):
    K = C + 273.15
    return K

C = int(input("รับองศาเซลเซียส: "))
print("องศาฟาเรนไฮส์ %.2f" % fahrenheit(C))

C = int(input("รับองศาเซลเซียส: "))
print("องศาเคลวิน %.2f" % kelvin(C))