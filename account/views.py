from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from .forms import FormLogin, OtpLoginForm, CzechOtpForm, UserProFileForm, TeacherForm
import ghasedakpack
from random import randint
from .models import Otp, User
from videos.models import Video, Notification
from django.utils.crypto import get_random_string
from uuid import uuid4
from .mixins import FieldsMixin , FormValidMixin, UpdateMixin
from django.contrib.auth.mixins import LoginRequiredMixin

SMS = ghasedakpack.Ghasedak("beee4729b279b215bd79847db9fb83756ec7002da0ef4b2a458ac2f55fed188c")


class Register_Login_View(View):
    def get(self, request):
        form = OtpLoginForm()
        return render(request, "account/register.html", {"form":form})

    def post(self, request):
        form = OtpLoginForm(request.POST)
        if form.is_valid():
            cd =  form.cleaned_data
            rendercode = randint(1000,9999)
            SMS.verification({'receptor': cd["number"],'type': '1','template': 'nordpython','param1': rendercode})
            token = str(uuid4())
            Otp.objects.create(number=cd["number"], code=rendercode, token=token)
            return redirect(reverse("account:check_otp") + f'?token={token}')
        else:
            form.add_error("number", 'شماره تلفن متعبر نمی باشد ')
        return render(request, "account/register.html", {"form":form})



class CzechOtpView(View):
    def get(self, request):
        form = CzechOtpForm()
        return render(request, "account/check_otp.html", {"form":form})

    def post(self, request):
        token = request.GET.get('token')
        form = CzechOtpForm(request.POST)
        if form.is_valid():
            cd =  form.cleaned_data
            if Otp.objects.filter(code=cd["code"], token=token).exists():
                otp = Otp.objects.get(token=token)
                user, is_create = User.objects.get_or_create(number=otp.number)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                otp.delete()
                return redirect("account:panel_user")

        else:
            form.add_error("code", 'کد متبعر نمی باشد')
        return render(request, "account/check_otp.html", {"form":form})

# panel user article
class PanelUser(LoginRequiredMixin, ListView):
    template_name = "account/panel_users.html"

    def get_queryset(self):
        if self.request.user.is_admin:
            superusers = Video.objects.all()
            return superusers
        else:
            superuser = Video.objects.filter(user=self.request.user)
            return superuser

#  panel view list video
class PanelCreateUser(FieldsMixin, FormValidMixin, CreateView):
    model = Video
    template_name = "account/panelcreateuser.html"


# panel update list video
class PanelUpdateUser(FieldsMixin, FormValidMixin, UpdateMixin, UpdateView):
    model = Video
    template_name = "account/panelcreateuser.html"

# panel user is profile users
class ProfileUser(UpdateView):
    model = User
    form_class = UserProFileForm
    template_name = "account/profile.html"

# panel user is TeacherForm
class author_about(UpdateView):
    model = User
    form_class = TeacherForm
    template_name = "account/author.html"

# panel Notification admin true
class NotificationView(ListView):
    template_name = "account/notification.html"

    def get_queryset(self):
        if self.request.user.is_admin:
            superusers = Notification.objects.all()
            return superusers

# panel Notification admin
class NotificationUpdate(UpdateView):
    template_name = "account/notification_update.html"
    model = Notification
    fields = "__all__"

    def get_success_url(self):
        return reverse('account:notifications')

# panel Notification admin
class NotificationCreate(CreateView):
    template_name = "account/notification_create.html"
    model = Notification
    fields = "__all__"

    def get_success_url(self):
        return reverse('account:notifications')



def user_logout(request):
    logout(request)
    return redirect('home:home')
