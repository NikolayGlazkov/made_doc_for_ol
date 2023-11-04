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
        "CITY": "Краснодарский край, ст. Ленинградская",  # город создания договора
        "CL_NAME": "Антохин Владимир Николаевич",  # имя клиента
        "PASPORT_SERIA": "0306",  # СЕРИЯ ПАСПОРТА клиента
        "PASPORT_NUMBER": "475098",  # НОМЕР ПАСПОРТА клиента
        "PASPORT_HOME": "ОУФМС России по Краснодарскому краю в Ленинградском районе",  # орган выдавший паспорт ПАСПОРТА клиента
        "PASPORT_DATE": "11.05.2007",  # дата выдачи ПаСПОРТА клиента
        "PASPORT_CODE": "230-042",  # код подразделения ПАСПОРТА клиента
        "REGISTER": "Краснодарский край, Ленинградский район, ст. Ленинградская, ул. Энергетика, д. 14",  # Прописка клиента
        "POST_INDEX": "353745",  # Почтовый индекс
        "INN": "234103504234",  # ИНН клиента
        "SNILS": "109-475-446 76",  # СНИЛС клиента
        "CLIENT_MAIL": "Kab130@mail.ru",  # Электронная почта клиента Учасника
        "CLIENT_PHONE": "+7 (918) 441-01-04",  # номер телефона Учасника
        
        "BANK_RS_NUMBER": "40817810330852068884",  # Р/С НОМЕР участника
        "BANK_NAME": "Краснодарское отделение №8619 ПАО Сбербанк",  # нименование банка
        "BANK_BIK": "040349602",  # БИК банка участника
        "BANK_KS_NUMBER": "30101810100000000602",  # К/С НОМЕР участника
        "BANK_KPP": "231043001",  # КПП банка участника
        "My_many": 6000, # цена по умолчанию 5 тыс
        "BANK_INN": "7707083893",  # ИНН банка участника
        # "THE_P_COD": "189721",
        "my_mani_in": "", 
        "Smol_name": "",
    }  
   
    klient_info["Smol_name"] = made_smole_name(klient_info["CL_NAME"])
    klient_info["my_mani_in"] = made_price_ofer_rus(klient_info["My_many"])
    

    return klient_info

# print(ClientInfo()["Smol_name"])