from docx import Document

from docxtpl import DocxTemplate
from made_resu_dickt import make_result_dikt,select_by_lot_numbers
import efrsb_parser



def made_docx_file(data_from_pars:dict,filename:str): # словарь мз парсера заходит сюда и взовисимости от типа торгов пишет файл
        doc = DocxTemplate(filename)
        doc.render(data_from_pars)
        if filename == "Agent_dogovor.docx":
            doc.save(f"Агентский договор№1.docx")
        if filename == "Zayavka_auction.docx":
              doc.save(f"Заявка для участия№1.docx")

def made_docx_par(data_from_pars: dict, filename: str):
    doc = Document(filename)

    if "Zayavka_auction.docx" in filename:
        for paragraph in doc.paragraphs:
            if "Описание лотов:" in paragraph.text:
                index = doc.paragraphs.index(paragraph)
                for key, value in data_from_pars.items():
                    doc.paragraphs[index].insert_paragraph_after(f"лот № {key}: {value}")

        new_file_name = filename.replace(filename, f"Результат_{filename}.docx")
        doc.save(new_file_name)

    elif "Agent_dogovor.docx" in filename:
        for paragraph in doc.paragraphs:
            if "Описание лотов:" in paragraph.text:
                index = doc.paragraphs.index(paragraph)
                for key, value in data_from_pars.items():
                    doc.paragraphs[index].insert_paragraph_after(f"лот № {key}: {value}")

        new_file_name = filename.replace(filename, f"Результат_{filename}.docx")
        doc.save(new_file_name) 


url = "https://old.bankrot.fedresurs.ru/MessageWindow.aspx?ID=ECD1121C6AD44109BB4E10BC6AA7EBBB"

dikt_table = efrsb_parser.data_lot_tabel(url)
dict_two = efrsb_parser.make_content_dict(url)

data_from_pars = make_result_dikt(dikt_table,dict_two)


# made_docx_file(data_from_pars,"Agent_dogovor.docx")
# made_docx_file(data_from_pars,"Zayavka_auction.docx")


selected_lots = ['1']

print(select_by_lot_numbers(dikt_table,lot_numbers = selected_lots))

# my_dict = {'3': 'АвтоФургон Марка, модель 2747-0000010 Год выпуска 2012 государственный регистрационный номер Е023ТЕ93 VIN Х3Х274700С0463208', '7': 'АвтоФургон Марка, модель 172412, Год выпуска 2012 государственный регистрационный номер С250ЕЕ123 VIN Z74172412C0021199', '6': 'АвтоФургон Марка, модель 172412 ГАЗ 172412, Год выпуска 2012 государственный регистрационный номер А064ТН123 VIN Z74172412C0016657', '8': 'АвтоФургон Марка, модель 172412, Год выпуска 2012 государственный регистрационный номер К323ТУ123 VIN Z74172412C0022009'}