from django import forms


class OrderCheckoutForm(forms.ModelForm):
    """
    Checkout form for users order
    """
    last_name = forms.CharField(widget=forms.TextInput(), required=True)
    first_name = forms.CharField(widget=forms.TextInput(), required=True)
    email = forms.CharField(widget=forms.TextInput(), required=True)