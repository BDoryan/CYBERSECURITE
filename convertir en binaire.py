def toBinary(number):
    return bin(number)[:1:-1];

number=int(input("Conversion en binaire : "))
binary=toBinary(number)
print("Binaire : ", binary)
