from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from report.models import *
from report.forms import *

def reportUploadStep1(request):
	#control variable in template
	step = "step1"
	
	#checking for posted form
	if request.POST:
		form = reportStep1Form(request.POST)
		#check if all field have been filled
		if form.is_valid():
			m = " ready to save, ok "
			step = "step2"
			
		else:
			m = "ready to save, not ok "	
		
		
	else:
		form = reportStep1Form()
		m = " not ok "
	
		
	context = {'step':step,'form':form,'m':m}
	return render(request, 'reportUpload.html', context)

def reportUploadStep2(request):
	#control variable in template
	step = "step2"
		
	context = {'step':step,}
	return render(request, 'reportUpload.html', context)
	
def reportUploadStep3(request):
	#control variable in template
	step = "step3"
		
	context = {'step':step,}
	return render(request, 'reportUpload.html', context)	
