# For loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

for x in reversed(range(1, 11)):
   print(x)
print("HAPPY NEW YEAR")

credit_card = "1234-8750-8065-7890"
for x in credit_card:
    print(x)

for x in range(1, 30):
    if x == 15:
        continue
    else:
        print(x)
    if x == 25:
        break
    else:
        print(x)