# print_command - shows how the print() function work

print("Hello world!", end=" * ")    # end określa znak na zakończeniu lini
print("Hello Mars!")
print("\tHello\n\"Venus!\"")        # niedrukowany znak \n to przejście do nowego wiersza 
                                    # niedrukowany znak \t to tabulator
                                    # aby wywietlić cudzysłów musimy uźyć \" backslash przed znakiem cudzysłowu
print('Hello "Venus!"')             # albo zmienić znak cudzysłowu wskazujący ciąg znaków na ' '
print("A","u","t","o", sep="-")     # sep określa znak wstawiany pomiędzy ciągami znaków
print("A" + "u" + "t" + "o")        # inny sposób łączenia ciągów znakowych to operator + ; sep nie ma znaczenia
print("#" + "F"*6)                  # mzoemy powielić wyświetlany znak (ciąg) za pomocą operatora * oraz 
                                        # liczby określającej wielokrotność powtózeń 