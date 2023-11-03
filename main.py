# a = 5
# b = 10
# if a < b:
# print(b)
import csv

# num = int(input ("введите число "))
# if 1000 <= num <= 9999:
# print(f"число {num} является четырехзначным.")
# elif -1000 >= num >= -9999:
# print (f"число {num} является четырехзначным.")
# else:
# print (f" число {num }не является четырехзначным")


# time  = int(input("введите число "))
# if 6 < time < 9:
# print (f"пора вставать.")
# else:
# print (f"ты проспал.")
# if 0 > time or time > 23:
# print (f"ошибка.")


# time2 = int(input ("текущее вреям в часах"))
# if  0 <= time2 <= 7:
# print (f"ночь.")
# if 7 <= time2 <= 11:
# print (f"утро.")
# if 12 <=  time2 <= 17:
# print (f"день.")
# if 17 <= time2 <= 23:
# print (f"вечер.")
# if 0 > time2 or time2 > 23:
# print (f"ошибка.")


# year = input ("название времени года.")
# if year == "лето":
# print (f'тополиный пух , жара , июль.')
# elif year == "зима":
# print (f"снеговик ,снежки и горка.")
# elif year == "осень":
# print(f"пора в школу.")
# elif year == "весна":
# print(f"весенняя капель.")
# else:
# print(f"ошибка")


# a = int(input("введите первое число"))
# b = int(input("введите второе число"))
# с = int(input("введите третье число"))
# if a > 10 and b > 10 and c > 10:
# print(f"yes")
# else:
# print(f"no")


# a = int(input("определите положительно или отрицательное число"))
# if a>0:
# print(f"число положительное")
# else:
# print(f"отрицацельный")


# b = int(input("определите число четное или нет "))
# if b % 2 == 0:
# print(f"четное число ")
# else:
# print(f"нечетное число ")


# t = int(input("температра воздуха"))
# if t>10:
# print(f"хорошая погода")
# elif t<=10:
# print(f"плохая погода")


# p = 5
# if p == 5:
# print(f"молодец")
# elif p == 4:
# print(f"хорошо")
# elif p <= 3:
# print(f"лентяй")
# else:
# print(f"ошибка")


# nom = int(input("введите число"))
# if nom > 0:
# print(f"число положительное")
# elif nom == 0:
# print(f"число равно нулю")
# else:
# print(f"число является отрицацельным")


# a = int(input("введите первое число"))
# b = int(input("введите второе число"))
# if a > b:
# print(f"Число {a} больше, чем число {b}")
# else:
# print(f"Число {a} меньше, чем число {b}")


# c = int(input("введите число"))
# f c % 3 == 0:
# print(f"число {c} является крантным ")
# else:
# print(f"число {c} не является крантным ")


# a = 7
# b = 3
# c = 5
# if a + b > c and b + c > a:
# print(f"можно составить треугольник")
# else:
# print(f"нельзя составить треугольник")


# k = int(input("введите число грибов"))
# if k % 10 == 1 and k % 100 != 11:
#     print(f"мы нашли {k} гриб в лесу")
# elif k % 10 == 2 or k % 10 == 3 or k % 10 ==4 and not k % 100 < 10 or k % 100 >= 20
#


# number = 1
# while number < 7:
#     if number % 3 == 0:
#         print(f"делится:{str(number)}")
#     else:
#         print(f"не делится:{str(number)}")
#     number += 1


# i = 3
# while i >= 0:
#     print(i)
#     i -=1


# number = 0
# while number < 5:
#     number += 1
#     if number == 3:
#         continue
#     print(f"число:{str(number)}")
#

# num = 0
# while True:
#     num += 1
#     print(num)


# number = 1
# while number <= 100:
#     print(number)
#     number += 1


# numbers = 1
# while numbers <= 100:
#     if numbers % 5 == 0:
#         print(f"*{numbers}*")
#         numbers += 1
#     else:
#         print(numbers)
#         numbers += 1


# fib1  = 0
# fib2 = 1
# count = 0
#
# print(fib1)
# print(fib2)
#
# while count < 13:
#     fib_sum = fib1 + fib2
#     print(fib_sum)
#     fib1 = fib2
#     fib2 = fib_sum
#     count += 1


# i = 1
# j = 1
# while i <= 10:
#     while j <= 10:
#         print(i * j, end="\t\t")
#         j+=1
#     print("\n")
#     j = 1
#     i += 1


