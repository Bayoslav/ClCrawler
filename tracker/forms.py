from django import forms
from .models import CarModel,Podesavanja
class CarForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name of the model','aria-describedby': 'sizing-addon3'}))
    link = forms.URLField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter car search link here','aria-describedby': 'sizing-addon3'}))
    #url = forms.URLField(label='Your website', required=False)
    #list_choices = ['Texas','Alabama']
    OPTIONS = [("Alaska", "Alaska"),
                 ( "Alabama","Alabama"),
                  ("Arkansas","Arkansas"),
                  ("Arizona", "Arizona"),
                  ("California","California"),
                  ("Colorado","Colorado"),
                  ("Connecticut","Connecticut"),
                  ("Delaware","Delaware"),
                  ("Florida","Florida"),
                  ("Georgia","Georgia"),
                  ("Hawaii","Hawaii"),
                  ("Iowa","Iowa"),
                  ("Idaho","Idaho"),
                  ("Illinois","Illinois"),
                  ("Indiana","Indiana"),
                  ("Kansas","Kansas"),
                  ("Kentucky","Kentucky"),
                  ("Louisiana","Louisiana"),
                  ("Massachusetts","Massachusetts"),
                  ("Maryland","Maryland"),
                  ("Maine","Maine"),
                  ("Michigan","Michigan"),
                  ("Minnesota","Minnesota"),
                  ("Missouri","Missouri"),
                  ("Mississippi","Mississippi"),
                  ("Montana","Montana"),
                  ("North Carolina","North Carolina"),
                  ("North Dakota","North Dakota"),
                  ("Nebraska","Nebraska"),
                  ("New Hampshire","New Hampshire"),
                  ("New Jersey","New Jersey"),
                  ("New Mexico","New Mexico"),
                  ("Nevada","Nevada"),
                  ("New York","New York"),
                  ("Ohio","Ohio"),
                  ("Oklahoma","Oklahoma"),
                  ("Oregon","Oregon"),
                  ("Pennsylvania","Pennsylvania"),
                  ("South Carolina","South Carolina"),
                  ("South Dakota","South Dakota"),
                  ("Tennessee","Tennessee"),
                  ("Texas","Texas"),
                  ("Utah","Utah"),
                  ("Virginia","Virginia"),
                  ("Vermont","Vermont"),
                  ("Washington","Washington"),
                  ("Wisconsin","Wisconsin"),
                  ("West Virginia","West Virginia"),
                  ("Wyoming","Wyoming"),]
    states = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=OPTIONS)
    class Meta:
        model = CarModel
        fields = ("name","link","states")

class SettingsForm(forms.ModelForm):
    STATUS_CHOICES = (('Start','Start'),
                    ('Stop','Stop'),)
    o = Podesavanja.objects.get(id=1)

    proxylist = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder' : "0.00.0:8000','123.45.67.8910'",'class' : 'uk-input uk-width-1-2', 'style': 'width: 100%; margin: 20px 0px; border-radius: 10px;', 'value' : o.proxylist}))
    status = forms.ChoiceField(required=False, choices=STATUS_CHOICES, initial=o.status)
    #description = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder' : 'Please enter the  description', 'size' : 300, 'class' : 'uk-input uk-width-1-2', 'style': 'width: 100%; margin: 20px 0px; border-radius: 10px;','cols': 120, 'rows': 50}))
    class Meta:
        model = Podesavanja
        fields = ("proxylist", "status")
    