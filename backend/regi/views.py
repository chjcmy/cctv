from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import datetime
from collections import Counter

from regi.models import People
from user.models import User
from log.models import log


def main(request):
    return render(request, 'registerPic.html')


@method_decorator(csrf_exempt, name='dispatch')
def postcreate(request):
    people = People()
    seamail = request.POST['userId']
    userNum = User.objects.values('id').filter(Email=seamail)
    people.user_id = userNum
    people.category = request.POST['category']
    people.danger = request.POST['danger']
    people.pic = request.FILES['fileupload']
    people.save()
    return JsonResponse({'message': 'success'})

def getgraph1(request):
    email = request.POST['userID2']
    userNum = User.objects.values('id').get(Email = email)
    logs = log.objects.filter(user = userNum['id'])
    # 한 달 추이
    date_now = datetime.datetime.today()
    date_month_before = date_now - datetime.timedelta(days=29)
    date_index = pd.date_range(start=date_month_before, end=date_now)
    date_index = [i.strftime("%Y-%m-%d") for i in date_index]
    time_data = []
    for i in logs:
        time_data.append(i.date.strftime("%Y-%m-%d"))
    countvisit = Counter(time_data)
    count_visit = []
    for i in date_index:
        if i in countvisit.keys():
            count_visit.append(countvisit[i])
        else:
            count_visit.append(0)

    # 원그래프
    hours = []
    for i in logs:
        hours.append(i.date.hour)
    hours_percentage = [0, 0, 0, 0]
    for i in range(len(hours)):
        if hours[i] < 6:
            hours_percentage[0] += 1
        elif hours[i] < 12:
            hours_percentage[1] += 1
        elif hours[i] < 18:
            hours_percentage[2] += 1
        else:
            hours_percentage[3] += 1
    sums = sum(hours_percentage)
    for i in range(4):
        hours_percentage[i] = round((hours_percentage[i] / sums) * 100, 2)

    # 위험도 그래프
    danger_data = []
    for i in logs:
        danger_data.append(i.danger)
    danger_data = [Counter(danger_data)[j] for j in range(3)]
    context = {
        'logs': logs,
        'danger_data': danger_data,
        'date_index': date_index,
        'count_visit': count_visit,
        'hours_percentage': hours_percentage
    }
    return render(request, 'graph.html', context)