# a = int(input("введите первое число "))
# b = int(input("введите второе число"))
#
# while a >= b:
#     if a % 2 ==0:
#         print(a)
#     a -= 1


# total = 0
# num = int(input("введите число:"))
#
# while num != 0:
#     total += num
#     num = int(input("введите число:"))
# print(f"сумма введённых чисел: {total}")


# num = int(input("введите число"))
# max_num = num
#
# while num != 0:
#     num = int(input("введите число:"))
#     if num > max_num:
#         max_num = num
# print(f"максимальное число:{max_num}")


# задание номер 4


# num = int(input("введите число"))
# min_num = num
# while num !=0:
#     if num < min_num:
#         min_num = num
#     num = int(input("введите число:"))
#     print (f"минимальное число :{min_num}")


# задание номер 6
# number = 957496
# count = 0
# while number != 0:
#     number //= 2
#     count += 1
# print (f"количество итераций {count} ")


# задание номер 7

# a = 2
# b = 497
# c = 0
# while b % a == 0:
#     c = c + 1
# print(f"количесто четных чисел : {c}")

# списки

# values = [
#     "a",2,True,-999,
#     None,"\n\t","",
#     -42,"списки",False
# ]
# print(values)


# number = [1,2,3,4,5]
# people =["Tom","Sam","Bob"]
# to_buy = ["хлеб","кабачки","масло","молоко"]
#
# num =number [3]
# print(people[-2])
# print(to_buy[5])

# values = [
#     [1,2,3],
#     ["a","b","c"],
#     [True,False,True]
# ]
#
# print(values[0][1])
# print(values[-2][2])


# items = ["яблоки","кабачки","груши","апельсины"]
# items[1] = "бананы"
# items[-1] = "мандарины"
#
#
# print(len(items))


# items = ["яблоки","кабачки","груши","апельсины"]
# new_item = "бананы"
#
# if new_item not in items:
#     items.append(new_item)
#
# items.pop(1)
#
#
# i = 0
# while i < len(items)-1:
#     item = items[i]
#     print(item)
#     i+=1


# задание 1


# numbers = [1,3,6,88,99]
# numbers.sort()
# print(sorted(numbers))


# num = [1,2,8,4,30,15]
# max(num) / len(num)
# print(num)


# задание для выполнения
# 3

# numbers = [1,4,5,65,34,21,23,77,88,76,54,92,12]
# total = 0
# i - 0


# практиеское задание 1

# numbers = []
#
# i = 2
# while len(numbers) < 10:
#     numbers.append(i)
#     i+=2
# print(numbers)


# 2
#


# 3
# a = [1,3,4,5]
# b = [4,5,6,7]
# i = 0
# while i < len(a):
#     if a[i] in b:
#         b.remove(a[i])
#         i += 1
#     else:
#         i += 1
# print(b)


# задание 5 повторение

# from random import randint
#
# numbers=[]
# i=0
# while i<10:
#     n = randint(1,100)
#     numbers.append(n)
#     i+=1
#     min_elem=min(numbers)
# print(min_elem)


# letters = ["a","b","c"]
#
# i=0
# while i < len(letters):
#     let=letters[i]
#     print(let)
#     i += 1
# print("готово")
#


# letters = ["a","b","c"]
#
# for let in letters:
#     print(let)
#
# print("готово")

# r = list(range(5))
# print (r)

# r = list(range(1,5))
# print(r)

# r = list((2,10,2))
# print(r)


# r = list(range(10,2,-2))
# print(r)


# задание 1 по теме цикла for

# test_list = (range(5,26))
# for i in test_list:
#      print(i)
#
#


# задание 2
# birthday = "04.06.2003"
#
# day = birthday[:2]
# print (day)


# повторение задание 1


# n = int(input("введите число:"))
#
# for i in range(0, n + 1):
#     print(i)


# задание 2

# k = int(input("введите число:"))
# n = int(input("введите число:"))
# for i in range (k , n + 1 ):
#     print(i)


# задание 3


# k = int(input("введите первое  число:"))
# n = int(input("введите второе число:"))
# total = 0
#
# for i in range(k,n +1 ):
#     total+=1
# print(f"сума чисел от {k} до {n}: {total}")


# задание 4


