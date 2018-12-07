from django.shortcuts import get_object_or_404, render
# from django.db.models import Q
from .models import Who, What
from .forms import WhatForm

# Create your views here.

def index(request):
    whats = ()
    what_form = ""
    if request.user.is_authenticated:
        whats = What.objects.order_by('result__id').filter(created_by=request.user)
        what_form = WhatForm()
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            # what_form = WhatForm(request.POST)
            # check whether it's valid:
            #if what_form.is_valid():
            # process the data in form.cleaned_data as required
            action = request.POST.get("action")
            what = What.objects.create(action=action,created_by=request.user)
            if request.POST.get("result"):
                result = What.objects.get(pk=request.POST.get("result"))
                what.result = result
            what.save()
        what_form.fields['result'].choices = (('','[Top]'),)
        for what in whats:
            what_form.fields['result'].choices.append((str(what.id),what.action))
            # form_whats = forms.ModelChoiceField(queryset=whats, empty_label=" ---- ")
    else:
        whats = What.objects.order_by('result__id').filter(public=True)
    
    return render(request, 'why/index.html', {'whats':whats,'what_form':what_form})

def who(request, who_id):
    return render(request, 'why/who.html', {})

def what(request, what_id):
    return render(request, 'why/what.html', {})