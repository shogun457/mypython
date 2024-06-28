kg = int(input("นํ้าหนัก"))
cm = int(input("ส่วนสูง"))
bmi = kg/(cm/100)**2
print (bmi)

if bmi < 18.50:
        print("นํ้าหนักน้อย")
elif bmi >= 18.5 and bmi <= 22.90:
        print("ปกติสุขภาพดี")
elif bmi >=23.00 and bmi <= 24.90:
        print("อันตรายระดับ1")
elif bmi >=25.00 and bmi <= 29.90:
        print("อันตรายระดับ2")           
else:
        print("อันตรายระดับ3")
    
    
    
