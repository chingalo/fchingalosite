from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from report.models import *
from report.forms import *

def reportUploadStep1(request):
	#control variable in template
	step = "step1"
	form = reportStep1Form()
		
	context = {'step':step,'form':form}
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
