from django import forms


class ContactForm(forms.ModelForm):
    """
    Create a new ticket from contact
    form using ticket model
    """
    class Meta:
        fields = ('name', 'email', 'message',)
