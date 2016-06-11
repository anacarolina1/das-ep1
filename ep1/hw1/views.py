from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from models import InputForm
from calculate import calculate

def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            return present_output(form)
    else:
        form = InputForm()

    return render_to_response('hw1.html',
            {'form': form}, context_instance=RequestContext(request))

def present_output(form):
    r = form.r
    s = calculate(r)
    return HttpResponse(' sin(%s)=%s' % (r, s))
