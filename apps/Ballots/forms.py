from django import forms
from django.forms import widgets

class BallotDetails(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(
                 attrs={
            'placeholder':'email',
            'class':"form-control",
            'data-parsley-trigger':"focusin focusout",
            'required':"true",
            'data-parsley-type':"email",
            'data-parsley-ui-enabled':'true'
            
        }
        ))
    
    ballot_name = forms.CharField(
        widget=forms.TextInput(
              attrs={
            'class':"form-control",
            'data-parsley-trigger':"focusin focusout",
            'required':"true",
            'data-parsley-error-message':"Plz enter the Ballot name"
            
        }
        ))
    
    ballot_details =  forms.CharField(
        widget=forms.Textarea(
                attrs={
            'class':"form-control",
            'rows':4,
            'data-parsley-trigger':"focusin focusout",
            'required':"true",
            'data-parsley-length':"[100, 1000]",
            'data-parsley-length-message':"You should use 100-1000 charactors"
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
            'data-parsley-type':"integer",
            'required':"true",
            'data-parsley-error-message':"Plz enter the proposal count"
        }
        ))
    
    CHOICES = [('1', 'Public'), ('2', 'Private')]
    published_method= forms.ChoiceField(
        widget=forms.RadioSelect(
        attrs={
            "class":"form-check-input",
            "id":"method",
            "name":"publish method",
            'required':"true"
               }
     ),
        choices=CHOICES
        )
    
    start_date=forms.DateField( 
        widget=forms.SelectDateWidget(
            attrs={
                'class':'form-control',
                'required':"true",
                'data-parsley-error-message':"Plz enter correct date",
                
            }
        )
       
    )
    
    end_date=forms.DateField(
        widget=forms.SelectDateWidget(
            attrs={
                'class':'form-control',
                'required':"true",
                'data-parsley-error-message':"Plz enter correct date"
          
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
    
