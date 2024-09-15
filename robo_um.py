from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time

path_chromedriver = 'C:\\Users\\DavidWillian\\Desktop\\Robos\\chromedriver.exe'
url_site = 'https://registro.br/'

service = Service(executable_path=path_chromedriver) # Definindo o serviço do ChromeDriver
driver = webdriver.Chrome(service=service)

df_workbook = pd.read_excel('dominio.xlsx') # Lendo excel
dominios = df_workbook.values.flatten().tolist()

driver.get(url_site)
print('Fazendo pesquisa dos dominios')

resultados = []
for dominio in dominios:
    campo_pesquisa = driver.find_element(By.ID, 'is-avail-field')
    campo_pesquisa.clear()

    campo_pesquisa.send_keys(dominio)
    time.sleep(1)
    campo_pesquisa.send_keys(Keys.ENTER)

    time.sleep(2)
    resultado = driver.find_elements(By.XPATH, '//*[@id="conteudo"]/div/section/div[2]/div/p/span/strong')
    if resultado:
        print('Dominio: ' + dominio + ' ' +  resultado[0].text)
    else:
        ValueError('Não foi encontrado seletor do resultado, validar!')
    resultados.append(resultado[0].text)

nome_arquivo = 'resultados.txt'
with open(nome_arquivo, 'w') as arquivo:
    arquivo.write('\n'.join(resultados))

driver.quit()