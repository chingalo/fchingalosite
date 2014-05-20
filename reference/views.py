from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from reference.models import *
from reference.forms import *

def referenceStep1(request):
	#control variable in template
	step = "step1"
	
	
	context = {'step':step,}
	return render(request, 'referenceUpload.html', context)

def referenceStep2(request):
	#control variable in template
	step = "step2"
	
	
	context = {'step':step,}
	return render(request, 'referenceUpload.html', context)
	
	
