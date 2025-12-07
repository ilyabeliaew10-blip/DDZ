print(" Учёт времени учебы за неделю ")
print()

while True:
    try:
        day = int(input("Введите количество учебных дней (от 1 до 7): "))
        if day < 1:
            print("Ошибка! Количество дней не может быть меньше 1")
        elif day > 7:
            print("Ошибка! Количество дней не может быть больше 7")
        else:
            break
    except ValueError:
        print("Ошибка пожалуйста введите целое число")

print(f"Отлично будем вводить данные для {day} дней")
print()

hours_list = []

for day1 in range(1, day + 1):
    while True:
        try:
            hours = float(input(f"Сколько часов вы учились в день {day1}? "))
            if hours < 0:
                print("Ошибка часы не могут быть отрицательными")
            else:
                hours_list.append(hours)
                break
        except ValueError:
            print("Ошибка пожалуйста введите число (можно с десятичной точкой)")



print("\n РЕЗУЛЬТАТЫ ")
print(f"Всего учебных дней: {day}")

for i in range(day):
    print(f"День {i + 1}: {hours_list[i]} часов")

hours = sum(hours_list)
print(f"\nОбщее количество часов учебы за неделю: {hours}")

if hours > 0:
    hours1 = hours / day
    print(f"Среднее количество часов в день: {hours1:}")

    if hours1 < 2:
        print("Вы учитесь довольно мало возможно стоит увеличить нагрузку?")
    elif hours1 > 6:
        print("Вы очень много учитесь не забывайте об отдыхе")
    else:
        print("Хороший баланс учебы и отдыха")
else:
    print("Вы не учились на этой неделе. Может, стоит начать?")