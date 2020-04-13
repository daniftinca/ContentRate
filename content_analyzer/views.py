from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response

from .forms import AnalyzeForm
from django.contrib.auth.decorators import login_required
from .service.analyzer_service import AnalyzerService
import math

# Create your views here.
# @login_required(login_url='/accounts/login/')
# def analyze_content(request):
#     template = 'home.html'
#
#     if request.method == 'POST':
#         form = AnalyzeForm(request.POST)
#
#         if form.is_valid():
#             url = form.cleaned_data['url_input']
#             target_query = form.cleaned_data['target_query']
#             print(url)
#             print(target_query)
#             service = AnalyzerService(url, target_query)
#             first_res = service.compare_len()
#             print(first_res)
#
#             req_tfidf_score, req_terms, google_tfidf_score, google_terms = service.get_request_tf_idf_result()
#
#             req_tfidf_score = [0 if math.isnan(x[0]) else x[0] for x in req_tfidf_score]
#             google_tfidf_score = [0 if math.isnan(x[0]) else x[0] for x in google_tfidf_score]
#             req_zip = zip(req_tfidf_score, req_terms)
#             google_zip = zip(google_tfidf_score, google_terms)
#
#             return render(request, 'results.html', {'form': form,
#                                                     'length_res': first_res,
#                                                     'req_zip': req_zip,
#                                                     'google_zip': google_zip
#                                                     })
#
#     else:
#         form = AnalyzeForm()
#
#         return render(request, template, {'form': form})


class ContentAnalyserView(APIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def post(self, request):
        try:
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

                status_code = status.HTTP_200_OK
                response = {
                    'success': 'true',
                    'status code': status_code,
                    'message': 'Content analyse successfully completed',
                    'data': [{
                        'form': form,
                        'length_res': first_res,
                        'req_zip': req_zip,
                        'google_zip': google_zip,
                        }]
                }
            else:
                status_code = status.HTTP_400_BAD_REQUEST
                response = {
                    'success': 'false',
                    'status code': status.HTTP_400_BAD_REQUEST,
                    'message': 'Form not valid :( ',
                }
        except Exception as e:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {
                'success': 'false',
                'status code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Internal server error :( ',
                'error': str(e)
            }
        return Response(response, status=status_code, template_name='home.html')
