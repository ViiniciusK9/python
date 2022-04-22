from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from pathlib import Path
from time import sleep


class ChromeAuto:
    def __init__(self, *options: str):
        self.driver_path = 'chromedriver'
        self.chrome_options = webdriver.ChromeOptions()

        if options is not None:
            for option in options:
                self.chrome_options.add_argument(option)

        self.chrome_options.add_argument('start-maximized')
        self.chrome_options.add_argument('--profile-directory=1')
        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.chrome_options.add_experimental_option("useAutomationExtension", False)

        self.chrome_service = Service(
            executable_path=self.driver_path,
        )

        self.chrome = webdriver.Chrome(
            service=self.chrome_service,
            options=self.chrome_options
        )

    def acessa(self, site: str):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_sing_in(self):
        try:
            btn_sing_in = self.chrome.find_element(by=By.CSS_SELECTOR, value='body > div.position-relative.js-header-wrapper > header > div > div.HeaderMenu.HeaderMenu--logged-out.position-fixed.top-0.right-0.bottom-0.height-fit.position-lg-relative.d-lg-flex.flex-justify-between.flex-items-center.flex-auto > div.d-lg-flex.flex-items-center.px-3.px-lg-0.text-center.text-lg-left > div.position-relative.mr-3.mb-4.mb-lg-0.d-inline-block > a')
            btn_sing_in.click()
        except Exception as error:
            print(f'Erro ao clickar em Sing in: {error}')
            pass

    def faz_login(self):
        try:
            input_login = self.chrome.find_element(by=By.ID, value='login_field')
            input_password = self.chrome.find_element(by=By.ID, value='password')
            btn_login = self.chrome.find_element(by=By.NAME, value='commit')

            input_login.send_keys('login')
            input_password.send_keys('senha')
            sleep(3)
            btn_login.click()
        except Exception as error:
            print(f'Erro ao fazer login: {error}')

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element(by=By.CSS_SELECTOR, value='body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details')
            perfil.click()
        except Exception as error:
            print(f'Erro ao clicar no perfil: {error}')

    def faz_logout(self):
        try:
            logout = self.chrome.find_element(by=By.CSS_SELECTOR, value='body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
            logout.click()
        except Exception as error:
            print(f'Erro em fazer logout: {error}')


if __name__ == '__main__':
    site = 'https://github.com/'
    chrome = ChromeAuto()
    chrome.acessa(site)
    sleep(2)
    chrome.clica_sing_in()
    sleep(2)
    chrome.faz_login()
    sleep(2)
    chrome.clica_perfil()
    sleep(2)
    chrome.faz_logout()
    sleep(2)
    chrome.sair()

