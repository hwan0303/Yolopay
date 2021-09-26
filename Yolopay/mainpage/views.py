from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Yolopay
from accounts.models import UserProfile
# Create your views here.
def main(request):
    return render(request, 'main.html')

def calendar(request):
    if not request.user.is_superuser:
        user = UserProfile.objects.filter(user = request.user)
        user = user.get()
    else:
        user = request.user
    records = Yolopay.objects.all()
    if Yolopay.objects.filter(yolo_fire="yolo"):
        yolo_cnt = Yolopay.objects.filter(yolo_fire="yolo")
        yolo_rate= round(len(yolo_cnt)/len(records),2)*100
    else:
        yolo_rate=0

    if Yolopay.objects.filter(yolo_fire="fire"):
        fire_cnt = Yolopay.objects.filter(yolo_fire="fire")
        fire_rate= round(len(fire_cnt)/len(records),2)*100
    else:
        fire_rate=0
    return render(request, 'calendar.html', {'user':user,'records':records, 'yolo_rate':yolo_rate,'fire_rate':fire_rate})

def create(request):
    new_record = Yolopay()
    new_record.body = request.POST['record']
    new_record.emotion = request.POST['emotion']
    new_record.yolo_fire = request.POST['type']
    new_record.date = request.POST['date']

    print(new_record.date)
    new_record.save()
    # {"body":new_record.body,"emotion":new_record.emotion,"yolo_fire":new_record.yolo_fire,"date":new_record.date}
    return redirect('calendar')