# ADINDA YECINTHYA NURLIYANTI_222410102025
# TUGAS MEMBUAT CODE BMI CALCULATOR

Name = str(input("Enter Your Name : "))
Weight = int(input("Your Weight (kg) : "))
Height = float(input("Your Height (m) : "))

BMI = Weight/(Height**2)

print("Hello, ", Name)
print("Your BMI is ", format(round(BMI, 2)), "so you're ", end='')

if BMI < 18.5:
    print("In underweight condition :(")
elif 18.5 <= BMI < 24.9:
    print("In normal Weight condition :)")
elif 25.0 <= BMI < 29.9:
    print("In overweight condition :<")
elif 30.0 <= BMI < 34.9:
    print("In obesity Class I condition :<")
elif 35.0 <= BMI < 39.9:
    print("In obesity Class II condition :<")
else:
    print("In obesity Class III condition :<")