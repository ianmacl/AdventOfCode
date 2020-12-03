with open("advent1.txt", "r") as fhandle:
    digits = [int(x.strip()) for x in fhandle.readlines()]
print digits
for x in digits:
    for y in digits:
        remainder = 2020 - x - y

        if remainder < 2020 and remainder in digits:
            print x
            print y
            print remainder
            print x * y * remainder
