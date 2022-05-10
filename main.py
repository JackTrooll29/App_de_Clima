import requests

key = ''
cidade = input('Digite o nome da sua cidade: ').lower()
link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}&lang=pt_br'


requisicao = requests.get(link)
res_requisicao = requisicao.json()
descricao = res_requisicao['weather'][0]['description']
temperatura = res_requisicao['main']['temp'] - 273.15

print(descricao, f'{temperatura:.0f}°C')
