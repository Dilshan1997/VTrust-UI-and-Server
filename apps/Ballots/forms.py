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
            'id':'prop_num'
        }
        ))
    
    CHOICES = [('1', 'Public'), ('2', 'Private')]
    published_method= forms.ChoiceField(
        widget=forms.RadioSelect(
        attrs={
            "class":"form-check-input"
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
    # for _ in range(prop_count):
    #     prop_name=forms.CharField(
    #         widget=forms.TextInput(
    #                     attrs={
    #                 'class':'form-control'
    #             }
            

    #         )
    #     )
        
    #     prop_details=forms.CharField(
    #         widget=forms.TextInput(
    #                     attrs={
    #                 'class':'form-control'
    #             }
            
    #         )
    #     )

    
    
