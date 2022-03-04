from django import forms
from django.forms import widgets

class BallotDetails(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(
                 attrs={
            'placeholder':'email',
            'class':"form-control",
            'data-parsley-trigger':"change",
            'required':"",
            'data-parsley-type':"email"
            
        }
        ))
    
    ballot_name = forms.CharField(
        widget=forms.TextInput(
              attrs={
            'class':"form-control",
            'data-parsley-trigger':"change",
            'required':""
            
        }
        ))
    
    ballot_details =  forms.CharField(
        widget=forms.Textarea(
                attrs={
            'class':"form-control",
            'rows':4,
            'data-parsley-trigger':"change",
            'required':""
        }
        ))
    
    
    # ballot_type_choices=[
    #     ('1','1'),('2','2'),('3','3')
    # ]
    # ballot_type = forms.CharField(
    #     widget=forms.Select(
    #         choices=ballot_type_choices,
    #         attrs={
    #             'class':"form-control"
    #         }
    #     )
      
    # )
    proposal_count = forms.CharField(
        widget=forms.NumberInput(
        attrs={
            'class':"form-control",
            'min':2,
            'id':'prop_num',
            'data-parsley-type':"integer"
        }
        ))
    
    CHOICES = [('1', 'Public'), ('2', 'Private')]
    published_method= forms.ChoiceField(
        widget=forms.RadioSelect(
        attrs={
            "class":"form-check-input",
            "id":"method",
            "name":"publish method"
               }
     ),
        choices=CHOICES
        )
    
    start_date=forms.DateField( 
        widget=forms.SelectDateWidget(
            attrs={
                'class':'form-control'
            }
        )
       
    )
    
    end_date=forms.DateField(
        widget=forms.SelectDateWidget(
            attrs={
                'class':'form-control',
          
            }
        )
    )
   
    # CHOICES = [('1', 'I agree'), ('2', 'Send the all the updates via email')]
    # agrements= forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple(
    #     #     attrs={
    #     # "class":"form-check-input"
    #     #        }
    #  ),
    # choices=CHOICES
    #     )
    
