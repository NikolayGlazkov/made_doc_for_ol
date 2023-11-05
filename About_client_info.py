from num2words import num2words

def made_price_ofer_rus(my_int=5000):
    price_as_text = num2words(my_int, lang='ru')
    return price_as_text

def made_smole_name(my_str:str):
    words = my_str.split()
    surname = words[0]
    patronymic_initial = ' '.join(word[0] + '.' for word in words[1:] if word.isalpha())
    return f"{surname} {patronymic_initial}"

def ClientInfo():
    klient_info = {
        "CITY": "гор. Беслан",  # город создания договора
        "CL_NAME": "Уруцкоева Мадина Аслановна",  # имя клиента
        "PASPORT_SERIA": "0915",  # СЕРИЯ ПАСПОРТА клиента
        "PASPORT_NUMBER": "189922",  # НОМЕР ПАСПОРТА клиента
        "PASPORT_HOME": "Отделение УФМС России по респ. Северная Осетия-Алания в Правобережном р-не",  # орган выдавший паспорт ПАСПОРТА клиента
        "PASPORT_DATE": "17.05.2016",  # дата выдачи ПаСПОРТА клиента
        "PASPORT_CODE": "150-007",  # код подразделения ПАСПОРТА клиента
        "REGISTER": "Респ Северная Осетия - Алания гор. Беслан ул. Ленина дом 185",  # Прописка клиента
        "POST_INDEX": "363025",  # Почтовый индекс
        "INN": "151101688830",  # ИНН клиента
        "SNILS": "128-625-884 90",  # СНИЛС клиента
        "CLIENT_MAIL": "",  # Электронная почта клиента Учасника
        "CLIENT_PHONE": "",  # номер телефона Учасника
        
        "My_many": 5000, # цена по умолчанию 5 тыс
        "My_prosent":"",
        "BANK_RS_NUMBER": "",  # Р/С НОМЕР участника
        "BANK_NAME": "",  # нименование банка
        "BANK_BIK": "",  # БИК банка участника
        "BANK_KS_NUMBER": "",  # К/С НОМЕР участника
        "BANK_KPP": "",  # КПП банка участника
        "BANK_INN": "",  # ИНН банка участника


        "my_mani_in": "",  # эта переменная еще не создана
        "Smol_name": "", #  эта переменная еще не создана
        "porydok_ras":""
    }  

   
    klient_info["Smol_name"] = made_smole_name(klient_info["CL_NAME"])
    klient_info["my_mani_in"] = made_price_ofer_rus(klient_info["My_many"])
    
    
    if isinstance(klient_info["My_prosent"], int):
        klient_info["porydok_ras"] = f"это число"
    else:
        klient_info["porydok_ras"] = f"это строка"
    
    return klient_info


ClientInfo()
