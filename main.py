# 1-FAKTORIAL HISOBLAGICH
son = int(input("Son kiriting: "))
faktorial = 1

for i in range(1, son + 1):
    faktorial *= i

print(f"{son}! =", faktorial)

# 2-TESKARI MATN
matn = input("Matn kiriting: ")
print("Teskari matn:", matn[::-1])

# 3-UNLI HARFLAR SANAQI
matn = input("Matn kiriting: ").lower()
unlilar = "aeiou"
sanoq = 0

for harf in matn:
    if harf in unlilar:
        sanoq += 1

print("Unli harflar soni:", sanoq)

# 4-AMALLAR KALKULYATORI
a = float(input("1-sonni kiriting: "))
b = float(input("2-sonni kiriting: "))
amal = input("Amalni kiriting (+, -, *, /): ")

if amal == "+":
    print(a + b)
elif amal == "-":
    print(a - b)
elif amal == "*":
    print(a * b)
elif amal == "/":
    if b != 0:
        print(a / b)
    else:
        print("0 ga bo‘lish mumkin emas!")
else:
    print("Noto‘g‘ri amal!")

# 5-PALINDROM TEKSHIRUVCHI
soz = input("So'z kiriting: ").lower()

if soz == soz[::-1]:
    print("Bu palindrom")
else:
    print("Bu palindrom emas")

