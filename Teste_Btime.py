from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
import csv


browser = Firefox()
browser.get('https://www.noticiasagricolas.com.br/cotacoes/') #site de cotacao agro
lista_inclusao = []


for i in range(0,24):

    #utilizei varias funçoes para demonstrar como chegar em um elemento web
    subsections = browser.find_element(By.CLASS_NAME, 'subsections')
    lista_n_ordenada = subsections.find_element(By.TAG_NAME, 'ul') #2
    lis = lista_n_ordenada.find_elements(By.TAG_NAME,'li')
    item = lis[i].find_element(By.TAG_NAME,'a').text
    li = lis[i].find_element(By.TAG_NAME,'a').click()
    body = browser.find_element(By.TAG_NAME, 'tbody')
    tr = body.find_element(By.TAG_NAME, 'tr') 
    #a tabela possui 3 colunas, mas uma particularidade do site impediu de buscar elas como uma lista
    #nesse caso e na vida de RPA muitas vezes precisamos seguir o feio e funcional
    data = tr.find_elements(By.TAG_NAME, "td")[0]
    data = data.text
    valor = tr.find_elements(By.TAG_NAME, "td")[1]
    valor = valor.text
    variacao_diaria = tr.find_elements(By.TAG_NAME, "td")[2]
    variacao_diaria = variacao_diaria.text
    #unindo as strings pra inserir em uma só linha da lista
    string_unida = item + ',' + data +',' + valor + ',' + variacao_diaria
    lista_inclusao.append(string_unida)
    #delay apenas para ficar claro o que o robô percorre no site
    sleep(0.7)
    browser.back()

#criacao do arquivo csv
with open('cotacao.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',') 
    field = ["produto", "data", "valor", "variacao_diaria"] #colunas criadas
    writer.writerow(field)
    for inclusoes in lista_inclusao:
        print(inclusoes)   #printando a linha concatenada
        writer.writerow(inclusoes)  #escrevendo no arquivo csv
