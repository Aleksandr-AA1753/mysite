from django.shortcuts import redirect, render
from .forms import TovarForm
from .models import Tovar

def index(request):
    context = {
        'products': Tovar.objects.all(),
    }
    return render(request, 'shopapp/index.html', context)

def tovar_create(request):
    form = TovarForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
            tovar = form.save()
            tovar.save()
            return redirect('shopapp:index')

    return render(
        request,
        'shopapp/tovar_create.html',
        {'form': form}
        )