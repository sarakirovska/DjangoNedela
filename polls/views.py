from django.shortcuts import render, redirect

from polls.forms import ProduktForm
from polls.models import Produkt


# Create your views here.
def index(request):
    return render(request, 'index.html')


def produkti(request):
    produkti = Produkt.objects.all()

    return render(request, 'produkti.html', {'produkti': produkti})


def addProdukt(request):
    if request.method == 'POST':
        form = ProduktForm(request.POST, request.FILES)
        if form.is_valid():
            produkt = form.save(commit=False)
            produkt.user = request.user
            produkt.save()

        return redirect("produkti")
    else:
        form = ProduktForm()
    return render(request, 'addProdukt.html', {'form': form})
