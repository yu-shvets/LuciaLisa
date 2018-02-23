from django import forms
from .models import Specs, Feedback


class SizesForm(forms.Form):

    def __init__(self, pk, *args, **kwargs):
        super(SizesForm, self).__init__(*args, **kwargs)
        self.fields['size'] = forms.ChoiceField(choices=[(i.size, str(i.size)) for i in Specs.objects.filter(item=pk)])


class FeedbackForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['feedback'].widget.attrs['placeholder'] = 'Feedback'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

    class Meta:
        model = Feedback
        fields = ('feedback', 'name', 'email')


