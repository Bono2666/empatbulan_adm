from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from apps.forms import FormHero
from apps.models import Hero


@login_required(login_url='/login/')
def home(request):
    context = {
        'segment': 'index',
    }
    return render(request, 'home/index.html', context)


@login_required(login_url='/login/')
def hero_index(request):
    hero = Hero.objects.all()
    context = {
        'hero': hero,
        'segment': 'hero',
        'crud': 'index',
    }
    return render(request, 'home/hero_index.html', context)


@login_required(login_url='/login/')
def hero_add(request):
    if request.POST:
        form = FormHero(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('hero-index'))
    else:
        form = FormHero()
        context = {
            'form': form,
            'crud': 'add',
        }
        return render(request, 'home/hero_add.html', context)


# Update Hero
@login_required(login_url='/login/')
def hero_update(request, _id):
    hero = Hero.objects.get(id=_id)
    if request.POST:
        form = FormHero(request.POST, request.FILES, instance=hero)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('hero-index'))
    else:
        form = FormHero(instance=hero)
        context = {
            'form': form,
            'data': hero,
            'crud': 'update',
        }
        return render(request, 'home/hero_update.html', context)


# Delete Hero
@login_required(login_url='/login/')
def hero_delete(request, _id):
    hero = Hero.objects.get(id=_id)
    hero.delete()
    return HttpResponseRedirect(reverse('hero-index'))


@login_required(login_url='/login/')
def icon(request):
    return render(request, 'home/icons.html')


@login_required(login_url='/login/')
def profile(request):
    return render(request, 'home/profile.html')

@login_required(login_url='/login/')
def table(request):
    return render(request, 'home/tables.html')
