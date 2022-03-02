FileSetA = open('inputA.txt', 'r')
FileSetB = open('inputB.txt', 'r')
FileSetManipulate = open('outputSet.txt', 'w')

n = input("1 для чтения из файла, 2 для чтения с консоли: ")
if int(n) == 1:
    FileSetA.seek(0, 0)
    SetA = set(FileSetA.read().split())
    FileSetB.seek(0, 0)
    SetB = set(FileSetB.read().split())
elif int(n) == 2:
    SetA = set(input("Введите множество A(через пробел): ").split())
    SetB = set(input("Введите множество B(через пробел): ").split())
else:
    n = "Error"
    print("Выбран некорректный режим работы программы")

if n != "Error":
    input_mode = [i for i  in input("Введите опреацию(Union, Cross, DiffAB, DiffBA можно несколько через пробел): ").split()]
    if len(input_mode) <= 4:
        print("Множество A: ", SetA)
        print("Множество B: ", SetB)
        for i in input_mode:
            if i == "Union" or i == "Cross" or i == "DiffAB" or i == "DiffBA":
                if i == "Union":
                    SetUnion = f"Объединение множеств A и B: {SetA.union(SetB)}\n"
                    FileSetManipulate.write(SetUnion)
                    print(SetUnion, end='')
                if i == "Cross":
                    SetCross = f"Пересечение множеств A и B: {SetA.intersection(SetB)}\n"
                    FileSetManipulate.write(SetCross)
                    print(SetCross, end='')
                if i == "DiffAB":
                    SetDiffAB = f"Разница множеств A и B: {SetA.difference(SetB)}\n"
                    FileSetManipulate.write(SetDiffAB)
                    print(SetDiffAB, end='')
                if i == "DiffBA":
                    SetDiffBA = f"Разница множеств B и A: {SetB.difference(SetA)}\n"
                    FileSetManipulate.write(SetDiffBA)
                    print(SetDiffBA, end='')
            else:
                print("Некоррекный режим работы.")
        print("Операция(ы) записана(ы) в файл.")
    else:
        print("Слишком большое количество операций", end='')
    FileSetA.close()
    FileSetB.close()
    FileSetManipulate.close()