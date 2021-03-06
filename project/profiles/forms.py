from django import forms

from .models import Profile


class BaseProfileForm(forms.Form):
    first_name = forms.CharField(label='Your First Name', max_length=30,
                                 required=False)
    last_name = forms.CharField(label='Your Last Name', max_length=30,
                                required=False)
    status = forms.ChoiceField(label='Your S&T Status',
                               choices=Profile.STATUS_CHOICES)
    about_me = forms.CharField(label='About Me', widget=forms.Textarea,
                               required=False)
    show_email = forms.BooleanField(label='Show my email address to other H4H users',
                                    required=False)


class SignupForm(BaseProfileForm):

    def signup(self, request, user):
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.profile.status = self.cleaned_data["status"]
        user.profile.about_me = self.cleaned_data["about_me"]
        user.profile.show_my_email = self.cleaned_data["show_email"]
        user.profile.save()
        user.save()


class ProfileForm(BaseProfileForm):
    pass
