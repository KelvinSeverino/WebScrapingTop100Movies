#Nome: KELVIN SEVERINO - 3ºADS - TURMA A

'''O código abaixo realiza a raspagem da lista do top 100 filmes do site rotten tomatoes
Primeiramente é feito a importação das bibliotecas Requests,BeautifulSoup e Pandas.
Logo em seguida é dado a url de onde os dados a iram ser raspados, logo após é criado
a soup onde ira ter a estrutura principal onde os dados ficam no site, e em seguida é
usado um for para entrar dentro das classe a e retirar todos os nomes dos filmes do site
e depois usa-se um laço de repetição para juntar todos os dados que estavam separados em listas distintas em um unica lista
logo após, é criado o dataframe que ira gerar um tabela ao extrair os dados da listacompleta'''

#Importando bibiotecas
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Abrindo o site(URL)
url = "https://www.rottentomatoes.com/top/bestofrt/"
r = requests.get(url)

#Criando instancia
soup = BeautifulSoup(r.text, "html.parser")

lista_info = soup.find_all("table", {"class":"table"})
#print(lista_info)

lista_titulos = []
lista_rating = []
lista_QtdeCriticas = []
for lista_td in lista_info:
    lista = (lista_td.find_all("a"))
    lista_r = (lista_td.find_all("span", {"class":"tMeterScore"}))
    lista_c = (lista_td.find_all("td", {"class":"right hidden-xs"}))
    #For para raspar o nome de cada filme
    for lista_dadosA in lista:
        titulos = lista_dadosA.next_element;
        titulos = titulos.lstrip() #lstrip() serve para remover os espaços que vem junto na raspagem
        lista_titulos.append([titulos])
    #For para raspar a porcentagem de aceitação de cada filme
    for lista_dadosSPAN in lista_r:
        rating = lista_dadosSPAN.next_element
        rating = rating.strip("RatingTomatometer\n") #strip remove os dados inuteis que vem junto na raspagem
        rating = rating.lstrip()
        lista_rating.append([rating])
    #For para raspar a quantidade de criticas de cada filme
    for lista_dadosCRITICAS in lista_c:
        qtdeCriticas = lista_dadosCRITICAS.next_element
        lista_QtdeCriticas.append([qtdeCriticas])

cont = 0
listacompleta = [["","",""]]
while cont < 100:
    listacompleta.append([lista_rating[cont],lista_titulos[cont],lista_QtdeCriticas[cont]])
    cont = cont + 1
    
df = pd.DataFrame(listacompleta, columns=['Avaliação','Títulos',"Qtde Críticas"])
print(df)
        
















