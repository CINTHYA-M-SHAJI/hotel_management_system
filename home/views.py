# Create your views here.
from pathlib import Path
from django.shortcuts import render

import home
from HMS.settings import BASE_DIR


def index(request):
    return render(request, "index.html")


def result(request):
    import pickle
    BASE_DIR = str(Path(__file__).resolve().parent.parent)
    with open(BASE_DIR+'/home/model_pkl', 'rb') as f:
        lr = pickle.load(f)
    room_type = float(request.GET['room_type'])
    hotel_type = float(request.GET['hotel_type'])
    z = [room_type, hotel_type]
    out = lr.predict([z]).astype(int)
    price = 'The predicted price is '+ str(out[0])
    return render(request, "result.html", {'result_price':price})