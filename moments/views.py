from django.shortcuts import render, redirect
from .models import WeChatUser, Status
from blueapps.account import get_user_model
from blueapps.conf import settings
from django.http import HttpResponse
from config import APP_CODE


def home(request):
    return render(request, 'homepage.html')


def show_user(request):
    user_id = request.user.id
    wechat_user = WeChatUser.objects.get(user_id=user_id)
    return render(request, 'user.html', {'user': wechat_user})


def show_status(request):
    statuses = Status.objects.all()
    return render(request, 'status.html', {'statuses': statuses})


def submit_post(request):
    user = WeChatUser.objects.get(user=request.user)
    text = request.POST.get('text')
    if text:
        status = Status(user=user, text=text)
        status.save()
        return redirect(f'/stag--{APP_CODE}/status')
    return render(request, 'my_post.html')


def set_super_user(request):
    user = get_user_model()
    for name in settings.INIT_SUPERUSER:
        user.objects.update_or_create(username=name,
                                      defaults={'is_staff': True, 'is_active': True, 'is_superuser': True})
    return HttpResponse("Success")
