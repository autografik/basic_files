# conditional_statement.py show how the if() statement works   

# ustalenie pełnoletniości
ch = "_-_"
year_birth = int(input("Podaj rok urodzenia:"))
current_year = 2023
age = current_year - year_birth
print("\nTwój wiek: ", age, "lat(a)")
if age >= 18:
  print("Jesteś pełnoletni")
else:
  print("Jesteś niepełnoletni")

print("\n",ch * 20,"\n")

# sprawdzenie znaku dwuch liczb
x = 1
y = 3
print("x = ", x, "; y = ",y)
if x > 0 and y >0:  # jeśli x>0 i y>0 to obie dodatnie
  print("obie dodatnie")

print("\n",ch * 20,"\n")

# porównanie dwuch liczb o róznych typach danych
num1 = 10
num2 = 10.
print("Porównanie liczby 10 typu integer i typu float:\n")
print(f"Zmienna num1: {num1}")
print(f"Zmienna num2: {num2}")
print("\n")
if num1 == num2:    # jeśli wartość num1 = num2 wypisz to ze równe
  print(f"1. {num1} = {num2} - wartości są jednakowe... ")
if num1 is num2: 
  print(f"2. {num1} is {num2} - ale nie są identyczne, bo Python odwołuje się do innych komurek w pamieci.")     # int jest zapisany w innym obszarze pamięci niz float // brak wydruku
if num1 is not num2:
  print(f"3. {num1} is not {num2} - ale nie są identyczne, bo Python odwołuje się do innych komurek w pamieci.") # int jest zapisany w innym obszarze pamięci niz float dlatego jest wydruk
num2 = int(num2)    # konwersja float do int
if num1 is int(num2):
  print(f"4. {num1} is {num2} - po konwersji do float do int wartości są rozpoznawane jako identyczne") # num 1 jest identyczne z num2

print("\n",ch * 20,"\n")

# sprawdzenie czy podana liczba jest parzysta
number = float(input("Podaj liczbę:"))
if number % 2 == 0:
  print(f"Liczba {number} jest parzysta.")
else:
  print(f"Liczba {number} nie jest parzysta.")
  print("\nSprawdzenie bloku kodu przyniosło porządany efekt.")

print("\nDobra robota, synu!")