import logging as log
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django import forms
from django.shortcuts import render


class HelloForm(forms.Form):
    email = forms.EmailField(required=True, label='Your Email Address')
    message = forms.CharField(max_length=4000, required=True, label='Your Message to me', widget=forms.Textarea)


def index(request):
    template = loader.get_template('hello/index.html')
    tmpl = {'hello_who': 'SDJournal.org'}
    if request.method == 'POST':
        form = HelloForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks')
    else:
        form = HelloForm()
    tmpl['form'] = form
    context = RequestContext(request, tmpl)
    return HttpResponse(template.render(context))


def thanks(request):
    return render(request, 'hello/thanks.html')
