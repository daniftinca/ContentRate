from django.shortcuts import render
from .forms import AnalyzeForm
from django.contrib.auth.decorators import login_required
from .service.analyzer_service import AnalyzerService
import math

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
            service = AnalyzerService(url, target_query)
            first_res = service.compare_len()
            print(first_res)

            req_tfidf_score, req_terms, google_tfidf_score, google_terms = service.get_request_tf_idf_result()

            req_tfidf_score = [0 if math.isnan(x[0]) else x[0] for x in req_tfidf_score]
            google_tfidf_score = [0 if math.isnan(x[0]) else x[0] for x in google_tfidf_score]
            req_zip = zip(req_tfidf_score, req_terms)
            google_zip = zip(google_tfidf_score, google_terms)

            return render(request, 'results.html', {'form': form,
                                                    'length_res': first_res,
                                                    'req_zip': req_zip,
                                                    'google_zip': google_zip
                                                    })

    else:
        form = AnalyzeForm()

        return render(request, template, {'form': form})
