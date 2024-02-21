from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.safari.options import Options

def clean_value(value):
    # Очистка значения от лишних символов пробелов и табуляции
    return value.strip().replace('\t', '').replace('\xa0', ' ')

def data_lot_table(url):
    options = Options()
    # Настройка опций для Safari, если это необходимо
    driver = webdriver.Safari(options=options)
    driver.get(url)
    
    wait = WebDriverWait(driver, 10)
    table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "lotInfo")))
    rows = table.find_elements(By.TAG_NAME, "tr")

    array_temp = []
    result_dict = {}
    current_key = None

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
    # Очистка каждой ячейки от лишних пробелов и специальных символов
        array = [cell.text.replace('\xa0', ' ').strip() for cell in cells if cell.text.strip()]
    
        if array:
            array_temp.append(array)
            if array[0].isdigit():
                current_key = array[0]
                result_dict[current_key] = {"Описание": array[1]}
            elif current_key:
                result_dict[current_key]["Описание"] += " " + array[0]  # Изменил на пробел для лучшей читаемости

    my_dict = {clean_value(item[0]): clean_value(item[1]) for item in array_temp if len(item) > 1}


    driver.quit()
    return my_dict

def make_content_dict(url):
    options = Options()
    # Настройка опций для Safari, если это необходимо
    driver = webdriver.Safari(options=options)
    driver.get(url)
    
    wait = WebDriverWait(driver, 10)
    elements_with_primary_class = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "primary")))

    respons_text = [
        "№ сообщения",
        "Дата публикации",
        "ФИО должника",
        "Наименование должника",
        "Место жительства",
        "Адрес",
        "ОГРН",
        "ИНН",
        "СНИЛС",
        "Арбитражный управляющий",
        "СРО АУ",
        "Вид торгов",
        "Дата и время торгов",
        "Форма подачи предложения о цене",
        "Место проведения",
        # "E-mail"
    ]

    array_temp = []

    for element in elements_with_primary_class:
        for text in respons_text:
            if text in element.text:
                td_elements = element.find_elements(By.XPATH, ".//ancestor::tr[1]//td")
                array = [clean_value(td.text) for td in td_elements]
                array_temp.append(array)

    my_dict = {clean_value(item[0]): clean_value(item[1]) for item in array_temp if len(item) > 1}

    driver.quit()
    return my_dict

