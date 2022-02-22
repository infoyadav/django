from django import forms
from .models import Product, Order, Category

# from .models import Product, Order

class CategoryForm(forms.ModelForm):    
    class Meta:
        model = Category
        fields = ("cname",)
        # fields = ("cname",'at_updated')

class ProductForm(forms.ModelForm):  
    # category_type = (
    #     ('Clothes', 'Clothes'),
    #     ('Shoes', 'Shoes'),
    #     ('Electronic', 'Electronic'),
    #     ('Vegitable', 'Vegitable'),
    #     ('Foods', 'Foods'),
    # )
    # category  = forms.ChoiceField(choices=category_type, help_text='*required', label="Select Here Category")

    def clean_field(self):
        image = self.cleaned_data.get('image', False)
        imageType = magic.from_buffer(file.read())
        if not "jpeg" or 'jpg' or 'png' in filetype:
            raise ValidationError("Not Valid Type Image")
        return image
        
    class Meta:
        model = Product
        fields = ("category","pname","ptitle", "quantity", 'price', "image")    

class OrderForm(forms.ModelForm):    
    class Meta:
        model = Order
        fields = ("product", "order_quantity", "date_of_order",)
# django.core.exceptions.FieldError: 'date_of_oder' cannot be specified for Order model form as it is a non-editable field