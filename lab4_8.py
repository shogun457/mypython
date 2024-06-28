try:
    weight = float( input('กรุณากรอกน้ำหนัก (กิโลกรัม) : ') )
    height = float( input('กรุณากรอกความสูง (เซนติเมตร) : ') )
except:
    weight = 0
    height = 0

if weight > 0 and height > 0 :
    height_m = ( height / 100 ) ** 2
    bmi = weight / height_m
    print( 'น้ำหนักของคุณ คือ', weight )
    print( 'ความสูงของคุณ คือ', height )
    print( 'ค่า BMI หรือค่าดัชนีมวลกาย คือ %.2f' %bmi )

if bmi < 18.50:
    print("นํ้าหนักน้อย")
elif bmi >= 18.5 and bmi <= 22.90:
    print("ปกติสุขภาพดี")
elif bmi >= 23 and bmi <= 24.90:
    print("ท้วม/โรคอ้วนระดับ 1")
elif bmi >= 25 and bmi <= 29.90:
    print("อ้วน/โรคอ้วนระดับ 2")
elif bmi >= (30):
    print("อ้วนมาก/โรคอ้วนระดับ 3")