# k = int(input("введите число:"))
# n = int(input("введите число:"))
# total = 0
# for i in range(k, n + 1):
#      if i % 2 == 0:
#           total += i
# print(f"сумма чисел от {k} до {n}: {total}")


# задание 5

# letters = "ЫгВЫоЯСремДШНККАыкЩЙФа"
# cleaned_letters = letters
# for letter in letters:
#         if letter.upper() == letter:
#             cleaned_letters = cleaned_letters.replace(letter,"")
# print(f"исходная строка : {letters}")
# print(f"очищенная строка :{cleaned_letters}")


# задание 1 по теме функции


# def sum_range ( start,end):
#     total = 0
#     if strat < end:
#         strat , end = end , strat
#         for i in (start,end + 1):
#             total+=1
#         return total
#
# result = sum_range(1,99)
# print(result)


# задание 2

# pi = 3.14
# radius = 5
# circle_area = pi * radius  ** 2
#
# def cirle_area (radius):
#      pi=3.14
#      area = pi * radius ** 2
#      return area
#
#
#  result = circle_area(5)
# print(f"площадь круга:{result}")


# задание 3

# def max_list(*list):
#     return max(list)
#
# result = max_list(1,33,221,454,4232,3232,23243,3)
# print(result)


# задание 4

# def unique_list(*lst):
#     unique_lst = []
#     for i in lst:
#         if i not in unique_lst:
#             unique_lst.append(i)
#     return unique_lst
#
#
# result = unique_list ( 1,34,3,1,1,1,1,34,22)
# print(result)


# задание 5

# def square (a):
#     print(f"P={a}*4={a*4}")                       периметр
#     print(f"S={a}**2={a**2}")                     площадь
#     print(f"d=(2 * {a}) ** 0.5 = {(2 *a) ** 0.5}")диагональ
#
#
# square(5)


# задание 7

# def is_year_leap(year):
#     year = int(input())
#     if year % 4 != 0 or ( year % 100 ==0 and year % 400 !=0):
#         return False
#     else:
#         return True
#
#
# result = is_year_leap(2003)


# словари


# users_list = [
#     ["Tom","+111123455"],
#     ["Bob","+385563295"],
#     ["Alice","+956831256"],
# ]
# user_dict = dict(users_list)
# print(user_dict)


# users = {
#     "Tom":"+111123455",
#     "Bob":"+385563295",
#     "Alise":"+956831256",
# }
#
# print(users["Tom"])
#
# users["Bob"]="+3333333333"
# print(users["Bob"])


# перебор словаря

# users={
#     "Tom":"+111123455",
#     "Bob":"+956831256",
#     "Alice":"+9876543"
# }
#
# for key,value in users.items():
#     print(f"user:{key},phone:{value}")


# users = {
#     "Tom" : {
#         "phone":"+797979797",
#         "email":"tom12@gmail.com"
# },
# "Bob":{
#     "phone":"+9988776",
#     "email":"bob@gmail.com",
#      "skype":"bob123"
#   }
# }
#
# old_email = users["Tom"]["email"]
# users["Tom"]["email"]="supertom@gmail.com"
# print(users["Tom"])


# задание 1

# user = {
# "Name1":"Федор",
# "Name2":"Евгений",
# "Name3":"Анатолий",
# }
# for key , value in user.items():
#       print(f"User:{key},{value}")


# задание 2

# week_days = {
#     "1": {
#         "ru": "Понедельник",
#         "en": "Monday"
#     },
#     "2": {
#         "ru": "Вторник",
#         "en": "Tuesday"
#     },
#     "3": {
#         "ru": "Среда",
#         "en": "Wednesday"
#     },
#     "4": {
#         "ru": "Четверг",
#         "en": "Thursday"
#     },
#     "5": {
#         "ru": "Пятница",
#         "en": "Friday"
#     },
#     "6": {
#         "ru": "Суббота",
#         "en": "Saturday"
#     },
#     "7": {
#         "ru": "Воскресенье",
#         "en": "Sunday"
#     }
# }
#
# for i in week_days:
#     print(f" Номер дня недели: {i}\n",
#           "Название дня недели на русскому языке: ", week_days[i]["ru"] + "\n",
#           "Название дня недели на английском языке: ", week_days[i]["en"] + "\n")


# практика по теме словари


# задание1

