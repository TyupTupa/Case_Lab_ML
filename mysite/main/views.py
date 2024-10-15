from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from model_work import model_answer, model_load

from .forms import TextForm

MODEL = None #глобальная переменная, чтобы загружать модель единожды при запуске приложения

def get_model():
    """
    Изменяет глобаьную переменную MODEL, содержащую модель sklearn. 
    Если модель еще не загружена в память, она загружается из
    сериализованного файла (в формате pickle).
    """
    
    global MODEL
    if MODEL is None:
        name = 'text_classification_model.pkl' 
        MODEL = model_load(name)
        
    return MODEL

def classification_form(request):

    """
     Обрабатывает POST и GET запросы для формы классификации текста
    """

    model = get_model()
    rate = None
    sentiment_bin = None

    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            rate, sentiment_bin = model_answer(model, [text])
            rate = rate[0]
            print(rate[0], sentiment_bin)

    else:
        form = TextForm()

    return render(request, 'main/classification.html', {
        'form': form,
        'rate': rate,
        'sentiment_bin': sentiment_bin
    })

