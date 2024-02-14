import mysql.connector

def show_me_database(user, host, password):
    """посмотреть все табицы в СУБД"""
    try:
        connection_params = {
            'user': user,
            'host': host,
            'password': password
        }

        with mysql.connector.connect(**connection_params) as connection:
            show_db_query = "SHOW DATABASES"
            with connection.cursor() as cursor:
                cursor.execute(show_db_query)
                for db in cursor:
                    print(db)
    except Exception as e:
        print(e)

def insert_client(user, host, password, database, id, CL_NAME, CITY, PASPORT_SERIA, PASPORT_NUMBER, PASPORT_HOME, PASPORT_DATE, PASPORT_CODE, REGISTER, POST_INDEX, INN, SNILS, CLIENT_MAIL, CLIENT_PHONE, BANK_RS_NUMBER, BANK_NAME, BANK_BIK, BANK_KS_NUMBER, BANK_KPP, BANK_INN):
    try:
        connection_params = {
            'user': user,
            'host': host,
            'password': password,
            'database': database
        }

        with mysql.connector.connect(**connection_params) as connection:
            insert_query = """
                INSERT INTO clients
                (id, CL_NAME, CITY, PASPORT_SERIA, PASPORT_NUMBER, PASPORT_HOME, PASPORT_DATE, PASPORT_CODE, REGISTER, POST_INDEX, INN, SNILS, CLIENT_MAIL, CLIENT_PHONE, BANK_RS_NUMBER, BANK_NAME, BANK_BIK, BANK_KS_NUMBER, BANK_KPP, BANK_INN)
                VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (id, CL_NAME, CITY, PASPORT_SERIA, PASPORT_NUMBER, PASPORT_HOME, PASPORT_DATE, PASPORT_CODE, REGISTER, POST_INDEX, INN, SNILS, CLIENT_MAIL, CLIENT_PHONE, BANK_RS_NUMBER, BANK_NAME, BANK_BIK, BANK_KS_NUMBER, BANK_KPP, BANK_INN)

            with connection.cursor() as cursor:
                cursor.execute(insert_query, values)

            connection.commit()
            print("Новый клиент успешно добавлен!")

    except Exception as e:
        print("Ошибка при добавлении нового клиента:", e)

user = "root"
host = "127.0.0.1"
password = "example"
database = "your_database_name"

# Вызываем функцию для создания нового клиента
insert_client(user=user, host=host, password=password, database=database, **new_client_data)

user = "root"
host = "127.0.0.1"
password = "example"

show_me_database(user=user,host=host,password=password)

# Пример данных для нового клиента
new_client_data = {
    'CL_NAME': 'Иванов',
    'CITY': None,
    'PASPORT_SERIA': '',
    'PASPORT_NUMBER': '',
    'PASPORT_HOME': '',
    'PASPORT_DATE': '',
    'PASPORT_CODE': '',
    'REGISTER': '',
    'POST_INDEX': None,
    'INN': '',
    'SNILS': None,
    'CLIENT_MAIL': None,
    'CLIENT_PHONE': None,
    'BANK_RS_NUMBER': None,
    'BANK_NAME': None,
    'BANK_BIK': None,
    'BANK_KS_NUMBER': None,
    'BANK_KPP': None,
    'BANK_INN': None
}

insert_client(user=user, host=host, password=password, database=database)