from docx import Document

from docxtpl import DocxTemplate
from made_resu_dickt import make_result_dikt, select_and_generate
import efrsb_parser

def docx_made_lot_list(my_list):
    doc = Document()

    for item in my_list:
        doc.add_paragraph(item)

    doc.save('Список лотов.docx')

def made_docx_file(
    data_from_pars: dict, filename: str
):  # словарь мз парсера заходит сюда и взовисимости от типа торгов пишет файл
    doc = DocxTemplate(filename)
    doc.render(data_from_pars)
    if filename == "Agent_dogovor.docx":
        doc.save(f"Агентский договор№1.docx")
    if filename == "Zayavka_auction.docx":
        doc.save(f"Заявка для участия№1.docx")


selected_lots = ["1"]  # введите номера лотов
url = "https://old.bankrot.fedresurs.ru/MessageWindow.aspx?ID=BEEB9CD80D69478988F808988A2F79F8"

dikt_table = efrsb_parser.data_lot_tabel(url)
dict_two = efrsb_parser.make_content_dict(url)

data_from_pars = make_result_dikt(dict_two,lot_numbers=selected_lots)


docx_made_lot_list(select_and_generate(dikt_table,lot_numbers = selected_lots)) # список лотов
made_docx_file(data_from_pars, "Agent_dogovor.docx")
made_docx_file(data_from_pars, "Zayavka_auction.docx")


# print(dikt_table)
