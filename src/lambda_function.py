import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import logging
from time import sleep

def lambda_handler(*args, **kwargs):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1280x1696')
    chrome_options.add_argument('--user-data-dir=/tmp/user-data')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_argument('--v=99')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--data-path=/tmp/data-path')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--homedir=/tmp')
    chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    chrome_options.binary_location = os.getcwd() + "/bin/headless-chromium"

    driver = webdriver.Chrome(options=chrome_options)

    wait = WebDriverWait(driver, 60)

    driver.get('https://app.pontomaisweb.com.br/#/acessar')

    el = driver.find_element_by_xpath('/html/body/ng-view/div/div/form/div/div[1]/div/div/div/label')
    print(el.text)

    cpf = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/ng-view/div/div/form/div/div[1]/div/div/div/div/input')))
    cpf.click()
    cpf.send_keys('05160816321')

    senha = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/ng-view/div/div/form/div/div[2]/div/div/div/div/input')))
    #print do nome do campo
    print(driver.find_element_by_xpath('/html/body/ng-view/div/div/form/div/div[2]/div/div/div/label').text)
    senha.click()
    senha.send_keys('Otav1234')

    login = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/ng-view/div/div/form/div/div[4]/div/div/div[3]/button')))
    #print do nome do botao
    print(driver.find_element_by_xpath('/html/body/ng-view/div/div/form/div/div[4]/div/div/div[3]/button').text)
    login.click()

    # editar_endereco = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="info-panel"]/ul/li[1]/div/div[2]/buttun[2]')))
    # # editar_endereco = driver.find_element_by_xpath('//*[@id="info-panel"]/ul/li[1]/div/div[2]/buttun[2]')
    # editar_endereco.click()

    # digite_endereco = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="info-panel"]/ul/li[1]/div/ul/li[1]/form/div/input')))
    # # digite_endereco = driver.find_element_by_xpath('//*[@id="info-panel"]/ul/li[1]/div/ul/li[1]/form/div/input')
    # digite_endereco.click()
    # digite_endereco.send_keys('38402030')

    # submit_endereco = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="info-panel"]/ul/li[1]/div/ul/li[1]/form/div/span/button/i')))
    # # submit_endereco = driver.find_element_by_xpath('//*[@id="info-panel"]/ul/li[1]/div/ul/li[1]/form/div/span/button/i')
    # submit_endereco.click()

    sleep(10)
    # # icon pontomais clock
    # icon_pontomais_clock = driver.find_element_by_xpath('//*[@id="container"]/div[1]/navbar/nav/div/ul[2]/li[1]/a/i')
    # icon_pontomais_clock.click()

    driver.get('https://app.pontomaisweb.com.br/#/meu_ponto/registro_de_ponto')

    registrar_ponto = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content-wrapper"]/div[2]/div/ng-view/div[2]/button')))
    # print do nome do botao
    print(driver.find_element_by_xpath('//*[@id="content-wrapper"]/div[2]/div/ng-view/div[2]/button').text)
    registrar_ponto.click()

    # espera 10 segundos pra pagina carregar
    sleep(10)
    
    # carrega todo o html e printa
    elem = driver.find_element_by_xpath("//*")
    source_code = elem.get_attribute("outerHTML")
    print(source_code.encode('utf-8'))

    # print("SUCESSO!")
    # logger.info("SUCESSO!")

# lambda_handler()