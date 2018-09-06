from django.shortcuts import render, redirect, get_object_or_404
from cms.form import AddForm, LoginForm
from cms.models import User, Auth, RefreshToken, AccessToken
from sequences import get_next_value
import secrets
from logging import getLogger, StreamHandler, DEBUG


def login(request):
    logger = getLogger('login')
    handler = StreamHandler()
    handler.setLevel(DEBUG)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)
    logger.propagate = False

    user = User()
    if request.method == 'POST':
        form = LoginForm(request.POST, instance=user)
        logger.debug(form.is_valid())
        user = form.save(commit=False)
        users = User.objects.all().filter(userId=user.userId, password=user.password)
        logger.debug(users.count())
        if users.count() > 0:
            auth = Auth()
            auth.authId = get_next_value('authId')
            auth.userId = user.userId
            auth.save()
        return redirect('cms:add_user')
    else:
        form = LoginForm()
    return render(request, 'cms/login.html', dict(form=form))


def add_user(request):
    logger = getLogger('add')
    handler = StreamHandler()
    handler.setLevel(DEBUG)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)
    logger.propagate = False

    user = User()
    if request.method == 'POST':
        form = AddForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            users = User.objects.all().filter(userId=user.userId, password=user.password)
            logger.debug(users.count())
            if users.count() == 0:
                user.save()
                return redirect('cms:login')
    else:
        form = AddForm()
    return render(request, 'cms/add.html', dict(form=form))
