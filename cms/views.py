from django.shortcuts import render, redirect
from django.http import HttpResponse
from cms.form import AddForm
from cms.models import User
import logging


def login(request):
    logger = logging.getLogger('develop')
    logger.info(request)
    return HttpResponse('ログイン')


def add_user(request):
    logger = logging.getLogger('develop')
    logger.info(request.method)
    user = User()
    if request.method == 'POST':
        form = AddForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            logger.info('success')
            return redirect('cms:login')
        else:
            logger.info('false')
    else:
        form = AddForm()
    return render(request, 'cms/add.html', dict(form=form))
