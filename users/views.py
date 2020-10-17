from django.shortcuts import render
from django.views import View
from .forms import UserRegistrationForm
from django.shortcuts import redirect
from django.http import HttpResponse


# Create your views here.
class RegistrationView(View):
    def get(self, request):
        context = {'registration_form': UserRegistrationForm()}
        return render(request, 'users\\registration.html', context=context)

    def post(self, request):
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid() and registration_form.password_verification():
            new_user = registration_form.save(commit=False)
            new_user.set_password(registration_form.password_verification())
            new_user.save()
            return redirect('https://yandex.ru/')

        return HttpResponse(f'{registration_form.is_valid()}\n{registration_form.password_verification()}')
