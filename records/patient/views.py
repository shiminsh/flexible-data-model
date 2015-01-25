from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.generic import FormView, ListView, DetailView
from django.contrib import auth
from patient.forms import *
from patient.models import *
from itertools import chain
from django.core.urlresolvers import reverse

class RegisterUser(FormView):
     template_name='register.html'
     form_class=RegistrationForm
     success_url='/register/'

     def form_valid(self, form):
        form.save()
        return super(RegisterUser, self).form_valid(form)

class UserListView(ListView):
    model = Register
    template_name = 'records.html'

def search(request):
    search = request.GET['q']
    a_list = Register.objects.filter(firstname__icontains=search)
    b_list = Register.objects.filter(lastname__icontains=search)
    c_list = Register.objects.filter(age__icontains=search)
    d_list = Register.objects.filter(contactno__icontains=search)
    e_list = Register.objects.filter(doctor__icontains=search)
    data = list(chain(a_list, b_list, c_list, d_list, e_list))
    return render_to_response('records.html', {'object_list':data})
 
class PatientDetail(DetailView):
    template_name = 'individual_record.html'
    model = Register

def patient_detail(request, pk):
    field_list = ['report', 'disease', 'cured', 'symptom', 'doctor', 'prescription']
    patient = Register.objects.get(id=pk)
    diseases = patient.disease_set.all()
    return render_to_response('individual_record.html',{'object':patient, 'form':DiseaseForm, 'diseases':diseases},context_instance=RequestContext(request))

def patient_disease(request, pk):
    if request.method=="POST":
        patient = Register.objects.get(id=pk)
        diseases = patient.disease_set.all()
        # for key, value in request.GET.iteritems():
        #     if key not in field_list:
        #         Schema.objects.create(title=key, name=key.lower(), datatype=Schema.TYPE_TEXT)
        # for key, value in request.GET.iteritems():
        form = DiseaseForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.patient = Register.objects.get(id=pk)
            f.save()
            return reverse("individual", kwargs={"pk": pk})
        else:
            return render_to_response('individual_record.html',{'object':patient, 'form':form, 'diseases':diseases}, context_instance=RequestContext(request))
    else:
        HttpResponse('ok')