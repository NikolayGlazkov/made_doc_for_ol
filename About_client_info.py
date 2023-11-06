from num2words import num2words

def made_price_ofer_rus(my_int):
    price_as_text = num2words(my_int, lang='ru')
    return price_as_text

def made_smole_name(my_str:str):
    words = my_str.split()
    surname = words[0]
    patronymic_initial = ' '.join(word[0] + '.' for word in words[1:] if word.isalpha())
    return f"{surname} {patronymic_initial}"

def ClientInfo():
    klient_info = {
        "CITY": "с. Урмаево",  # город создания договора
        "CL_NAME": "Хуснутдинова Эльвира Ильгизовна",  # имя клиента
        "PASPORT_SERIA": "4619",  # СЕРИЯ ПАСПОРТА клиента
        "PASPORT_NUMBER": "434751",  # НОМЕР ПАСПОРТА клиента
        "PASPORT_HOME": "ГУ МВД России по Московской области",  # орган выдавший паспорт ПАСПОРТА клиента
        "PASPORT_DATE": "03.07.2019",  # дата выдачи ПаСПОРТА клиента
        "PASPORT_CODE": "500-053",  # код подразделения ПАСПОРТА клиента
        "REGISTER": "Чувашская Республика, Комсомольский р-н, с. Урмаево, ул. Школьная, д. 1, кв. 1",  # Прописка клиента
        "POST_INDEX": "429153",  # Почтовый индекс
        "INN": "210802622826",  # ИНН клиента
        "SNILS": "151-842-387 63",  # СНИЛС клиента
        "CLIENT_MAIL": "elvira.pahalova@yandex.ru",  # Электронная почта клиента Учасника
        "CLIENT_PHONE": "+7(967)244-55-36",  # номер телефона Учасника
        
        "My_many": 10000, # цена по умолчанию 5 тыс
        "My_prosent":1, # процент по огентскому вознагрождению
        "BANK_RS_NUMBER": "40817810438173048495",  # Р/С НОМЕР участника
        "BANK_NAME": "ПАО Сбербанк",  # нименование банка
        "BANK_BIK": "044525225",  # БИК банка участника
        "BANK_KS_NUMBER": "30101810400000000225",  # К/С НОМЕР участника
        "BANK_KPP": "773643001",  # КПП банка участника
        "BANK_INN": "7707083893",  # ИНН банка участника


        "my_mani_in": "",  # эта переменная еще не создана
        "Smol_name": "", #  эта переменная еще не создана
        "Porydak_Ras":""
    }  

   
    klient_info["Smol_name"] = made_smole_name(klient_info["CL_NAME"])
    klient_info["my_mani_in"] = made_price_ofer_rus(klient_info["My_many"])
    
    if klient_info["My_prosent"] > 1:
        word = "прцентов"
    if klient_info["My_prosent"] == 1:
        word = "процент"
    my_str = f"Дополнительно, в случае победы, Агенту выплачивается вознаграждение в размере {klient_info['My_prosent']}% ({made_price_ofer_rus(klient_info['My_prosent'])} {word}) от суммы покупки выше упомянуты лотов на торгах, но не менее 2000 (двух тысяч) рублей за каждый выигранный лот. Вознаграждение выплачивается не позднее 2-х рабочих дней с момента опубликования протокола о результатах торгов."
    if klient_info["My_prosent"] > 0:
        klient_info["Porydak_Ras"] = my_str
    if klient_info["My_prosent"] == 0:
        klient_info["Porydak_Ras"] = ""
    
    return klient_info


# print(ClientInfo()['porydok_ras'])
print(len(str(210802622826)))