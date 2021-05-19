from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Guitar, Wood
from .forms import SetUpForm


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def guitars_index(request):
    guitars = Guitar.objects.all()
    return render(request, "guitars/index.html", {"guitars": guitars})


def guitars_detail(request, guitar_id):
    guitar = Guitar.objects.get(id=guitar_id)
    woods_guit_doesnt_have = Wood.objects.order_by('part').exclude(id__in = guitar.woods.all().values_list('id'))
    setup_form = SetUpForm()
    return render(request, "guitars/detail.html", {"guitar": guitar, 'setup_form': setup_form, 'woods': woods_guit_doesnt_have})

def assoc_wood(request, guitar_id, wood_id):
    Guitar.objects.get(id=guitar_id).woods.add(wood_id)
    return redirect('detail', guitar_id=guitar_id)

def add_setup(request, guitar_id):
    form = SetUpForm(request.POST)
    if form.is_valid():
        new_setup = form.save(commit=False)
        new_setup.guitar_id = guitar_id
        new_setup.save()
    return redirect('detail', guitar_id=guitar_id)

class GuitarCreate(CreateView):
    model = Guitar
    fields = "__all__"


class GuitarUpdate(UpdateView):
    model = Guitar
    fields = ["make", "year", "description"]


class GuitarDelete(DeleteView):
    model = Guitar
    success_url = "/guitars/"
