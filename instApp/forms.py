from django import forms
from .models import Post
from crispy_forms.helper import formhelper
from crispy_forms.layout import submit,Layout,field

class PostForm(forms.modelform):
      helper = formhelper()
      helper.form_method = 'POST'
      helper.add_input(submit('post','post',css_class='btn-primary'))

      class meta:
          model = post
          fields = [
              'image',
              'caption'
          ]

  
