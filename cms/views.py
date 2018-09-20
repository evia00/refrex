from django.shortcuts import render, redirect
from cms.form import AddForm, LoginForm
from cms.models import Auth, RefreshToken, AccessToken, User
from sequences import get_next_value
import secrets
from logging import getLogger, StreamHandler, DEBUG
from datetime import datetime


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

            refreshToken = RefreshToken()
            refreshToken.refreshTokenId = get_next_value('refreshId')
            refreshToken.authId = auth.authId
            refreshToken.refreshToken = secrets.token_hex()
            refreshToken.validTs = datetime.now()
            refreshToken.save()

            accessToken = AccessToken()
            accessToken.accessTokenId = get_next_value('accessToken')
            accessToken.refreshTokenId = refreshToken.refreshTokenId
            accessToken.accessToken = secrets.token_hex()
            accessToken.validTs = datetime.now()
            accessToken.save()
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

    form = AddForm()
    return render(request, 'cms/add.html', dict(form=form))


def del_users(request):
    logger = getLogger('add')
    handler = StreamHandler()
    handler.setLevel(DEBUG)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)
    logger.propagate = False

    users = User.objects.all()
    for i, j in enumerate(users):
        j.delete()

    return redirect('cms/add.html')
