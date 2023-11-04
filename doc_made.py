from docx import Document
from docx.shared import Pt
from docxtpl import DocxTemplate
import made_resu_dickt

def made_docx_file(data_from_pars:dict,lot_namber,filename:str): # словарь мз парсера заходит сюда и взовисимости от типа торгов пишет файл
        doc = DocxTemplate(filename)
        doc.render(data_from_pars)
        if filename == "Agent_dogovor.docx":
            doc.save(f'Агентский договор №1.docx')
        if filename == "Zayavka_auction.docx":
             doc.save(f'Заявка на участие №1.docx')



url = "https://old.bankrot.fedresurs.ru/MessageWindow.aspx?ID=C8F7781A6667492495E4EA0A23904DA8"
lot_namber = "4" #:укажите номер лота

data_from_pars = made_resu_dickt.make_result_dikt(url=url,lot_num=lot_namber) 

made_docx_file(data_from_pars,lot_namber,"Agent_dogovor.docx")
if data_from_pars["PROCES"] == "Открытый аукцион":
    made_docx_file(data_from_pars,lot_namber,"Zayavka_auction.docx")
if data_from_pars["PROCES"] == "Публичное предложение": 
    made_docx_file(data_from_pars,lot_namber,"Zayavka_pablic.docx")
if data_from_pars["PROCES"] == "Закрытый аукцион":
    made_docx_file(data_from_pars,lot_namber,"Zayavka_auction.docx")

# made_docx_file(data_from_pars,lot_namber,"Zayavka_auction.docx")