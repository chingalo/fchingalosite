from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from report.models import *
from report.forms import *

#step 1 for upload report file
def reportUploadStep1(request):
	#control variable in template
	step = "step1"
	
	#checking for posted form
	if request.POST:
		form = reportStep1Form(request.POST)
		#check if all field have been filled
		if form.is_valid():
			
			#save the form and shift to step two
			form.save()
			form = reportStep2Form()
			step = "step2"
			
		else:
			m = "page returned "	
		
		
	else:
		form = reportStep1Form()
			
		
	context = {'step':step,'form':form,}
	return render(request, 'reportUpload.html', context)


#step 2 for upload report file
def reportUploadStep2(request):
	#control variable in template
	step = "step2"
		
	#checking for posted form
	if request.POST:
		form = reportStep2Form(request.POST)
		#check if all field have been filled
		if form.is_valid():
			#save the form and shift to step two
			form.save()
			form = reportStep3Form()
			step = "step3"
			
		else:
			m = "page returned"	
		
		
	else:
		form = reportStep2Form()
			
		
	context = {'step':step,'form':form,}
	return render(request, 'reportUpload.html', context)


#step 3 for upload report file	
def reportUploadStep3(request):
	#control variable in template
	step = "step3"
		
	#checking for posted form
	if request.POST:
		form = reportStep3Form(request.POST, request.FILES)
		#check if all field have been filled
		if form.is_valid():
			m = "saved and redirect to home page"
			#save the form and shift to step two
			form.save()
			return HttpResponseRedirect('/report/')
			
		else:
			m = "page returned"	
		
		
	else:
		form = reportStep3Form()
			
		
	context = {'step':step,'form':form,}
	return render(request, 'reportUpload.html', context)	


#downloading report file
def reportDownload(request):
	
	#data form database 		
	receiverList =  Receiver_of_report.objects.all()
	reportList = Details_of_Report.objects.all()
	fileList = Report_files.objects.all()
	
	message = "download page for report, still under development"
	context = {'message':message,'receiverList':receiverList,'reportList':reportList,'fileList':fileList,}
	return render(request, 'downloadreport.html', context)


#search for  report file or detail	
def reportSearch(request):
	page = ''
	searchedReportTitle = ''
	searchedReceiver = ''
	fileList = Report_files.objects.all()
	resultOfReceiver = []
	resultOfReport = []
	receiverList =  Receiver_of_report.objects.all()
	reportList = Details_of_Report.objects.all()
	message = "search page for report, still under development"
	
	if  request.POST:
		page = 'searchResults'		
		form = request.POST
		#taking values  report_title    name_of_receiver  reciver  report .filter(title__icontains=q)
		SearchList = form.getlist('reciver')
		searchedReceiver= SearchList[0]
		
		SearchList = form.getlist('report')
		searchedReportTitle = SearchList[0]
		
		#filter form database based on values in form
		if searchedReceiver != "":
			resultOfReceiver = Receiver_of_report.objects.filter(name_of_receiver__icontains = searchedReceiver)
		if 	searchedReportTitle != "":
			resultOfReport = Details_of_Report.objects.filter(report_title__icontains = searchedReportTitle)
		if 	searchedReportTitle != "" and searchedReceiver != "":
			resultOfReceiver = Receiver_of_report.objects.filter(name_of_receiver__icontains = searchedReceiver)
			resultOfReport = Details_of_Report.objects.filter(report_title__icontains = searchedReportTitle)							
	
	
	context = {'message':message,'reportList':reportList,'receiverList':receiverList,'page':page,'fileList':fileList,'resultOfReceiver':resultOfReceiver,'resultOfReport':resultOfReport,'searchedReportTitle':searchedReportTitle,'searchedReceiver':searchedReceiver,}
	return render(request, 'searchreport.html', context)	
	
	
	
	
