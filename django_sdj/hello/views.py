import logging as log
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django import forms
from django.shortcuts import render
from django.core.mail import send_mail
from hello.models import Hello

class HelloForm(forms.Form):
    email = forms.EmailField(required=True, label='Your Email Address')
    message = forms.CharField(max_length=4000, required=True, label='Your Message to me', widget=forms.Textarea)


def index(request):
    template = loader.get_template('hello/index.html')
    tmpl = {'hello_who': 'SDJournal.org'}
    if request.method == 'POST':
        form = HelloForm(request.POST)
        if form.is_valid():
            hello = Hello(email=request.POST['email'], message=request.POST['message'])
            hello.save()
            send_mail('Hello from django_sdj', request.POST['message'], request.POST['email'], ['mdagosta@codebug.com'],
                      fail_silently=False)
            return HttpResponseRedirect('/thanks')
    else:
        form = HelloForm()
    tmpl['form'] = form
    context = RequestContext(request, tmpl)
    return HttpResponse(template.render(context))


def thanks(request):
    return render(request, 'hello/thanks.html')


def messages(request):
    tmpl = {'messages': Hello.objects.all()}
    return render(request, 'hello/messages.html', tmpl)
