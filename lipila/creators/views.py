from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from creators.forms.forms import SignupForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, renderer_classes
from creators.models import CreatorUser
from business.models import Product
from LipilaInfo.models import Patron


def index(request):
    return render(request, 'creators/index.html')

def contribute(request, user):
    return render(request, 'creators/admin/actions/contribute.html')


class SignupView(View):

    def get(self, request):
        form = SignupForm()
        context = {'form': form, 'category': 'Creators'}

        return render(request, 'registration/signup.html', context)

    def post(self, request):
        form = SignupForm(request.POST)
        context = {'form': form}

        try:
            if form.is_valid():
                user = form.save(commit=False)  # Don't save directly
                user.set_password(user.password)
                user.save()
                messages.add_message(request, messages.SUCCESS,
                                     "Account created successfully")
                return redirect('login')
            else:
                messages.add_message(
                    request, messages.ERROR, "Error during signup!")
                return render(request, 'registration/signup.html', context)
        except Exception as e:
            messages.add_message(
                    request, messages.ERROR, "Error during signup!")
            return render(request, 'registration/signup.html', context)
        

@login_required
def list_patrons(request, user):
    context = {}
    user_object = get_object_or_404(CreatorUser, username=request.user)
    patrons = Patron.objects.filter(creators=user_object.id)
    context['patrons'] = patrons
    context['user'] = user_object
    return render(request, 'creators/admin/log/patrons.html', context)


@login_required
def log_products(request, user):
    context = {}
    user_object = get_object_or_404(CreatorUser, username=request.user)
    products = Product.objects.filter(owner=user_object.id)
    context['products'] = products
    context['user'] = user_object
    return render(request, 'creators/admin/log/products.html', context)