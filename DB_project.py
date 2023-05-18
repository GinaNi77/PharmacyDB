import mysql.connector
from mysql.connector import Error
from datetime import datetime

bd = 'pharmacy2'  # созданная БД

while True:  # циклическое выполнение действий
    print("""Меню действий:
                1 - ПОДКЛЮЧЕНИЕ, 3 - ДАННЫЕ КЛИЕНТОВ, 4 - ДАННЫЕ СОТРУДНИКОВ, 5 - ДАННЫЕ ТОВАРОВ,
                6 - ДАННЫЕ ПРОДАЖ, 7 - ВВОД ЗАПИСИ КЛИЕНТА, 8 - ВВОД ЗАПИСИ СОТРУДНИКА,
                9 - ВВОД ЗАПИСИ ПРОДУКТА, 10 - ВВОД ЗАПИСИ ПРОДАЖИ, 11 - ВВОД ЗАПИСИ ЗАКАЗА,
                12 - ВВОД ЗАПИСИ ТОВАРОВ В ЗАКАЗ, 13 - СМЕНА СТАТУСА ЗАДАЧИ, 14 - СПИСОК ЗАКАНЧИВАЮЩИХСЯ ТОВАРОВ,
                15 - ВЫВОД ТОП 3 СОТРУДНИКОВ, 0 - ВЫХОД""")
    Code = int(input('Выберите действие: '))

    if Code == 0:  # завершение сеанса работы с БД
        try:
            cnx.close()
            print('сеанс работы с БД завершен')
        except Error as err:
            print(err)
        finally:
            break

    elif Code == 1:  # подключение к БД и создание курсора
        try:
            cnx = mysql.connector.connect(
                host="localhost", user='root', database=bd, password='89181024524Ni@')
            cursor1 = cnx.cursor()
            print('подключение к БД выполнено')
        except Error as e:
            print(e)

    elif Code == 2:  # выполнение произвольного запроса на выборку данных
        Query1 = input('Введите запрос на выборку данных: ')
        try:
            cnx.start_transaction()
            cursor1.execute(Query1)
            for row in cursor1.fetchall():
                print(row)
            cnx.commit()
        except Error as err:
            print(err)

    elif Code == 3:  # отображение данных клиентов
        QueryCustomer = "SELECT * FROM Customers"
        try:
            cursor1.execute(QueryCustomer)
            for (Customer_ID, FirstName, LastName, Adress, PhoneNumber) in cursor1:
                print('{} {} зарегистрирован(а) под номером {}'.format(
                    FirstName, LastName, Customer_ID))
        except Error as err:
            print(err)

    elif Code == 4:  # отображение данных сотрудников
        QueryEmployee = "SELECT * FROM Employees"
        try:
            cursor1.execute(QueryEmployee)
            for (Employee_ID, FirstName, LastName, Position, Salary) in cursor1:
                print(
                    '{} {} - зарегистрирован(а) под номером {}'.format(FirstName, LastName, Employee_ID))
        except Error as err:
            print(err)

    elif Code == 5:  # отображение данных о товаре
        QueryProducts = "SELECT * FROM Products"
        try:
            cursor1.execute(QueryProducts)
            for (Product_ID, Name, Description, Price, Quantity, Manufacturer) in cursor1:
                print('{} ({}) - зарегистрирован(а) под номером {}. Цена - {}руб. Производитель - {}. Кол-во - {}.'.format(
                    Name, Description, Product_ID, Price, Manufacturer, Quantity))
        except Error as err:
            print(err)

    elif Code == 6:  # отображение данных о продаже
        QuerySales = "SELECT * FROM Sales"
        try:
            cursor1.execute(QuerySales)
            for (Sale_ID, Customer_ID, Employee_ID, Product_ID, Amount, SaleDate, Quantity) in cursor1:
                print('{} {} {} {} {} {} {}'.format(Sale_ID, Customer_ID,
                      Employee_ID, Product_ID, Amount, SaleDate, Quantity))
        except Error as err:
            print(err)

    elif Code == 7:  # ввод данных о клиентов
        print('введите данные о клиенте')
        FirstName = input('Имя: ')
        LastName = input('Фамилия: ')
        Adress = input('Адрес: ')
        PhoneNumber = input('Телефон: ')
        QueryInputCustomer = """INSERT INTO Customers (FirstName, LastName, Adress, PhoneNumber) VALUE ('{}','{}','{}','{}')""".format(
            FirstName, LastName, Adress, PhoneNumber)

        print(QueryInputCustomer)

        try:
            cursor1.execute(QueryInputCustomer)
            cnx.commit()
            print('данные введены')
        except Error as err:
            print(err)

    elif Code == 8:  # ввод данных о сотруднике
        print('введите данные о cотруднике')
        FirstName = input('Имя: ')
        LastName = input('Фамилия: ')
        Position = input('Должность: ')
        Salary = input('Зарплата: ')
        QueryInputEmployee = """INSERT INTO Employees (FirstName, LastName, Position, Salary) VALUE ('{}', '{}','{}','{}')""".format(
            FirstName, LastName, Position, Salary)

        print(QueryInputEmployee)

        try:
            cursor1.execute(QueryInputEmployee)
            cnx.commit()
            print('данные введены')
        except Error as err:
            print(err)

    elif Code == 9:  # ввод данных о товаре
        print('введите данные о товаре')
        Name = input('Наименование товара: ')
        Description = input('Описание товара: ')
        Price = input('Цена товара: ')
        Quantity = input('Кол-во товара: ')
        Manufacturer = input('Производитель товара: ')
        QueryInputProduct = """INSERT INTO Products (Name, Description, Price, Quantity, Manufacturer) VALUE ('{}', '{}', '{}','{}','{}')""".format(
            Name, Description, Price, Quantity, Manufacturer)

        print(QueryInputProduct)

        try:
            cursor1.execute(QueryInputProduct)
            cnx.commit()
            print('данные введены')
        except Error as err:
            print(err)

    elif Code == 10:  # ввод данных о продаже
        print('введите данные о товаре')
        Customer_ID = input('Код клиента: ')
        Employee_ID = input('Код сотрудника: ')
        Product_ID = input('Код товара: ')
        Quantity = input('Кол-во товара: ')
        SaleDate = datetime.now()
        QueryInputSales = """INSERT INTO Sales (Customer_ID, Employee_ID, Product_ID, SaleDate, Quantity) VALUE ('{}', '{}', '{}','{}','{}')""".format(
            Customer_ID, Employee_ID, Product_ID, SaleDate, Quantity)

        print(QueryInputSales)

        try:
            cursor1.execute(QueryInputSales)
            cnx.commit()
            print('данные введены')
        except Error as err:
            print(err)

    elif Code == 11:  # ввод данных о заказе
        print('введите данные о заказе')
        Order_Employee_ID = input('Код сотрудника: ')
        Status = "Создан"
        OrderDate = datetime.now()
        QueryInputOrders = """INSERT INTO Orders (Order_Employee_ID, Status, OrderDate) VALUE ('{}', '{}', '{}')""".format(
            Order_Employee_ID, Status, OrderDate)

        print(QueryInputOrders)

        try:
            cursor1.execute(QueryInputOrders)
            cnx.commit()
            print('данные введены')
        except Error as err:
            print(err)

    elif Code == 12:  # ввод данных о товарах в заказе
        print('введите данные о товаров в заказ')
        Order_ID = input('Код заказа: ')
        Product_ID = input('Код товара: ')
        Order_Product_Quantity = input('Кол-во: ')
        QueryInputOrderProducts = """INSERT INTO OrderProducts (Order_ID, Product_ID, Order_Product_Quantity) VALUE ('{}', '{}', '{}')""".format(
            Order_ID, Product_ID, Order_Product_Quantity)

        print(QueryInputOrderProducts)

        try:
            cursor1.execute(QueryInputOrderProducts)
            cnx.commit()
            print('данные введены')
        except Error as err:
            print(err)

    elif Code == 13:  # смена статуса заказа
        print('введите новый статус заказа')
        Order_ID = input('Код заказа: ')
        print('Выберите: 1. Оформлен    2. Доставлен')
        Status = input('Новый статус заказа: ')

        if (Status == "1"):
            Status = "Оформлен"
        elif (Status == "2"):
            Status = "Доставлен"

        MutationUpdateOrderStatus = """UPDATE Orders SET Status = %s WHERE Order_ID = %s"""
        input_data = (Status, Order_ID)

        print(MutationUpdateOrderStatus)

        try:
            cursor1.execute(MutationUpdateOrderStatus, input_data)
            cnx.commit()
            print('данные введены')
        except Error as err:
            print(err)

    elif Code == 14:  # вывод 3х товаров с самым низким кол-ом на складе

        try:
            cursor1.callproc('GetLowestQuantityProducts')
            for result in cursor1.stored_results():
                for row in result.fetchall():
                    print(row)
        except Error as err:
            print(err)

    elif Code == 15:  # ввод 3х работников с самыми большими продажами
        print('введите новый месяц')
        month = int(input('Месяц: '))
        try:
            cursor1.callproc('GeThreeTopSalesEmployees', [month])
            for result in cursor1.stored_results():
                for row in result.fetchall():
                    print(row)
        except Error as err:
            print(err)

print('работа программы завершена')
