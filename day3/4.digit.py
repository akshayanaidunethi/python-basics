num = 5384

ones = num % 10
tens = (num // 10) % 10
hundreds = (num // 100) % 10
thousands = num // 1000

print("Thousands:", thousands)
print("Hundreds:", hundreds)
print("Tens:", tens)
print("Ones:", ones)
