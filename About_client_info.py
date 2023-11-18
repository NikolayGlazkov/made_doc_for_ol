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
        "CITY": "г. Омск",  # город создания договора
        "CL_NAME": "Тазылисламов Руслан Робертович",  # имя клиента
        "PASPORT_SERIA": "8008",  # СЕРИЯ ПАСПОРТА клиента
        "PASPORT_NUMBER": "605164",  # НОМЕР ПАСПОРТА клиента
        "PASPORT_HOME": "Отделением УФМС России по республике Башкортостан в гор. Таймазы",  # орган выдавший паспорт ПАСПОРТА клиента
        "PASPORT_DATE": "25.08.2008",  # дата выдачи ПаСПОРТА клиента
        "PASPORT_CODE": "020-025 ",  # код подразделения ПАСПОРТА клиента
        "REGISTER": "г. Омск ул. Рокосовсткого дом№ 32 кв. 254",  # Прописка клиента
        "POST_INDEX": "644073",  # Почтовый индекс
        "INN": "024400220096",  # ИНН клиента
        "SNILS": "133-217-431 17",  # СНИЛС клиента
        "CLIENT_MAIL": "pl128@bk.ru",  # Электронная почта клиента Учасника
        "CLIENT_PHONE": "+79609952665",  # номер телефона Учасника
        
        "My_many": 3000, # цена по умолчанию 5 тыс
        "My_prosent":0, # процент по огентскому вознагрождению
        "BANK_RS_NUMBER": "40817810600099050792",  # Р/С НОМЕР участника
        "BANK_NAME": "АО «Тинькофф Банк»",  # нименование банка
        "BANK_BIK": "044525974",  # БИК банка участника
        "BANK_KS_NUMBER": "30101810145250000974",  # К/С НОМЕР участника
        "BANK_KPP": "773401001",  # КПП банка участника
        "BANK_INN": "7710140679",  # ИНН банка участника


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


# print(ClientInfo()['porydok_ras'])
print(len(str(210802622826)))