from django.forms import ModelForm
from .models import ClientEmails


class EmailForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

    class Meta:
        model = ClientEmails
        fields = ('email',)
