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
        "CITY": "г. Оренбург",  # город создания договора
        "CL_NAME": "Молдаваненко Сергей Владимирович",  # имя клиента
        "PASPORT_SERIA": "5321".replace(" ",""),  # СЕРИЯ ПАСПОРТА клиента
        "PASPORT_NUMBER": "160858".replace(" ",""),  # НОМЕР ПАСПОРТА клиента
        "PASPORT_HOME": "УМВД России по Оренбургской Области",  # орган выдавший паспорт ПАСПОРТА клиента
        "PASPORT_DATE": "18.11.2021",  # дата выдачи ПаСПОРТА клиента
        "PASPORT_CODE": "560-003",  # код подразделения ПАСПОРТА клиента
        "REGISTER": "г. Оренбург ул. Юных Ленинцев д.12 кв. 55",  # Прописка клиента
        "POST_INDEX": "460047".replace(" ",""),  # Почтовый индекс
        "INN": "560913051832",  # ИНН клиента
        "SNILS": "219-684-138 01",  # СНИЛС клиента
        "CLIENT_MAIL": "moldavan88@mail.ru",  # Электронная почта клиента Учасника
        "CLIENT_PHONE": "89878616178",  # номер телефона Учасника
        
        "My_many": 5000, # цена по умолчанию 3 тыс
        "My_prosent":1, # процент по огентскому вознагрождению
        "BANK_RS_NUMBER": "40817810446005712939",  # Р/С НОМЕР участника
        "BANK_NAME": 'ОРЕНБУРГСКОЕ ОТДЕЛЕНИЕ N8623 ПАО СБЕРБАНК',  # нименование банка
        "BANK_BIK": "045354601",  # БИК банка участника
        "BANK_KS_NUMBER": "30101810600000000601",  # К/С НОМЕР участника
        "BANK_INN": "7707083893",  # ИНН банка участника
        "BANK_KPP": "561202001",  # КПП банка участника


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

