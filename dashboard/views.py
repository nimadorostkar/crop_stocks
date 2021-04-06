from .models import Profile, Notice, Payment, Submitted_files, Ticket, Money_req
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from .forms import ProfileForm, UserForm, PaymentForm, TicketForm, Money_reqForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.db import transaction
from django.conf import settings
from django import forms
from . import models
import random





#------------------------------------------------------------------------------
@login_required
@transaction.atomic
def dashboard(request):
  profile = models.Profile.objects.filter(user=request.user)
  notices = models.Notice.objects.filter(user=request.user).order_by('-created_on')
  payment = models.Payment.objects.filter(user=request.user).order_by('-created_on')
  ticket = models.Ticket.objects.filter(user=request.user).order_by('-created_on')
  money_req = models.Money_req.objects.filter(user=request.user).order_by('-created_on')
  submitted_files = models.Submitted_files.objects.filter(user=request.user).order_by('-created_on')

  if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            context = {'profile': profile,'notices': notices,'payment': payment,'ticket': ticket ,'money_req': money_req,'submitted_files':submitted_files, 'user_form': user_form,'profile_form': profile_form }
            return render(request, 'dashboard/dashboard.html', context)
        else:
            messages.error(request, _('Please correct the error below.'))
  else:
      user_form = UserForm(instance=request.user)
      profile_form = ProfileForm(instance=request.user.profile)

  context = {
  'profile': profile,
  'notices': notices,
  'payment': payment,
  'ticket': ticket,
  'money_req': money_req,
  'user_form': user_form,
  'submitted_files':submitted_files,
  'profile_form': profile_form }
  return render(request, 'dashboard/dashboard.html', context)






#------------------------------------------------------------------------------
@login_required
@transaction.atomic
def payment(request):
    if request.method == 'POST':
        payment_form=PaymentForm(request.POST, request.FILES, instance=request.user)
        if payment_form.is_valid():
            obj = Payment() #gets new object
            obj.descriptions = payment_form.cleaned_data['descriptions']
            obj.photo = payment_form.cleaned_data['photo']
            obj.user = payment_form.created_by=request.user
            obj.save()
            messages.success(request, _('Your Payment was successfully updated!'))
            return redirect('/dashboard')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
      payment_form=PaymentForm(request.POST, request.FILES, instance=request.user)
      context = {'payment_form': payment_form }
      return render(request, 'dashboard/payment.html', context)








#------------------------------------------------------------------------------
@login_required
@transaction.atomic
def ticket(request):
    if request.method == 'POST':
        ticket_form=TicketForm(request.POST, request.FILES, instance=request.user)
        if ticket_form.is_valid():
            obj = Ticket() #gets new object
            obj.title = ticket_form.cleaned_data['title']
            obj.descriptions = ticket_form.cleaned_data['descriptions']
            obj.user = ticket_form.created_by=request.user
            obj.save()
            messages.success(request, _('Your Payment was successfully updated!'))
            return redirect('/dashboard')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
      ticket_form=TicketForm(request.POST, request.FILES, instance=request.user)
      context = {'ticket_form': ticket_form }
      return render(request, 'dashboard/ticket.html', context)





#------------------------------------------------------------------------------
@login_required
@transaction.atomic
def money_req(request):
    if request.method == 'POST':
        money_req_form=Money_reqForm(request.POST, request.FILES, instance=request.user)
        if money_req_form.is_valid():
            obj = Money_req() #gets new object
            obj.amount = money_req_form.cleaned_data['amount']
            obj.descriptions = money_req_form.cleaned_data['descriptions']
            obj.user = money_req_form.created_by=request.user
            obj.save()
            messages.success(request, _('Your Payment was successfully updated!'))
            return redirect('/dashboard')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
      money_req_form=Money_reqForm(request.POST, request.FILES, instance=request.user)
      context = {'money_req_form': money_req_form }
      return render(request, 'dashboard/money_req.html', context)









#--------------------------------- Views End ----------------------------------
