import requests
from django.shortcuts import render

def clima_view(request):
    if request.method == "POST":
        cidade = request.POST['cidade']
        api_key = '1825c5316c741dae6d60c371bf1c7be5' 
        url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br'
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            clima = {
                'cidade': cidade,
                'temperatura': data['main']['temp'],
                'descricao': data['weather'][0]['description'],
                'humidade': data['main']['humidity'],
                'vento': data['wind']['speed'],
            }
            return render(request, 'clima/clima.html', {'clima': clima})
        else:
            erro = "Cidade não encontrada. Tente novamente."
            return render(request, 'clima/clima.html', {'erro': erro})
    return render(request, 'clima/clima.html')

