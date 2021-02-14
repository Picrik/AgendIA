from django.shortcuts import render, redirect
from .models import Task
from .qr_code import get_data
from datetime import date
from PIL import Image
import base64
from io import BytesIO
import re
from .google_pred import process_photo
from django.http import JsonResponse

def index(request):
    tasks = Task.objects.filter(beginning__gt=date.today())
    data = {}
    for t in tasks:
        if t.beginning.month in data.keys():
            data[t.beginning.month][t.beginning.day] = t.title
        else:
            data[t.beginning.month] = {t.beginning.day: t.title}
    return render(request, 'myPWA/index.html', locals())

def add_task(request):
    if request.method == 'POST':

        data = request.POST.get("image")


        from django.core.files.base import ContentFile
        format, imgstr = data.split(';base64,')
        ext = format.split('/')[-1]

        data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)  # You can save this as file instance.
        im = Image.open(data)
        im.save('photos/image.png', 'PNG')

        ret = process_photo(r"photos\image.png")
        print('le retour :', ret)

        return JsonResponse(ret)
