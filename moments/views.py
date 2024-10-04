from django.shortcuts import render, redirect
from .models import WeChatUser, Status


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
        return redirect('/status')
    return render(request, 'my_post.html')
