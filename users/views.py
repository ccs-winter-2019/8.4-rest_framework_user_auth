from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model, authenticate, login
from django.urls import reverse_lazy

from .forms import SignupForm

User = get_user_model()


class SignupView(CreateView):
    template_name = 'registration/signup.html'
    model = User
    form_class = SignupForm
    success_url = reverse_lazy('rides:ride_list')

    def form_valid(self, form):
        response = super(form).form_valid(form)

        # Authenticate the user checks provided password against the hash
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])

        # Login the user (does the session table/cookie stuff)
        login(self.request, user)

        return response