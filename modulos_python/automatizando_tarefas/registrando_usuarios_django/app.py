from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from pathlib import Path
from time import sleep
import names
import random
from selenium.webdriver.support.ui import Select


"""Script para registrar usuarios aleatorios automaticamente."""


class ChromeAuto:
    def __init__(self):
        self.driver_path = r'C:\Users\green\Documents\git\python\modulos_python\automatizando_tarefas\registrando_usuarios_django\chromedriver.exe'
        self.chrome_options = webdriver.ChromeOptions()

        self.chrome_options.add_argument('start-maximized')
        self.chrome_options.add_argument('--profile-directory=1')
        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.chrome_options.add_experimental_option("useAutomationExtension", False)

        self.chrome_service = Service(
            executable_path=self.driver_path,
        )

        self.chrome = webdriver.Chrome(
            options=self.chrome_options
        )

    def acessa(self, site: str):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def faz_login(self):
        try:
            input_login = self.chrome.find_element(by=By.CSS_SELECTOR, value='#id_username')
            input_password = self.chrome.find_element(by=By.CSS_SELECTOR, value='#id_password')
            btn_login = self.chrome.find_element(by=By.CSS_SELECTOR, value='#login-form > div.submit-row > input[type=submit]')

            input_login.send_keys('usuario') 
            input_password.send_keys('senha')
            sleep(1)
            btn_login.click()
        except Exception as error:
            print(f'Erro ao fazer login: {error}')

    @staticmethod
    def gera_dados():
        email_end = ['@gmail.com', '@hotmail.com', '@outlook.com']
        nome = names.get_first_name()
        sobrenome = names.get_last_name()
        numero = str(random.randint(10, 99)), ' ', str(9), ' ', str(random.randint(91000000, 99999999))
        email = str(nome), str(sobrenome), str(random.sample(email_end, 1)[0])
        categoria = str(random.randint(1, 3))
        return [nome, sobrenome, numero, email, categoria]

    def registra_contato(self):
        btn_add_contato = self.chrome.find_element(by=By.CSS_SELECTOR, value='#content-main > ul > li > a')
        sleep(0.3)
        btn_add_contato.click()
        dados = self.gera_dados()

        input_name = self.chrome.find_element(by=By.CSS_SELECTOR, value='#id_nome')
        input_name.send_keys(dados[0])
        sleep(0.3)
        input_sobrenome = self.chrome.find_element(by=By.CSS_SELECTOR, value='#id_sobrenome')
        input_sobrenome.send_keys(dados[1])
        sleep(0.3)
        input_telefone = self.chrome.find_element(by=By.CSS_SELECTOR, value='#id_telefone')
        input_telefone.send_keys(dados[2])
        sleep(0.3)
        input_email = self.chrome.find_element(by=By.CSS_SELECTOR, value='#id_email')
        input_email.send_keys(dados[3])
        sleep(0.3)
        btn_categoria = self.chrome.find_element(by=By.CSS_SELECTOR, value='#id_categoria')
        select_categoria = Select(btn_categoria)
        select_categoria.select_by_value(dados[4])
        sleep(0.3)

        btn_salvar_registro = self.chrome.find_element(by=By.CSS_SELECTOR, value='#contato_form > div > div > input.default')
        btn_salvar_registro.click()

    def faz_logout(self):
        btn_logout = self.chrome.find_element(by=By.CSS_SELECTOR, value='#user-tools > a:nth-child(4)')
        btn_logout.click()


if __name__ == '__main__':
    site = 'http://127.0.0.1:8000/admin/contatos/contato/'
    chrome = ChromeAuto()
    chrome.acessa(site)
    sleep(0.5)
    chrome.faz_login()
    sleep(0.5)
    for i in range(200):
        # chrome.registra_contato()
        pass
    chrome.faz_logout()
    sleep(0.5)
    chrome.sair()
    sleep(0.5)
