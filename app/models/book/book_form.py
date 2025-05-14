from django import forms
from .book_model import BookDemoModel

# Create your forms here.

class BookDemoForm(forms.ModelForm):

    name = forms.CharField(max_length = 100, required=True, help_text='Name')

    email = forms.EmailField(required=True, max_length = 100, help_text='Email', label='Emil')

    institution= forms.CharField(required=True, max_length = 100, help_text='Institution')

    phone = forms.IntegerField(required=True, help_text='Phone Number')

    subject = forms.CharField(max_length = 150, required=True, help_text='Subject')

    message = forms.CharField(max_length = 750, required=True, help_text='Message')
            

    class Meta:
        model = BookDemoModel
        fields = ('name', 'email','institution','phone', 'subject','message')


    

