import time

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View

from .forms import PhotoForm
from .forms import AtomForm
from .models import Photo
from .models import Atom


class BasicUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'photos/basic_upload/index.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class ProgressBarUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'photos/progress_bar_upload/index.html', {'photos': photos_list})

    def post(self, request):
        time.sleep(1)
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
            photo.title = photo.file.name
            photo.save()
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class DragAndDropUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'photos/drag_and_drop_upload/index.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)



def clear_database(request):
    size1 = 0
    for photo in Photo.objects.all():
        photo.file.size
        photo.delete()
    return redirect(request.POST.get('next'))


def showLibrary(request):
    search_term = ''
    photos = Photo.objects.all().order_by('-uploaded_at')
    if 'search' in request.GET:
        search_term = request.GET['search']
        photos = photos.filter(title__icontains=search_term)
    return render(request, 'photos/library/index.html', {'photos': photos, 'search_term': search_term})


def home(request):
    photos = Photo.objects.all()
    return render(request, 'core/home.html',  {'photos': photos})


class ProgressBarPUploadView(View):
    def get(self, request):
        atoms_list = Atom.objects.all()
        return render(self.request, 'photos/progress_bar_private_upload/index.html', {'atoms': atoms_list})

    def post(self, request):
        time.sleep(1)
        form = AtomForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            atom = form.save()
            data = {'is_valid': True, 'name': atom.file.name, 'url': atom.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)






