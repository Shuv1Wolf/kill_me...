from django.forms import ModelForm, TextInput, NumberInput
from .models import paymentModel1, paymentModel2, paymentModel3, paymentModelAll

# тестовые формы
class paymentForm1(ModelForm):
    class Meta:
        model = paymentModel1
        fields = ['field']
        widgets = {
            'field': NumberInput(attrs={
                'class': "form-control",
                'placeholder': "Цена",
                'aria-label': "Цена",
            })
        }


class paymentForm2(ModelForm):
    class Meta:
        model = paymentModel2
        fields = ['field']
        widgets = {
            'field': NumberInput(attrs={
                'class': "form-control",
                'placeholder': "Цена",
                'aria-label': "Цена",
            })
        }


class paymentForm3(ModelForm):
    class Meta:
        model = paymentModel3
        fields = ['field']
        widgets = {
            'field': NumberInput(attrs={
                'class': "form-control",
                'placeholder': "Цена",
                'aria-label': "Цена",
            })
        }


# релизная форма
class paymentFormAll(ModelForm):
    class Meta:
       model = paymentModelAll
       fields = ['field1', 'field2', 'field3']
       widgets = {
           'field1': NumberInput(attrs={
               'class': "form-control",
               'placeholder': "Цена",
               'aria-label': "Цена",
           }),
           'field2': NumberInput(attrs={
               'class': "form-control",
               'placeholder': "Цена",
               'aria-label': "Цена",
           }),
           'field3': NumberInput(attrs={
               'class': "form-control",
               'placeholder': "Цена",
               'aria-label': "Цена",
           })
       }