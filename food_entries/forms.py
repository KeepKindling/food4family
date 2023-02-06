from django import forms
from django.forms import ModelForm
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    family_name = forms.CharField(max_length=30, label='Family name')

    def signup(self, request, user):
        user.last_name = self.cleaned_data['last_name']
        user.save()

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.
        user.last_name = self.cleaned_data['last_name']

        # You must return the original result.
        return user


# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = FamilyMember()
#         fields = ['family_name']

#     def signup(self, request, user):
#         user.family_name = self.cleaned_data['family_name']
#         save()
