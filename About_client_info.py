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
        "CITY": "г. Екатеринбург",  # город создания договора
        "CL_NAME": "Сычык Валерий Андреевич",  # имя клиента
        "PASPORT_SERIA": "6513".replace(" ",""),  # СЕРИЯ ПАСПОРТА клиента
        "PASPORT_NUMBER": "738055".replace(" ",""),  # НОМЕР ПАСПОРТА клиента
        "PASPORT_HOME": "ОУФМС России по Свердловской обл. в Чкаловском р-не г. Екатеринбурга",  # орган выдавший паспорт ПАСПОРТА клиента
        "PASPORT_DATE": "26.04.2014",  # дата выдачи ПаСПОРТА клиента
        "PASPORT_CODE": "660-010",  # код подразделения ПАСПОРТА клиента
        "REGISTER": "обл. Свердловская г. Екатеринбург р-н Чкаловский ул. Аптекарская д. 50 ком. 91 сек. 17",  # Прописка клиента
        "POST_INDEX": "620085".replace(" ",""),  # Почтовый индекс
        "INN": "667472521501",  # ИНН клиента
        "SNILS": "109-196-445-71",  # СНИЛС клиента
        "CLIENT_MAIL": "Worldtotem@yandex.ru",  # Электронная почта клиента Учасника
        "CLIENT_PHONE": "+7(991)515-04-04",  # номер телефона Учасника
        
        "My_many": 3000, # цена по умолчанию 3 тыс
        "My_prosent":0, # процент по огентскому вознагрождению
        "BANK_RS_NUMBER": "40817810000002674239",  # Р/С НОМЕР участника
        "BANK_NAME": 'ПАО "Московский кредитный банк"',  # нименование банка
        "BANK_BIK": "044525659",  # БИК банка участника
        "BANK_KS_NUMBER": "30101810745250000659",  # К/С НОМЕР участника
        "BANK_INN": "7734202860",  # ИНН банка участника
        "BANK_KPP": "770801001",  # КПП банка участника


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
    
    # my_str = f"Дополнительно, в случае победы, Агенту выплачивается вознаграждение в размере {klient_info['My_prosent']}% ({made_price_ofer_rus(klient_info['My_prosent'])} {word}) от суммы покупки выше упомянуты лотов на торгах, но не менее 2000 (двух тысяч) рублей за каждый выигранный лот. Вознаграждение выплачивается не позднее 2-х рабочих дней с момента опубликования протокола о результатах торгов."
    my_str = ""
    if klient_info["My_prosent"] > 0:
        klient_info["Porydak_Ras"] = my_str
    if klient_info["My_prosent"] == 0:
        klient_info["Porydak_Ras"] = ""
    
    return klient_info

