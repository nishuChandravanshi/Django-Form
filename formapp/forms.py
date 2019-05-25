from django import forms
from formapp.models import User


class FormName(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


    # botcatcher = forms. CharField(required= False,
                                  # widget = forms.HiddenInput)
                    # refer level 3- form validation lecture

# hidden fields--are present in html but not visible to users..tahts y (required=False) is checked
