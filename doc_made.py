from docx import Document
from docx.shared import Pt
from docxtpl import DocxTemplate
from made_resu_dickt import make_result_dikt
from efrsb_parser import data_lot_tabel

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
data_from_pars = make_result_dikt(url=url)

# # lot_namber = "6" #:укажите номер лота
# selected_lots = ['4', '7', '8']
made_docx_file(data_from_pars,"Agent_dogovor.docx")
made_docx_file(data_from_pars,"Zayavka_auction.docx")
# made_docx_par(data_lot_tabel(url=url),"Агентский договор№1.docx")
# made_docx_par(data_lot_tabel(url=url),"Заявка для участия№1.docx")
