Django Bootstrap Wysiwyg
========================

This django app utilizes `bootstrap-wysiwyg` editor in an app. It provides 
a form widget to easily integrate the editor to your forms.

The widget contains some inline javascript, I plan to fix this in future versions.

One thing to note is that image uploading works, there is a drag and drop feature.
The wysiwyg editor is very lightweight. See dependencies and usage sections for more info.

See http://mindmup.github.io/bootstrap-wysiwyg/ for details of the editor.

Installation
------------

Install using the pypi

    pip install django-bootstrap-wysiwyg

or directly frop the source

    pip install git+https://github.com/laplacesdemon/django-bootstrap-wysiwyg.git

Usage
-----

Add `django-bootstrap-wysiwyg` to your APPS.

Make sure that you add dependency javascripts (bootstrap, jquery, this apps js file) before rendering the form. 

Have a look at the `static/django_bootstrap_wysiwyg/css/bootstrap-wysiwyg.css` file, and modify it for your needs.

Change the textarea widget to `WysiwygInput` widget. See options section for more information.

    class MyForm(forms.ModelForm):
        class Meta:
            model = MyModel
            widgets = {
                'myfield': WysiwygInput()
            }

That's it. See sample project to see how it's like.

Options
-------

Wysiwyg editor has an optional toolbar. You can determine what features you want on the toolbar. 

The default setting for toolbar is `WYSIWYG_DEFAULT_TOOLBAR_ITEMS`. Just add or remove the items as you wish.
Following is the default value of it.

    WYSIWYH_DEFAULT_TOOLBAR_ITEMS = [
        'fonts', 
        'font_size', 
        'font_weights', 
        'lists',
        'alignments', 
        'hyperlink', 
        'image',  
        'history',  # undo/redo buttons
        'speech'  # only available for chrome
    ]

You can override these options per widget object:

    WysiwygInput(toolbar_items=[
        'fonts', 'font-sizes', 'alignments'
        ]))

The editor is a `div` element and by default a css class is added by the application. You can change it
by the following setting:

    WYSIWYG_DEFAULT_CSS_CLASS = 'editor'

Dependencies
------------
`bootsrap-wysiwyg` dependencies

* jQuery http://jquery.com/
* jQuery HotKeys https://github.com/jeresig/jquery.hotkeys
* Bootstrap http://twitter.github.com/bootstrap/
