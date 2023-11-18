import mysql.connector

# Параметры подключения к базе данных MySQL
# cnx = mysql.connector.connect(user='root', password='example',
#                               host='127.0.0.1',
#                               database='client_data_base')

try:
    with mysql.connector.connect(
        user="root", host="127.0.0.1", password="example", database="client_data_base"
    ) as connection:
        show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)
except Error as e:
    print(e)

# # Создаем объект курсора
# cursor = cnx.cursor()

# Пример запроса
# query = """SELECT id, CL_NAME, CITY, BANK_KPP, BANK_INN
# FROM client_data_base.clients
# WHERE INN = '210802622826'"""

# cursor.execute(query)

# # Получаем результаты запроса
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# # Закрываем курсор и соединение
# cursor.close()
# cnx.close()