# def calculate_score(word):
#     english_scores = {
#         'A': 1, 'E': 1, 'I': 1,
#         'O': 1, 'U': 1, 'L': 1,
#         'N': 1, 'S': 1, 'T': 1,
#         'R': 1, 'D': 2, 'G': 2,
#         'B': 3, 'C': 3, 'M': 3,
#         'P': 3, 'F': 4, 'H': 4,
#         'V': 4, 'W': 4, 'Y': 4,
#         'K': 5, 'J': 8, 'X': 8,
#         'Q': 10, 'Z': 10
#     }
#
#     russian_scores = {
#         'А': 1, 'В': 1, 'Е': 1,
#         'И': 1, 'Н': 1, 'О': 1,
#         'Р': 1, 'С': 1, 'Т': 1,
#         'Д': 2, 'К': 2, 'Л': 2,
#         'М': 2, 'П': 2, 'У': 2,
#         'Б': 3, 'Г': 3, 'Ё': 3,
#         'Ь': 3, 'Я': 3, 'Й': 4,
#         'Ы': 4, 'Ж': 5, 'З': 5,
#         'Х': 5, 'Ц': 5, 'Ч': 5,
#         'Ш': 8, 'Э': 8, 'Ю': 8,
#         'Ф': 10, 'Щ': 10, 'Ъ': 10
#     }
#
#     score = 0
#
#     if word.isalpha() == False:
#         return "Неверный ввод. Повторите ввод, используя только русские или английские буквы."
#
#     word = word.upper()
#
#     if word[0] in english_scores:
#         for letter in word:
#             score += english_scores[letter]
#     elif word[0] in russian_scores:
#         for letter in word:
#             score += russian_scores[letter]
#     else:
#         return "Неверный ввод. Повторите ввод, используя только русские или английские буквы."
#
#     return score
#
#
# word = input("Введите слово: ")
# score = calculate_score(word)
# print(f"Счёт слова '{word}': {score}")


# задание 2
# product = {
# 1: {"название":"смеситель",
#     "опсиание":"для ванной ",
#     "цена":200,
#     "категория":"сантехника"
# },
# 2:{"название": "тарелки",
#     "опсиание":"для кухни",
#     "цена":100,
#     "категория":"посуда"
# },
# 3: {"название": "гель",
#     "описание":"моющее средство",
#     "цена":100,
#     "категория":"химия",
# },
# 4:{"название" : "антисептики",
#     "описание":"защита от бактерий",
#     "цена":200,
#     "категория":"диз. средство"
#     }
# }
#
# key = int(input("введите номер товара:"))
# punkt = input("введите пункт:"\n\t название )


import message

# def add_note():
#     note = input("Введите заметку , которую хотите добавить:")
#     with open("hello.txt ," "a") as file:
#         file.write(note + "\n")
#         print("\n Заметка добавлена в файл")
#
# #
# def delete_note1():
#     with open("hello.txt", "r") as file:
#         reader = file.readlines()
#         search = input("Введите  заметку ,которую хотите удалить:")
#         if search + "\n" not in reader:
#             print("Введенной заметки не существет.")
#         else:
#             with open("hello.txt" , "w") as rewritten_file:
#                 for string in reader:
#                     if string in reader:
#                         if string.strip("\n") != search:
#                             rewritten_file.write(string)
#                             print("Выбранная заметка удалена.")

#
# def editor_note2():
#     note1 = input("Введите заметеку , которую хотите редактировать:")
#     with open("hello.txt" , "a")  as file:


