import efrsb_parser
import About_client_info
import datetime
from petrovich.main import Petrovich
import re
from num2words import num2words
from About_client_info import made_smole_name


"""мы делаем результотирующий список из двух списков импортируемых из файла efrsb_parser"""


def make_result_dikt(url:str):
    dikt_table = efrsb_parser.data_lot_tabel(url)
    dict_two = efrsb_parser.make_content_dict(url)

    clieInf = About_client_info.ClientInfo()


    if len(dict_two["ИНН"]) == 12:
        name_of_obligator = dict_two["ФИО должника"]
        # obligator_rad = sklonenie_name(dict_two["ФИО должника"], "GENITIVE")
        # ob_snils_ogrn = f"СНИЛС {dict_two['СНИЛС']}"
        # adres = dict_two["Место жительства"]
    elif len(dict_two["ИНН"]) == 10:
        name_of_obligator = dict_two["Наименование должника"]
        # obligator_rad = dict_two["Наименование должника"]
        # ob_snils_ogrn = f"ОГРН {dict_two['ОГРН']}"
        # adres = dict_two["Адрес"]
    else:
        name_of_obligator = None  # Вы можете установить значение по умолчанию или обработать другим способом

    if dict_two["Вид торгов"] == "Открытый аукцион":
        type_of_bidding = "открытого аукциона"  # Склоенние формы проедения перменная
    elif dict_two["Вид торгов"] == "Публичное предложение":
        type_of_bidding = "публичного предложения"
    elif dict_two["Вид торгов"] == "Закрытый аукцион":
        type_of_bidding = "закрытого аукциона"


    
    name_arbitr = " ".join(re.split(r'\s+',dict_two["Арбитражный управляющий"])[:3])
    INN_CNI_arbit_manager = " ".join(re.split(r'\s+',dict_two["Арбитражный управляющий"])[3:])

    lot_list = [f"лот № {key}: {value['Описание']}" for key, value in dikt_table.items()]
    
    lot_info = {
        "DATE": datetime.date.today().strftime("%d.%m.%Y"),  # дата создания договора
        "INN_OBLIGOR": dict_two["ИНН"],  # ИНН должника
        "OBLIGOR_NAME": name_of_obligator,  # фио должника
        "arb_man_name": name_arbitr,  # ФИО Арбитражного управляющео
        # "arb_man_email": "Это надо доделать не всегда есть",#dict_two["E-mail"],

        # "SNIL_OGRN_OBLIGOR": ob_snils_ogrn,  # Снилс или ОГРН долника ввод включая слово "Снилс" или "ОГРН"
       # "EFRS_NUM": dict_two["№ сообщения"],  # Номер публикации в ЕФРСБ
        #"EFRSB_PUB_DAT": dict_two["Дата публикации"],  # Дата публикации в ЕФРСБ
        # "OBL_MAN_IN_RAD": obligator_rad,  # фио должника в радительном
        #"PLASE_OBLIGOR": adres,  # Место нахождения должника
        # "opn_clos_an": opn_clos_an,
        #  "opn_clos_skl": opn_clos_skl,
        # "AR_MAN_IN_DAT": sklonenie_name(name_arbitr, "DATIVE"),  # ФИО арбитр в склоеннии
        "INN_CNI_arbit_manager": INN_CNI_arbit_manager,  # инн снилс арбитражного упровляющего
        "Sro_Arbitration": dict_two["СРО АУ"],  # наименование СРО АУ
        # "PROCES": dict_two["Вид торгов"],  # Тип проведения торгов
        "TYPE_OF_BID": type_of_bidding,  # склонение типа проведения торгов
        "OPCLOSE": dict_two["Форма подачи предложения о цене"],  # Форма подачи ценовых предложений
        "ELECTONIC_PLASE": f"ЭТП {dict_two['Место проведения']}",  # Этп проведения
        "lot_list_name":lot_list,
          # Наименование и номер лота
        # "DATA_AUCKCIONA": acsion_date,  # дата провдения
        # "LOT_PRICE": lot_price,  # цена лота
        # "PERCENT_LOT_PRICE": percent_price,  # процент от цены лота
        # "DEPOSIT": zadatok  # Размер задатка
        "smol_arb_name":"",

    }
    
    lot_info["smol_arb_name"] = made_smole_name(lot_info["arb_man_name"])
    

    return clieInf | lot_info


