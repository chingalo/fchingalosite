from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from reference.models import *
from reference.forms import *


#step 1 for upload reference file
def referenceUploadStep1(request):
	#control variable in template
	step = "step1"
	
	#checking for posted form
	if request.POST:
		form = referenceStep1Form(request.POST)
		#check if all field have been filled
		if form.is_valid():
			m = " page saved and redirect "
			#save the form and shift to step two
			form.save()
			form = referenceStep2Form()
			step = "step2"
			
		else:
			m = "page returned "	
		
		
	else:
		form = referenceStep1Form()
			
		
	context = {'step':step,'form':form,}
	return render(request, 'referenceUpload.html', context)


#step 2 for upload reference file
def referenceUploadStep2(request):
	#control variable in template
	step = "step2"
	
	#checking for posted form
	if request.POST:
		form = referenceStep2Form(request.POST, request.FILES)
		#check if all field have been filled
		if form.is_valid():
			m = " sabed and redirect"
			#save the form and shift to step two
			form.save()
			
			
		else:
			m = "page returned"	
		
		
	else:
		form = referenceStep2Form()
			
		
	context = {'step':step,'form':form,}
	return render(request, 'referenceUpload.html', context)
	

#downloading  reference file 
def referenceDownload(request):
	
	#data form database 
	referenceList = Reference.objects.all()
	fileList = Reference_file.objects.all()
	
	message = "download page for reference, still under development"
	context = {'message':message,'referenceList':referenceList,'fileList':fileList,}
	return render(request, 'downloadreference.html', context)
	

#search for  reference file or detail		
def referenceSearch(request):
	
	
	message = "search page for reference, still under development"
	context = {'message':message,}
	return render(request, 'searchreference.html', context)



	