# print("\t Элеткронный блокнот: \n"
#       "Список функций:")
#
#
# def add_note():
#     note = input("Введите заметку , которую хотите добавить :")
#     with open("hello.txt", "a") as file:
#         file.write(note + "\n")
#         print("\nЗаметка успешно добавлена в файл ")
#
#
# def print_note():
#     with open("hello.txt ", "r") as file:
#         rider = file.readlines()
#         try:
#             index = input("Введите индекс заметки , которую хотите вывести :")
#             print(f"Выбранная заметка:{rider[int(index)]}" + "\n")
#         except IndexError:
#             print("Заметки с указаным индексом не существует. Повторите попыту ввода\n")
#
#
# def note_count():
#     with open("hello.txt", "r") as file:
#         count = len(file.readlines())
#         print(f"Количество записанных заметок в файле : {count}\n")
#
#
# def delete_note():
#     with open("hello.txt", "r", encoding='utf8') as file:
#         reader = file.readlines()
#         searh = input("Введите текст замектки , которую хотите удалить :")
#
#         if searh + "\n" not in reader:
#             print("Введенной заметки не существует")
#         else:
#             with open("hello.txt", "w") as rewritten_file:
#                 for string in reader:
#                     if string.strip("\n") != searh:
#                         rewritten_file.write(string)
#                 print("Ввыбранная заметка удалена")
#
#
# def print_oll_note():
#     with open("hello.txt", "r") as file:
#         all_notes = file.readlines()
#         numbers = list(range(1, 1001))
#         print("Список заметок:\n")
#         for note, i in zip(all_notes, numbers):
#             print(str(numbers[i - 1]) + ")" + " " + note.rstrip())
#         print("\n")
#
#
# def find_note():
#     with open("hello.txt", "r") as file:
#         reader = file.readlines()
#         searh = input("Введите текст заметки , которую хотите найти :")
#
#         if searh + "\n" not in reader:
#             print("Введенной заметки не существует.")
#         else:
#             print(f"Введенная заметка :{searh}")
#
#
# def max_note():
#     print("Заметка с наибольшей длиной: ", max(open("hello.txt", "r"), key=len), "\n")
#
#
# num = 0
#
# while True:
#     print("\t1 - добавить новую заметку;\n",
#           "\t2 - вывести заметку по индексу;\n",
#           "\t3 - узнать количество записанных заметок;\n",
#           "\t4 - удалить заметку по тексту;\n",
#           "\t5 - вывести все заметки;\n",
#           "\t6 - поиск заметки по тексту;\n",
#           "\t7 - вывести размер максимальной записанной заметки;\n",
#           "\t0 - завершить работу программы.")
#
#     try:
#         selection = int(input("\nВведите номер операции для вызова из описанного функционала: "))
#     except ValueError:
#         print("Пожалуйста, повторите попытку ввода ещё раз.")
#         continue
#     if selection == num:
#         print("\nБлагодарим за использование программы. Сеанс будет завершён.")
#         break
#     elif selection == 1:
#         add_note()
#         continue
#     elif selection == 2:
#         print_note()
#         continue
#     elif selection == 3:
#         note_count()
#         continue
#     elif selection == 4:
#         delete_note()
#         continue
#     elif selection == 5:
#         print_oll_note()
#         continue
#     elif selection == 6:
#         find_note()
#         continue
#     elif selection == 7:
#         max_note()
#         continue
#     else:
#         print("Выбранной операции не существует. Повторите попытку снова.")
#         continue

# ПРАКТИЧЕСКАЯ ПО ТЕМЕ ЦИКЛ FOR
# numbers = int(input("Введите число:"))
# for i in range(numbers +1):
#     print(i)

# num = int(input("Введите число K:"))
# num1 = int(input("Введите число N:"))
# for i in range(num , num1 +1):
#     print(i)

# num = int(input("Введите число K:"))
# num1 = int(input("Введите число N:"))
# sum_numbers = 0
# for i in range(num , num1+1):
#     if i % 2 == 0:
#         sum_numbers +=i
#     print(sum_numbers)


# a=int(input("a = "))
# b=int(input("b = "))
# total = []
# for i in range(a, b+1):
#     if i%2==0:
#         total.append(i)
# print(sum(total))

# with open("hello.txt ","a") as my_file:
#     text = input("Введите текст: ")
#     my_file.write(text)


# def calc(a,b):
#     c = a + b
#     print(f"{a} + {b} = {c}")
#
#
# calc(5,4)


# def helloUser(name):
#     print(f"Добро пожаловать : {name}")
#
# helloUser("гость")


# def printMax(a , b):
#     if a > b:
#         print(f"Число {a}  больше, чем {b}")
#     if a == b:
#             print(f"Числа равны")
#     else:
#         print(f"Число {b} больше, чем {a}")
#
# printMax(3 , 8)
# printMax(5 , 100)
# printMax(34 , 34)


# def sum_range(start, end):
#     result = 0
#     for i in (start, end+1)
#         s

def sum_range(start, end):
    if start > end:
        end, start = start, end
    return sum(range(start, end + 1))

print(sum_range(2, 12))
print(sum_range(-4, 4))
print(sum_range(3, 2))


