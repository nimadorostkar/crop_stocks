from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User
from .models import Profile, Payment
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm





#------------------------------------------------------------------------------
class PaymentForm(forms.ModelForm):
	class Meta:
		model = Payment
		fields = ['descriptions', 'photo']



#------------------------------------------------------------------------------
class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = [
        'father_name',
        'identity_number',
        'national_code',
		'phone',
        'address',
        'bank_name',
        'account_holder',
        'cardـnumber',
        'user_photo',
        'signature',
        'personalـphoto']



#------------------------------------------------------------------------------
class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password1','password2']






class MyCustomSignupForm(SignupForm):
	def __init__(self, *args, **kwargs):
		super(MyCustomSignupForm, self).__init__(*args, **kwargs)
		self.fields['organization'] = forms.CharField(required=True)
		self.fields['bank'] = forms.CharField(required=True)
	def save(self, request):
		organization = self.cleaned_data.pop('organization')
		bank = self.cleaned_data.pop('bank')
		...
		user = super(MyCustomSignupForm, self).save(request)






'''

# SpyBookSignupForm inherits from django-allauth's SignupForm
class SpyBookSignupForm(SignupForm):

    # Specify a choice field that matches the choice field on our user model
    type = forms.ChoiceField(choices=[("SPY", "Spy"), ("DRIVER", "Driver")])

    # Override the init method
    def __init__(self, *args, **kwargs):
        # Call the init of the parent class
        super().__init__(*args, **kwargs)
        # Remove autofocus because it is in the wrong place
        del self.fields["username"].widget.attrs["autofocus"]

    # Put in custom signup logic
    def custom_signup(self, request, user):
        # Set the user's type from the form reponse
        user.type = self.cleaned_data["type"]
        # Save the user's type to their database record
        user.save()

'''


#------------------------------- Forms End -----------------------------------