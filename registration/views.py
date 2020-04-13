from django.contrib.auth import login
from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ViewSet

from registration.models import User
from registration.serializer import UserRegistrationSerializer, UserLoginSerializer
from .forms import RegisterForm


# def user_register(request):
#     # if this is a POST request we need to process the form data
#     template = 'registration/registration.html'
#
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = RegisterForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             if User.objects.filter(username=form.cleaned_data['username']).exists():
#                 return render(request, template, {
#                     'form': form,
#                     'error_message': 'Username already exists.'
#                 })
#             elif User.objects.filter(email=form.cleaned_data['email']).exists():
#                 return render(request, template, {
#                     'form': form,
#                     'error_message': 'Email already exists.'
#                 })
#             elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
#                 return render(request, template, {
#                     'form': form,
#                     'error_message': 'Passwords do not match.'
#                 })
#             else:
#                 # Create the user:
#                 user = User.objects.create_user(
#                     form.cleaned_data['username'],
#                     form.cleaned_data['email'],
#                     form.cleaned_data['password']
#                 )
#                 # user.first_name = form.cleaned_data['first_name']
#                 # user.last_name = form.cleaned_data['last_name']
#                 # user.phone_number = form.cleaned_data['phone_number']
#                 user.save()
#
#                 # Login the user
#                 login(request, user)
#
#                 # redirect to accounts page:
#                 return HttpResponseRedirect('/accounts/login')
#
#     # No post data availabe, let's just show the page.
#     else:
#         form = RegisterForm()
#
#     return render(request, template, {'form': form})


##########################################################
##########################################################


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status code': status_code,
            'message': 'User registered  successfully',
        }

        return Response(response, status=status_code)


class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)
