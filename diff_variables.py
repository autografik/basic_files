# diff_variables.py presents different variables 
# and what we can to do with them
ch = "-"
v1 = 6
v2 = 4
# podstawowe działania na zmiennych
print("\n\tPodstawowe działania na zmiennych\n")
print(v1, "+", v2, "=", v1 + v2)
print(v1, "-", v2, "=", v1 - v2)
print(v1, "*", v2, "=", v1 * v2)
print(v1, "/", v2, "=", v1 / v2)
print(f"{v1} % {v2} = {v1 % v2}")
print(f"{v1} ** {v2} = {v1 ** v2}")

# wypisanie typów uzytych zmiennych
print("\n" + ch*35 + "\n")
print("\tUkazanie typów zmiennych\n")
v3 = 1
v4 = 1.5
v5 = True
v6 = "text"
print("v3 = ", v3, type(v3))
print("v4 = ", v4, type(v4))
print("v5 = ", v5, type(v5))
print("v6 = ", v6, type(v6))
v3 = "jeden"
v6 = 2.0
print("v3 = ", v3, type(v3))
print("v6 = ", v6, type(v6))

# przypisanie wywołania jakiejś funkcji(przekazanie parametrów)
print("\n" + ch*35 + "\n")
print("\tPrzypisać wywołanie funkcji do zmiennej\n")
drukuj = print
drukuj("Zmienna drukuj ma przypisane wywołanie funkcji print, a zatem...")
drukuj("...czy drukuj wpisze sumę?")
drukuj("\t" + "\n",v1, "+", v2, "=", v1+v2,"" + "\tWYPISAŁO! :)")

# Odkrycie miejsca przechowywania zmiennej
print("\n" + ch*35 + "\n")
print("\tUjawnić adresy komórek pamięci przechowujące zmienne\n")
v10 = "abc"
print(v10, id(v10))
v11 = "abc"
print(v11, id(v11))
v12 = 64
print("",v12, id(v12))
v13 = 64
print("",v13, id(v13))
v13 = 61
print("",v13, id(v13))
v13 = 61
print("",v13, id(v13))
v14 = 512
print(v14, id(v14))
v15 = 512
print(v15, id(v15))

# nadanie nowych wartości róznym zmiennym w pojedynczym przypisaniu
print("\n" + ch*35 + "\n")
print("\tPrzypisać nowe wartości zmiennym w jwdnej linii kodu\n")
v7 = 6
v8 = 9
print("Pierwotne wartości:  ",v7, v8)
v7, v8 = v8+3, v7-1
print("     Nowe wartości: ",v7, v8)

# jedna wartość w rónych systemach liczbowych
print("\n" + ch*35 + "\n")
print("\tTa sama wartość zdefiniowana w rómych systemach liczbowych\n")
int1 = 256          # dziesiętny
int2 = 0x100        # szesnastkowy
int3 = 0o400        # ósemkowy
int4 = 0b100000000  # binarny
print("",int1,"dec\n", int2,"hex\n", int3,"okt\n", int4,"bin")

# liczba zmiennoprzecinkowa
print("\n" + ch*35 + "\n")
print("\tPrezentacja liczby zmiennoprzecinkowej z uycziem kropki diesiętnej i wykładnika\n")
re1 = 100.
re2 = 0.10
re3 = .10
re4 = 1e3
print(" ", re1,"\n   ", re2,"\n   ", re3,"\n", re4)

# przypisanie zmiennym wartości pobranych z klawiatury
print("\n" + ch*35 + "\n")
print("\tMona pobrać dane z klawiatury i przypisać je do zmiennej\n")
txt = input("Wpisz dowolny tekst: ")
print("\nWpisałeć: ",txt,"\n\n")
num1 = int(input("Pierwsza liczba:"))
num2 = float(input("Druga liczba:"))
print("\nInterpreter zamienia drugą liczbę na zmiennoprzecinkową\n"
      + "dlatego wynik te jest liczbą zniennoprzecinkową\n")
print(f"{num1} + {num2} = {num1+num2}")