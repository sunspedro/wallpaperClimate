import requests

chaveApi = "e0290c240f4261a838a010102ec07a4e"
cidade = "Caxias do Sul"
url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&units=metric&appid={chaveApi}"

requisicao = requests.get(url)
requisicao_dic = requisicao.json()
temperatura = requisicao_dic['main']['temp']
