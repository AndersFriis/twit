from django import forms
from .models import Post


"""forms.py is set up for the form on the webpage. So on the webpage you have a text box 
and you put in your name and text and you hit submit.. 
The textbox on the webpage is just used to create posts
Remember to import to views.py (from forms import--> here you put the class name )
So it would look like this= from forms import Tweet 
Also remember to put in the form logic in your html

"""
class PostForm(forms.ModelForm):
    

    class Meta:
        model = Post
        fields = ( 'description', )