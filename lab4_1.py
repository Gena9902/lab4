import os
from itertools import combinations

def unique(i):
    args = []
    for a in i:
        if a not in args:
            args.append(a)
    return args


def chunk_using_generators(lst):
    lst = list(lst)
    for i in range(0, len(lst), 2):
        yield lst[i:i + 2]

FileSetManipulate = open('outputSet.txt', 'w')

try:
    FileSet = open('input.txt', 'r')
    if FileSet.read() == '':
        raise Exception()
    FileSet.seek(0,0)
except:
    FileSet = open('input.txt', 'w')
    print("Файл пустой")
    FileSet.write(input("Введите множество A(через пробел): ")+"\n")
    FileSet.write(input("Введите множество B(через пробел): ")+"\n")
    FileSet.close()
    FileSet = open('input.txt', 'r')

n = input("1 для чтения из файла, 2 для чтения с консоли: ")
if int(n) == 1:
    Set = FileSet.readlines()    
    SetA = set(Set[0].split())
    SetB = set(Set[1].split())
elif int(n) == 2:
    SetA = set(input("Введите множество A(через пробел): ").split())
    SetB = set(input("Введите множество B(через пробел): ").split())
else:
    n = "Error"
    print("Выбран некорректный режим работы программы")

if n != "Error":
    input_mode = [i for i in input("Введите опреацию(Union(1), Cross(2), DiffAB(3), DiffBA(4), \
SymmDiff(5), AdditionBA(6), PartB(7) можно несколько через пробел): ").split()]
    if len(input_mode) <= 7:
        print("Множество A: ", SetA)
        print("Множество B: ", SetB)
        for i in unique(input_mode):
            if i == "Union" or i == "Cross" or i == "DiffAB" or i == "DiffBA" or i == "SymmDiff" or i == 'AdditionBA' or i == 'PartB' \
            or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7':
                if i == "Union" or i == '1':
                    SetUnion = f"Объединение множеств A и B: {SetA.union(SetB)}\n"
                    FileSetManipulate.write(SetUnion)
                    print(SetUnion, end='')
                if i == "Cross" or i == '2':
                    SetCross = f"Пересечение множеств A и B: {SetA.intersection(SetB)}\n"
                    FileSetManipulate.write(SetCross)
                    print(SetCross, end='')
                if i == "DiffAB" or i == '3':
                    SetDiffAB = f"Разница множеств A и B: {SetA.difference(SetB)}\n"
                    FileSetManipulate.write(SetDiffAB)
                    print(SetDiffAB, end='')
                if i == "DiffBA" or i == '4':
                    SetDiffBA = f"Разница множеств B и A: {SetB.difference(SetA)}\n"
                    FileSetManipulate.write(SetDiffBA)
                    print(SetDiffBA, end='')
                if i == "SymmDiff" or i == '5':
                    SetSymmDiff = f"Симметричная разница множеств A и B: {SetA.symmetric_difference(SetB)}\n"
                    FileSetManipulate.write(SetSymmDiff)
                    print(SetSymmDiff, end='')
                if i == "AdditionBA" or i == '6':
                    if SetA.issuperset(SetB):
                        SetAdditionBA = f"Дополнение множества В до множества А: {SetA.difference(SetB)}\n"
                        FileSetManipulate.write(SetAdditionBA)
                        print(SetAdditionBA, end='')
                    else:
                        SetAdditionBA = "Множество B не является подмножетвом множества A\n"
                        FileSetManipulate.write(SetAdditionBA)
                        print(SetAdditionBA, end='')
                if i == "PartB" or i == '7':
                    r = str(list(chunk_using_generators(SetB)))
                    r1 = r.replace('[', '{')
                    r2 = r1.replace(']', '}')
                    SetPartB = f"Разбиение множества B: {r2}\n"
                    FileSetManipulate.write(SetPartB)
                    print(SetPartB, end='')
            else:
                print("Некоррекный режим работы.")
        print("Операция(ы) записана(ы) в файл.")
    else:
        print("Слишком большое количество операций", end='')
    FileSet.close()
    FileSetManipulate.close()
os.system("pause")
