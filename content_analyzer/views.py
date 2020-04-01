from django.shortcuts import render
from .forms import AnalyzeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def analyze_content(request):
    template = 'home.html'



    if request.method == 'POST':
        form = AnalyzeForm(request.POST)

    else:
        form = AnalyzeForm()

    return render(request, template, {'form': form})
