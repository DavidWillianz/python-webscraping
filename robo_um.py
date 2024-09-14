from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

path_chromedriver = 'C:\\Users\\DavidWillian\\Desktop\\Robos\\chromedriver.exe'
url_site = 'https://registro.br/'

service = Service(executable_path=path_chromedriver) # Definindo o serviço do ChromeDriver
driver = webdriver.Chrome(service=service)

print('Acessando site')
driver.get(url_site)

dominios = ['testando_robo.com.br', 'uol.com.br', 'abcbolinhas.com.br']
resultados = []
for dominio in dominios:
    campo_pesquisa = driver.find_element(By.ID, 'is-avail-field')
    campo_pesquisa.clear()

    campo_pesquisa.send_keys(dominio)
    time.sleep(1)
    campo_pesquisa.send_keys(Keys.ENTER)
    print('Pesquisa efetuada!')

    time.sleep(2)
    resultado = driver.find_elements(By.XPATH, '//*[@id="conteudo"]/div/section/div[2]/div/p/span/strong')
    if resultado:
        print('Dominio: ' + dominio + ' ' +  resultado[0].text)
    else:
        print('Não foi encontrado seletor do resultado, validar! \n')
    resultados.append(resultado[0].text)

print('Todas urls pesquisadas!' + '\nResultado: ' + ' '.join(resultados))
driver.quit()