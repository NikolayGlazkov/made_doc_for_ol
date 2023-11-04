from docx import Document
from docx.shared import Pt
from docxtpl import DocxTemplate
from made_resu_dickt import make_result_dikt

def made_docx_file(data_from_pars:dict,filename:str): # словарь мз парсера заходит сюда и взовисимости от типа торгов пишет файл
        doc = DocxTemplate(filename)
        doc.render(data_from_pars)
        if filename == "Agent_dogovor.docx":
            doc.save(f"Агентский договор№1.docx")
        if filename == "Zayavka_auction.docx":
              doc.save(f"Заявка для участия№1.docx")



url = "https://old.bankrot.fedresurs.ru/MessageWindow.aspx?ID=17312B0CF7084B68AF8471BBEE3F9C5F"
data_from_pars = make_result_dikt(url=url,lot_numbers = ['1'])

# # lot_namber = "6" #:укажите номер лота
# selected_lots = ['4', '7', '8']
made_docx_file(data_from_pars,"Agent_dogovor.docx")
made_docx_file(data_from_pars,"Zayavka_auction.docx")