import requests as re
import json
import urllib as urllibb
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pandas as pd
from datetime import date,datetime

# %%
#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
#Link Request

# %%
APi_Key = '13b5ba9e5e9e393dc81e5f3b5b9459a9'    
cidade = 'sao paulo'
cod_cid = 'br'
#request = re.get('https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cidade,APi_Key))


# %%
link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade},{cod_cid},&appid={APi_Key}&lang=pt_br&units=metric&cnt=1'
request = re.get(link, verify= False)
clima = request.json()

# %%
descricao = clima['weather'][0]['description']
descricao = descricao.upper()
data = datetime.now().date().strftime('%d-%m-%Y')
descricao

humidade = clima['main']['humidity']
humidade = int(humidade)/100
# %%
list = {"Cidade" : clima['name'],"Data " : data , "Descrição" : descricao,"Temperatura" : clima['main']['temp'], 
"Sensação Térmica" :clima['main']['feels_like'], 'Temperatura Min' : clima['main']['temp_min'],
"Temperatura Max" : clima['main']['temp_max'], "Humidade" : humidade}
list

# %%
dt_clima = pd.DataFrame(data= list, index=[0])
print(dt_clima)
# # %%
# df_antiga = pd.read_csv('Clima.csv', sep=';')
# df_antiga = pd.concat([df_antiga,dt_clima])

# # %%
dt_clima.to_csv('Clima.csv',index=False,  sep=';')


