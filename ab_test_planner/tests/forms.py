from django import forms
from .models import ABTest, ABTestVariant, ABTestOutcome

class ABTestForm(forms.ModelForm):
    class Meta:
        model = ABTest
        fields = ['name', 'description', 'start_date', 'end_date']

class ABTestVariantForm(forms.ModelForm):
    class Meta:
        model = ABTestVariant
        fields = ['name', 'description']

class ABTestOutcomeForm(forms.ModelForm):
    class Meta:
        model = ABTestOutcome
        fields = ['metric', 'baseline', 'goal']
