from django import forms


class SearchForm(forms.Form):

    city = forms.CharField()
