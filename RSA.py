##

# from math import gcd

# print(gcd(15,20))




# 1. wybor 2 liczb pierwszych
p = 11
q = 13
print(p,q)

#2. 

n=p*q
f=(p-1)*(q-1)
print(n)
print(f)

from math import gcd

for i in range(2,f):
  if gcd(i,f)==1:
    e = i
    break
print(e, n)



#4.generujemy klucz prywatny d taki ze d * e % f rowna sie 1

for j in range (2,f):
  if j*e%f==1:
    d = j
    break
    
print(d,n)

# JAK SZYFROWAĆ
# mamy m - wiadomosc
# c = m**e % n (c - cipher - szyfrogram, tekst zaszyfrowany)
#t = c**d % n (t - text jawny - znow wiadomosc m)

m = input()
cipher = ""
for i in m:
  cipher += chr((ord(i)**e)%n)

print(m)
print(cipher)

tekst=""

for i in cipher:
  tekst += chr((ord(i)**d)%n)
print(tekst)









