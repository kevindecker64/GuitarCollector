from django.forms import ModelForm
from .models import SetUp

class SetUpForm(ModelForm):
    class Meta:
        model = SetUp
        fields = ['date', 'service']