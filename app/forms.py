from django import forms
from .models import Product
from .models import Order
from .models import Comment

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'stock', 'discount', 'category']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']