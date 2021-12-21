'''
Created on 17-Dec-2021

@author: Rishi

    name = models.CharField(max_length=40, blank=False, null=False)
    duration = models.CharField(max_length=10, blank=False, null=False)
    description =  models.TextField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    review = models.TextField(null=False)
'''
from django import forms
from product.models import Course


class CourseForm(forms.ModelForm):
    
    name = forms.CharField(label="Course Name: " , widget=forms.TextInput(
                                                    attrs=
                                                        {'placeholder' : 'Please Enter Course Name', 
                                                         'size': '40',
                                                        }))
    
    
    class Meta:
        model = Course
        fields = [
            'name',
            'duration',
            'description',
            'price',
            'review',
            ]
        
    
    def clean_name(self):
        get_name = self.cleaned_data.get("name")
        if "H2K" not in get_name:
            raise forms.ValidationError("Name is Invalid")
        return get_name
        
    def clean_duration(self):
        get_duration = self.cleaned_data.get("duration")
        if int(get_duration) >= 6:
            raise forms.ValidationError("Duration should be Less Than 6 Months")
        return get_duration