from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    template = loader.get_template('hello/index.html')
    context = RequestContext(request, {'hello_who': 'SDJournal.org'})
    return HttpResponse(template.render(context))
