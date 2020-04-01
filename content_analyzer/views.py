from django.shortcuts import render
from .forms import AnalyzeForm
from django.contrib.auth.decorators import login_required
from .service.analyzer_service import AnalyzerService

# Create your views here.
@login_required(login_url='/accounts/login/')
def analyze_content(request):
    template = 'home.html'



    if request.method == 'POST':
        form = AnalyzeForm(request.POST)

        if form.is_valid():

            url = form.cleaned_data['url_input']
            target_query = form.cleaned_data['target_query']
            print(url)
            print(target_query)
            service = AnalyzerService(url,target_query)
            first_res = service.compare_len()
            print(first_res)

    else:
        form = AnalyzeForm()

    return render(request, template, {'form': form})
