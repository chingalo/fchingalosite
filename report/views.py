from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from report.models import *
from report.models import *

def reportStep1(request):
	#control variable in template
	step = "step1"
		
	context = {'step':step,}
	return render(request, 'reportUpload.html', context)

def reportStep2(request):
	#control variable in template
	step = "step2"
		
	context = {'step':step,}
	return render(request, 'reportUpload.html', context)
	
def reportStep3(request):
	#control variable in template
	step = "step3"
		
	context = {'step':step,}
	return render(request, 'reportUpload.html', context)	
