from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView

from main.forms import ContactForm


def home(request):
    return render(request, 'main/home.html')


def bouquets(request):
    return render(request, 'main/bouquets.html')


def bouquets_nevest(request):
    return render(request, 'main/bouquets_nevest.html')


def compositions(request):
    return render(request, 'main/compositions.html')


def slider(request):
    return render(request, 'main/slider.html')


def contact(request):
    return render(request, 'main/contact.html')


class RegisterView(FormView):
    form_class = ContactForm
    template_name = 'main/send_email_error.html'

    def form_valid(self, form):
        # проверка валидности reCAPTCHA
        if self.request.recaptcha_is_valid:
            if self.request.method == 'POST':
                form = ContactForm(self.request.POST)
                if form.is_valid():
                    name = form.cleaned_data['name']
                    phone = form.cleaned_data['phone']
                    body = form.cleaned_data['body']
                    recipients = ['sasha1997com@gmail.com']
                    try:
                        send_mail('Обратный звонок',
                                  'Обратный звонок с сайта Цветочный больвар' + "\n" + name + "\n" + phone + "\n" + body,
                                  'noreply.flowers5430@mail.ru', recipients,
                                  fail_silently=False, )
                    except BadHeaderError:
                        return HttpResponse('Invalid header found')
                    return render(self.request, 'main/send_email_success.html', self.get_context_data())
        return render(self.request, 'main/send_email_error.html', self.get_context_data())

