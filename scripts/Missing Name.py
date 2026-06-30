import os

files = os.listdir()
numbers = []

for f in files:
    if f.endswith(".jpg"):
        name = os.path.splitext(f)[0]
        if name.isdigit():
            numbers.append(int(name))

numbers = sorted(numbers)

missing = []
for i in range(1, max(numbers)+1):
    if i not in numbers:
        missing.append(i)

print("Jumlah file:", len(numbers))
print("Nomor terbesar:", max(numbers))
print("Angka yang hilang:")
print(missing)
