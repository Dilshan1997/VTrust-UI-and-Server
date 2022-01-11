from django import forms
from django.forms import widgets


class BallotDetails(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
                 attrs={
            'placeholder':'email',
            'class':"form-control",
            
        }
        ))
    
    ballot_name = forms.CharField(
        widget=forms.TextInput(
              attrs={
            'class':"form-control",
            
        }
        ))
    
    ballot_details =  forms.CharField(
        widget=forms.Textarea(
                attrs={
            'class':"form-control",
            'rows':4
            
        }
        ))
    
    
    ballot_type_choices=[
        ('1','1'),('2','2'),('3','3')
    ]
    ballot_type = forms.CharField(
        widget=forms.Select(
            choices=ballot_type_choices,
            attrs={
                'class':"form-control"
            }
        )
      
    )
    proposal_count = forms.CharField(
        widget=forms.NumberInput(
        attrs={
            'class':"form-control",
            'min':2
        }
        ))
    
    CHOICES = [('1', 'Public'), ('2', 'Private')]
    publish_method= forms.ChoiceField(
        widget=forms.RadioSelect(
        attrs={
            "class":"form-check-input"
               }
     ),
        choices=CHOICES
        )
    
    start_date=forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],

        widget=forms.DateTimeInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    end_date=forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                'class':'form-control',
          

            }
        )
    )
    
   

    
    
