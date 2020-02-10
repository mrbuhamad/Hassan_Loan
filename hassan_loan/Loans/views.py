from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from .models import *
from .forms import *


# ----------- partisipent section ------------#
def participants_list(request):
	participants = Participants.objects.all().order_by("name")

	# for x in participants:
	# 	method_list=[]
	# 	part_dic={}
	# 	part_dic["name"]=x.name
	# 	part_dic["hold"]=x.part_hold_amount()
	# 	part_dic["profit"]=x.part_profit_amount()
	# 	method_list.append(part_dic)
	# 	return method_list
	# part_data=part_dic
	
	context = {
		"participants": participants,
		# 'method_list':method_list
	}
	return render(request, 'part_list.html', context)

def participants_create(request):
	form = ParticipantsForm()
	if request.method == "POST":
		form = ParticipantsForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Successfully Created!")
			return redirect('participants-list')
		print (form.errors)             
	context = {
	"form": form,
	}
	return render(request, "create_participants.html", context)


# ----------- hold_amount section ------------#


def int_hold_amount_list(request,participants_id):
	participants = Participants.objects.get(id=participants_id)
	Hold_amount_obj= Hold_amount.objects.filter(participant=participants)
	form=holdamountForm(request.POST)
	context = {
		"participants": participants,
		"Hold_amount_obj": Hold_amount_obj,
		"form":form
	}
	return render(request, 'hold_list.html', context)

def hold_create(request,participants_id):    
	form=holdamountForm(request.POST)
	participants = Participants.objects.get(id=participants_id)
	if form.is_valid():
		hold=form.save(commit=False)
		hold.participant = participants
		hold.save()
		messages.success(request, "Successfully Created!")
		return redirect('hold-list', participants.id)
	print (form.errors)             
	return render(request, 'hold_list.html', participants.id)


def hold_delete(request, hold_id):                  # --   hold delete templet is not working -- 
	Hold_amount.objects.get(id=hold_id).delete()
	messages.success(request, "Successfully Deleted!")
	return redirect('participants-list')


# ----------- loan list section ------------#
def loan_list(request, participants_id):
	participants = Participants.objects.get(id=participants_id)
	Loan_obj= Loan.objects.filter(participant=participants).order_by("participant")
	context = {
		"participants": participants,
		"loan": Loan_obj,
	}
	return render(request, 'part_detail.html', context)


def loan_create(request,participants_id):   
	form = Loanform(request.POST)
	participants_obj = Participants.objects.get(id=participants_id)
	if request.method == "POST":
		form = ParticipantsForm(request.POST)
		if form.is_valid():
			new_loan=form.save(commit=False)
			new_loan.participant = participants_obj
			new_loan.save()
			messages.success(request, "Successfully Created!")
			return redirect('loan-detail', participants_obj.id)
	context = {
        "form":form,
        "participants_obj":participants_obj
    }
	print (form.errors)             
	return render(request, 'create_loan.html',context )

# ----------- pyment list section ------------#

def pyment_list(request, Loan_id):                       
	Loan_obj= Loan.objects.get(id=Loan_id)
	pyments= Pyments.objects.filter(loan=Loan_obj).order_by("date")
	total_loan=Loan_obj.loan_amount+Loan_obj.hold_amount+Loan_obj.profit_amount   # check if we need this 
	remaining_amount=Loan_obj.totla_loan_amount-Loan_obj.paid_amount			  # check if we need this
	form = Pymentsform()
	context = {
		"loan_obj": Loan_obj,
		"pyments":pyments,
		"remaining_amount":remaining_amount,
		"form": form,
	}
	return render(request, 'pyment_list.html', context)


def pyment_create(request,Loan_id):    
	form = Pymentsform(request.POST)
	Loan_obj= Loan.objects.get(id=Loan_id)
	if form.is_valid():
		pyments=form.save(commit=False)
		pyments.loan = Loan_obj
		pyments.save()
		messages.success(request, "Successfully Created!")
		return redirect('pyment-list', Loan_obj.id)
	print (form.errors)             
	return render(request, 'pyment_list.html', Loan_obj.id)


def pyment_delete(request, pyment_id):          
	Pyments.objects.get(id=pyment_id).delete()
	messages.success(request, "Successfully Deleted!")
	return redirect('participants-list')



# def classroom_update(request, classroom_id):
# 	classroom = Classroom.objects.get(id=classroom_id)
# 	form = ClassroomForm(instance=classroom)
# 	if request.method == "POST":
# 		form = ClassroomForm(request.POST, request.FILES or None, instance=classroom)
# 		if form.is_valid():
# 			form.save()
# 			messages.success(request, "Successfully Edited!")
# 			return redirect('classroom-list')
# 		print (form.errors)
# 	context = {
# 	"form": form,
# 	"classroom": classroom,
# 	}
# 	return render(request, 'update_classroom.html', context)







