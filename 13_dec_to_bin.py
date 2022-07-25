def DecToBin(n):
    lstBin = []
    while n > 0:
        lstBin.append(str(n % 2))
        n //= 2
    return "".join(lstBin[::-1])


dec = int(input("Задайте число для перевода в двоичную систему -> "))
print(DecToBin(dec))