from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from subprocess import run


def getTranslate(text='', input_language='en', output_language='es'):
    option = Options()
    option.add_argument('--headless')

    driver = webdriver.Firefox(
        executable_path='/usr/local/bin/geckodriver', options=option)

    driver.get(
        f'https://translate.google.com/?sl={input_language}&tl={output_language}&text={text}&op=translate')

    data = driver.find_element_by_class_name('J0lOec')

    return data.text


def getAutoTranslate(text='', output_language='es'):
    """
    this is a function that can translate a text automatically
    """
    option = Options()
    option.add_argument('--headless')

    driver = webdriver.Firefox(
        executable_path='/usr/local/bin/geckodriver', options=option)

    driver.get(
        f'https://translate.google.com/?sl=auto&tl={output_language}&text={text}&op=translate')

    data = driver.find_element_by_class_name('J0lOec')

    return data.text
    
inputText = input("Enter the text: ")
output = input("lang code: ")

run("clear", shell=True)
print(getAutoTranslate(inputText, output))