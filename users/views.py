from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import forms, models, middlewares


class RegistrationView(CreateView):
    # form_class = UserCreationForm
    form_class = forms.CustomRegistrationForm
    template_name = 'users/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        response = super().form_valid(form)
        age = form.cleaned_data['age']
        if age < 5:
            self.object.club = "Детский"
        elif 5 <= age <= 10:
            self.object.club = "Детский"
        elif 11 <= age <= 18:
            self.object.club = "Подростковый"
        elif 18 <= age <= 45:
            self.object.club = "Взрослый"
        else:
            self.object.club = "Клуб не определен"
        self.object.save()
        return response


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('users:user_list')


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')


class UserListView(ListView):
    template_name = 'users/user_list.html'
    model = models.CustomUser

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['club'] = getattr(self.request, 'club', "Клуб не определен")
        return context
