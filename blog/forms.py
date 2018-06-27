from django import forms
from .models import T_IG, T_document

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)
    
    def clean_message(self):
        message = self.cleaned_data['message']
        if "merde" in message:
            raise forms.ValidationError("Pas d'insultes, on fait de notre mieux!")
        return message
    
class T_IGForm(forms.ModelForm):
    class Meta:
        model = T_IG
        exclude = ('ID_IG', )
            
class importPJ(forms.Form):
    class Meta:
        model = T_document
        exclude = ('dateUp')