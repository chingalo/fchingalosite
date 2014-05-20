from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from reference.models import *
from reference.forms import *

def referenceUploadStep1(request):
	#control variable in template
	step = "step1"
	
	#checking for posted form
	if request.POST:
		form = referenceStep1Form(request.POST)
		#check if all field have been filled
		if form.is_valid():
			m = " ready to save, ok "
			#save the form and shift to step two
			#form.save()
			form = referenceStep2Form()
			step = "step2"
			
		else:
			m = "ready to save, not ok "	
		
		
	else:
		form = referenceStep1Form()
		m = " not ok "
	
		
	context = {'step':step,'form':form,'m':m}
	return render(request, 'referenceUpload.html', context)

def referenceUploadStep2(request):
	#control variable in template
	step = "step2"
	
	#checking for posted form
	if request.POST:
		form = referenceStep2Form(request.POST, request.FILES)
		#check if all field have been filled
		if form.is_valid():
			m = " ready to save, ok "
			#save the form and shift to step two
			#form.save()
			
			
		else:
			m = "ready to save, not ok "	
		
		
	else:
		form = referenceStep2Form()
		m = " not ok "
	
		
	context = {'step':step,'form':form,'m':m}
	return render(request, 'referenceUpload.html', context)
	
	
