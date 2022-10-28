from django.shortcuts import render
from datetime import datetime


def index(request):
    return render(request, 'about/index.html')


def whoami(request):
    user_agent = request.META.get('HTTP_USER_AGENT')
    remote_address = request.META.get('REMOTE_ADDR')
    time = datetime.now().strftime('%H:%M:%S')
    return render(request, 'about/whoami.html', context={'user_agent': user_agent,
                                                         'remote_address': remote_address,
                                                         'time': time})
