## SZYFR CEZARA
## Alfabet Python (A-Z), (26 liter)

## Funkcja ord zwraca kod accil danego znaku
## Accil na dużych literach (od 65 do 90)
# 
##Funkcja chr()
##Zwraca kod donego kodu accil

# Wypisz pętlą range alfabet

# for i in range(65, 91):
#   print(chr(i), end=" ")

# Jak słowo rozbić na litery

## len zwraca długość napisu
# napis = "POLSKA"
# print(len(napis[0]))

#Wypiszcie kody accill literek napisu: "POLSKA"

# napis = "POLSKA"
# print(len(napis[0]))

# for i in range(len(napis)):
#   print(ord(napis[i]))

# napis = "MAREK"
# print(len(napis[0]))

# for i in range(len(napis)):
#   print(chr(65 + (ord(napis[i])-65+3)%26),end="")
 
##Chalange




#a = int(input())
#b = int(input())
#c = int(input())
#d = int(input())
#o = b * d
#k, l = b, d

#suma = 0
#suma2 = 0
#mno1 = 0
#mno2 = 0
#if b == d:
   #suma = a+c
   #print(suma, "/", b)
#else:
   #while b != d :
     #if b > d : b = b - d
     #if d > b : d = d - b 
  
   #mno = o/b
  # mno1 = mno // k
  # mno2 = mno // l
  # suma2 = (a*mno1) + (c*mno2)
  # print(suma2, "/", mno)


#Zadanie 1

# a = int(input())
# b = int(input())
# c = int(input())


# g = b-a
# h = b / a


# if g == c - b:
#   print("arytmetyczny TAK")
# else:
#   print("arytmetyczny NIE")
# if h == c / b:
#   print("geometryczny TAK")
# else:
#   print("geometryczny NIE")
# if a < b and b < c:
#   print("rosnący TAK")
# else:
#   print("rosnący NIE")  
# if a > b and b > c:
#   print("malejący")
# else:
#   print("malejący NIE")

# Zadanie 2
# suma = 0
# suma2 = 0
# for i in range(100, 1000):     
#   if i % 8 == 0:
#     suma += i
#   if i % 16 == 0:
#     suma2 += i
# print(suma-suma2)

#Zadanie 3
# a = 0
# b = 0
# for i in range(10, 100,):
#   if i % 7 == 0:
#     a = i
  
# print(a)

# for k in range(1000, 10000):
#   if k % a == 0:
#     b = b + 1
    
# print(b)
#Zadanie 4


# b = 0


# for i in range(10, 100):
#   cd = i // 10
#   cj = i % 10
#   if cd >= cj *2:
#     b = b + 1
# print(b)

#Zadanie 5
# b = 0
# suma = 0
# for i in range(100, 1000):
#   cs = i // 100
#   a = i % 100
#   cj = i % 10
#   cd = a // 10
#   if cd + cj < cs:
#     b += 1
#     suma += i
    
  
# print("ilość:",b,"Suma:", suma)

#Zadanie 6


# n = int(input())
# suma = 0
# licznik=0
# for i in range(10, 100):
#   if i % 19 == 0: 
#     suma = suma + 19
#     licznik+=1
#   if licznik == n:
#     break
# print(suma)


#zadanie 7


# n = int(input())
# suma = 0
# licznik=0
# for i in range(1000, 100, -1):
#   if i % 37 == 0: 
#     suma = suma + i
#     licznik+=1
#   if licznik == n:
#     break
# print(suma)

# Zadanie 8
# n = int(input())
# suma = 0
# a = 2
# b = 5
# c = 8
# d = 0
# e, f, g = a, b, c
# h, i, j  = a, b, c

# for i in range(n):
#   d = (b + c) - a
#   a = c
#   b = d
#   c = b + 3
#   suma += e
#   e = a
#   f = b
#   g = c
# print(suma)

#Zadanie 10

