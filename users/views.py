from django.shortcuts import render

from .models import User
from .services import github


def index(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        status_code, res = github.get_user(username)
        if status_code == 200:
            User(**res).save()
            context.update({'user': res})
        else:
            context.update({'error': res})
    return render(request, 'users/home.html', context)
