# -*- coding: utf-8 -*-
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse

from django.shortcuts import redirect, render, render_to_response
from django.template.context_processors import csrf
from django.template.loader import render_to_string

from django.views import View
from django.views import generic

from django.conf import settings
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site

from django.urls import reverse_lazy


# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

from django.utils.encoding import force_text
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode

from .special_func import get_next_url
from .tokens import account_activation_token
from .forms import ProfileForm
from .forms import SignUpForm


class ELoginView(View):
    context_object_name = 'login'

    def get(self, request, *args, **kwargs):
        # если пользователь авторизован, то делаем редирект на главную страницу
        if auth.get_user(request).is_authenticated:
            return redirect('index')
        else:
            # Иначе формируем контекст с формой авторизации и отдаём страницу
            # с этим контекстом.
            # работает, как для url - /admin/login/ так и для /accounts/login/
            context = self.create_context_username_csrf(request)
            return render_to_response('accounts/login.html', context=context)

    def post(self, request):
        # получив запрос на авторизацию
        form = AuthenticationForm(request, data=request.POST)

        # проверяем правильность формы, что есть такой пользователь
        # и он ввёл правильный пароль
        if form.is_valid():
            # в случае успеха авторизуем пользователя
            auth.login(request, form.get_user())
            # получаем предыдущий url
            next = urlparse(get_next_url(request)).path
            # и если пользователь из числа персонала и заходил через url /admin/login/
            # то перенаправляем пользователя в админ панель
            if next == '/admin/login/' and request.user.is_staff:
                return redirect('/admin/')
            # иначе делаем редирект на предыдущую страницу,
            # в случае с /accounts/login/ произойдёт ещё один редирект на главную страницу
            # в случае любого другого url, пользователь вернётся на данный url
            return redirect(next)

        # если данные не верны, то пользователь окажется на странице авторизации
        # и увидит сообщение об ошибке
        context = self.create_context_username_csrf(request)
        context['login_form'] = form
        return render_to_response('accounts/login.html', context=context)

    def create_context_username_csrf(self, request):
        """
        вспомогательный метод для формирования контекста с csrf_token
        и добавлением формы авторизации в этом контексте
        """
        context = {}
        context.update(csrf(request))
        context['login_form'] = AuthenticationForm
        return context


# Работает, но не используется. Сделано через Class Based View, см.ниже
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        context = super(SignUp, self).get_context_data(**kwargs)
        context['user_creation_form'] = UserCreationForm
        return context


class ESignUpView(generic.CreateView):
    template_name = 'accounts/signup.html'

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            mail_sent = self.send_mail(request, user)
            # смотрит на настройку SITE_ID и берет из БД домен
#            current_site = get_current_site(request)
#            subject = '{project_name} : Регистрационная информация'.\
#                format(project_name=settings.PROJECT_NAME)
#            message = render_to_string(
#                'accounts/account_activation_email.html',
#                {
#                    'user': user,
#                    'domain': current_site.domain,
#                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                    'token': account_activation_token.make_token(user),
#                })
#            user.email_user(subject, message, fail_silently=False)
            return redirect('accounts:account_activation_sent')

# Без использования почты
#            user = form.save()
#            user.refresh_from_db()
            # load the profile instance created by the signal
#            user.profile.birth_date = form.cleaned_data.get('birth_date')
#            user.save()
#            raw_password = form.cleaned_data.get('password1')
#            user = authenticate(username=user.username, password=raw_password)
#            login(request, user)
#            return redirect('index')
        return render(
            request,
            self.template_name,
            {
                'user_creation_form': form
            }
            )

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'user_creation_form': form})
        
    def send_email(self, request, user):
        # смотрит на настройку SITE_ID и берет из БД домен
        current_site = get_current_site(request)
        subject = '{project_name} : Регистрационная информация'.\
            format(project_name=settings.PROJECT_NAME)
        context = {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            }
        text_message = render_to_string(
            'accounts/account_activation_email.text',
            context=context)
        html_message = render_to_string(
            'accounts/account_activation_email.html',
            context=context)
        res = user.email_user(
            subject,
            message=text_message,
            fail_silently=False,
            html_message=html_message
            )
        return res


class ProfileView(LoginRequiredMixin, View):
    template_name = 'accounts/profile.html'

    def post(self, request):
        user = request.user
        form = ProfileForm(request.POST)
        if form.is_valid():
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.bio = form.cleaned_data.get('bio')
            user.profile.location = form.cleaned_data.get('location')
            user.profile.country = form.cleaned_data.get('country')
            user.save()
            return redirect('index')

        return render(
            request,
            self.template_name,
            {'user_profile_form': form}
            )

    def get(self, request):
        user = request.user
        initial = {}
        initial['first_name'] = user.first_name
        initial['last_name'] = user.last_name
        initial['email'] = user.email
        initial['birth_date'] = user.profile.birth_date
        initial['bio'] = user.profile.bio
        initial['location'] = user.profile.location
        initial['country'] = user.profile.country
        initial['email_confirmed'] = user.profile.email_confirmed
        form = ProfileForm(initial=initial)
        return render(
            request,
            self.template_name,
            {'user_profile_form': form}
            )


def account_activation_sent(request):
    return render(request, 'accounts/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        # кодируется через force_bytes почему-то
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'accounts/account_activation_invalid.html')
                