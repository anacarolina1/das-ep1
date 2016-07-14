from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from forms import InputForm
from django.views.generic import View, TemplateView
from calculate import calculate_sin, calculate_cos, calculate_tan

class Home(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

def sen(request):
    s = None  # initial value of result
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            radianos = form.radianos
            s = calculate_sin(radianos)
    else:
        form = InputForm()

    return render_to_response('sen.html',
            {'form': form,
             's': '%.5f' % s if isinstance(s, float) else ''
             }, context_instance=RequestContext(request))

def cos(request):
    c = None  # initial value of result
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            radianos = form.radianos
            c = calculate_cos(radianos)
    else:
        form = InputForm()

    return render_to_response('cos.html',
            {'form': form,
             'c': '%.5f' % c if isinstance(c, float) else ''
             }, context_instance=RequestContext(request))

def tan(request):
    t = None  # initial value of result
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            radianos = form.radianos
            t = calculate_tan(radianos)
    else:
        form = InputForm()

    return render_to_response('tan.html',
            {'form': form,
             't': '%.5f' % t if isinstance(t, float) else ''
             }, context_instance=RequestContext(request))




