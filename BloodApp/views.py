from django.shortcuts import render, redirect,HttpResponseRedirect
from .forms import *
from .models import *

from django.db.models import Count
# Create your views here.


def index(request):
	donors=Donor.objects.all()
	return render(request,'index.html',{'total':len(donors)})


def add_donor(request):
	form=AddDonor()

	if request.method == 'POST':
		form=AddDonor(request.POST)
		if form.is_valid():
			form.save()
		return redirect('add_donor')
			
	context={'form':form}


	return render(request,'add.html',context)

	
def list_all(request):
	donors=Donor.objects.all()
	context={'donors':donors}
	return render(request,'search.html',context)


def search_result(request):
	query=request.GET['query']
	if len(query)>20:
		donors=Donor.objects.none()
	else:
		donors_name=Donor.objects.filter(donor_name__icontains=query)

		donors_group=Donor.objects.filter(donor_blood_group__icontains=query)

		donors=donors_name.union(donors_group)

	context={'donors':donors}
	return render(request,'searchresult.html',context)



def edit_donor(request,pk):
	if request.method=='POST':
		donor=Donor.objects.get(pk=pk)
		form=AddDonor(request.POST,instance=donor)
		if form.is_valid():
			form.save()
	else:
		donor=Donor.objects.get(pk=pk)
		form=AddDonor(instance=donor)

	return render(request,'edit.html',{'form':form})


def delete_donor(request,pk):
	if request.method=="POST":
		donor=Donor.objects.get(pk=pk)
		donor.delete()
		return redirect('list_all')


def blood_check(request):
	blood=Donor.objects.values('donor_blood_group').annotate(count=Count('pk'))
	return render(request,'blood_check.html',{'blood':blood})