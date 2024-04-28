import logging

import pandas as pd
from main.models import *
import shutil 
import  webbrowser

from django.conf import settings

from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.template.loader import render_to_string
from django.http import HttpResponse


from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_200_OK,
    
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    
    HTTP_500_INTERNAL_SERVER_ERROR
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def make_predict(data_from_csv):
    messages = []
    for index, i in data_from_csv['messages'].items():
        messages.append(i)
    

    #начинаем предсказывать
    sequence_to_classify = messages[:len(messages)]
    candidate_labels = ['отрицательный отклик', 'положительный отклик', 'нейтральный отклик']
    preds = settings.CLASSIFIER(sequence_to_classify, candidate_labels)
    
    dic = {'1' : 0, #нейтраль
           '2' : 0, #доброта
           '3' : 0} #злые люди

    # print(preds)
    for i in range(len(preds)):
        print("meassage =" + preds[i]["sequence"])
        print("probability = ", preds[i]["scores"]) # у нас лейблы упорядочены и вероятности тоже, то есть мы можем взять ответ с позиции на которой стоит наибольшая вероятность 
        print("max probability = ", max(preds[i]["scores"]))
        print("verdict is = ", preds[i]["labels"][preds[i]["scores"].index(max(preds[i]["scores"]))])
        if (preds[i]["labels"][preds[i]["scores"].index(max(preds[i]["scores"]))] == "нейтральный отклик"):
            dic['1'] += 1
        elif ((preds[i]["labels"][preds[i]["scores"].index(max(preds[i]["scores"]))] == "положительный отклик")):
            dic['2'] += 1
        else:
            dic['3'] += 1    

    return dic


    
@csrf_exempt
@ensure_csrf_cookie
@api_view(["GET"])
@permission_classes((AllowAny,))
def main_render(request):
    """"
        Display root html file
    """
    return render(request, 'root.html') 



@csrf_exempt
@ensure_csrf_cookie
@api_view(["POST"])
@permission_classes((AllowAny,))
def send(request):
    """"
        Getting and prepare data for analysis
    """

    res = make_predict(pd.read_csv(request.FILES.get('file')))

    src = "/usr/src/app/main/templates/table.html"

    dst = "/usr/src/app/main/templates/to_render.html"

    shutil.copyfile(src, dst)

    with open(dst, 'r') as file:
        file_data = file.read()

    # Заменяем все вхождения старой строки на новую
    file_data = file_data.replace("var 1", str(res['1']))
    file_data = file_data.replace("var 2", str(res['2']))
    file_data = file_data.replace("var 3", str(res['3']))


    # Открываем файл для записи
    with open(dst, 'w') as file:
        file.write(file_data)

    file.close()


    webbrowser.open('file://' + dst)    

    return Response({
                        "text":"OK",
                    },
                    status=HTTP_200_OK
            )

