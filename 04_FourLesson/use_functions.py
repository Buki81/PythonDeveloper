def sale(x=None, current_account = 0, sales_dict = {}):
    while x == 4:
        break
    else:
        if x == 1:
            add_funds = int(input('\nПополняем счет\nВведите сумму пополнения(натуральное число): '))
            current_account += add_funds
            print(f'Вы пополнили счет на {add_funds} тугриков\nНа счету всего: {current_account} тугриков\n')
        elif x == 2:
            sale_name = input('\nПокупаем что-то, напишите что: ')
            sale_coast = int(input('Сколько заплатим тугриков?: '))
            if current_account >= sale_coast:
                current_account -= sale_coast
                sales_dict[sale_name] = sale_coast
                print(f'\nКупили {sale_name} на сумму {sale_coast} тугриков.\n'
                      f'На счету осталось {current_account} тугриков\n')
            elif current_account < sale_coast:
                print(f'\nНа счету не хватет средств. Пополните счет\n')
        elif x == 3:
            print(f'\nВсего совершенно покупок - {len(sales_dict)} на сумму {sum(list(sales_dict.values()))} тугриков')
            for key, value in sales_dict.items():
                print(f'{key} - {value} тугриков')
            print()
        a = None
        while a not in (1, 2, 3, 4):
            a = input(f'Программа предлагает следующие варианты действий\n1. пополнить счет\n'
                      f'2. покупка\n3. история покупок\n4. выход\nВведите цифру 1-4: ')
            if a.isdigit():
                a = int(a)
            if a not in (1, 2, 3, 4):
                print(f'\nНЕВЕРНО!\n')
        return sale(a, current_account, sales_dict)



sale()
print(f'\nДо встречи!')
