import math
def calculate_circle_area(radius):
    # คำนวณพื้นที่วงกลมโดยใช้สูตร π * r²
    area = math.pi * radius**2
    return area

radius = float(input("ป้อนรัศมีของวงกลม: "))
circle_area = calculate_circle_area(radius)
print(f"พื้นที่ของวงกลมที่มีรัศมี {radius} คือ {circle_area:.2f}")