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
        "CITY": "ст. Алексеевска",  # город создания договора
        "CL_NAME": "Конотобсков Сергей Александрович",  # имя клиента
        "PASPORT_SERIA": "1810".replace(" ",""),  # СЕРИЯ ПАСПОРТА клиента
        "PASPORT_NUMBER": "574802".replace(" ",""),  # НОМЕР ПАСПОРТА клиента
        "PASPORT_HOME": "Отделением УФМС России по Волгоградской области в Алексеевском районе",  # орган выдавший паспорт ПАСПОРТА клиента
        "PASPORT_DATE": "12.01.2012",  # дата выдачи ПаСПОРТА клиента
        "PASPORT_CODE": "340-009",  # код подразделения ПАСПОРТА клиента
        "REGISTER": "Волгоградская обл. ст. Алексеевская пер. Пионерский дом 35",  # Прописка клиента
        "POST_INDEX": "403241".replace(" ",""),  # Почтовый индекс
        "INN": "340101346270",  # ИНН клиента
        "SNILS": "134-194-814 57",  # СНИЛС клиента
        "CLIENT_MAIL": " gn9377419582@gmail.com",  # Электронная почта клиента Учасника
        "CLIENT_PHONE": "+7 905 395-88-84",  # номер телефона Учасника
        
        "My_many": 3000, # цена по умолчанию 3 тыс
        "My_prosent":1, # процент по огентскому вознагрождению
        "BANK_RS_NUMBER": "",  # Р/С НОМЕР участника
        "BANK_NAME": '',  # нименование банка
        "BANK_BIK": "",  # БИК банка участника
        "BANK_KS_NUMBER": "",  # К/С НОМЕР участника
        "BANK_INN": "",  # ИНН банка участника
        "BANK_KPP": "",  # КПП банка участника


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

