from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from report.models import *
from report.models import *

def reportStep1(request):
	context = {'message':'step 1'}
	return render(request, 'reportStep1.html', context)
