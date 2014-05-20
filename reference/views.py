from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from reference.models import *
from reference.forms import *

def referenceStep1(request):
	context = {'message':'step 1'}
	return render(request, 'referenceStep1.html', context)
