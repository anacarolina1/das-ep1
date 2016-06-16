from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from forms import InputForm
from calculate import calculate_sin, calculate_cos, calculate_tan

def index(request):

    ''' Defines the actions we want to perform when invoking 
        the URL ( here http://127.0.0.1:8000/hw1/).'''

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

    ''' Show pages with the results.'''

    r = form.r
    r2 = form.r2
    r3 = form.r3
    s = calculate_sin(r)
    c = calculate_cos(r2)
    t = calculate_tan(r3)
    return HttpResponse([
        ' seno (%s) = %s --' % (r, s),
        ' cosseno (%s) = %s --' % (r2, c),
        ' tangente (%s) = %s ' % (r3, t)

        ])