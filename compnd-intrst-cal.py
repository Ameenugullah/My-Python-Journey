# Python compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Please Enter principle amount: "))
    if principle < 0:
        print("principle can't be less than zero")
    else:
        break
while True:
    rate = float(input("Please Enter rate amount: "))
    if rate < 0:
       print("rate can't be less than zero")
    else:
        break


while True:
     time = int(input("Please Enter time in years: "))
     if time < 0:
        print("Time can't be less than zero")
     else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")
