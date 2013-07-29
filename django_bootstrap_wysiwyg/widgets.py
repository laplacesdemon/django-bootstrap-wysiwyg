import string
import random
from django.forms import Widget
from django.template import loader
from .utils import setting


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class WysiwygInput(Widget):
    template_name = 'django_bootstrap_wysiwyg/input.html'

    # default css class of the editor element
    css_class = setting(
        "WYSIWYG_DEFAULT_CSS_CLASS",
        "editor"
    )

    # default toolbar items can be overridden via the constructor parameter
    toolbar_items = setting(
        "WYSIWYH_DEFAULT_TOOLBAR_ITEMS",
        ['fonts', 'font_size', 'font_weights', 'lists',
         'alignments', 'hyperlink', 'image', 'history', 'speech']
    )

    def __init__(self, attrs=None, toolbar_items=None):
        if toolbar_items:
            self.toolbar_items = toolbar_items
        return super(WysiwygInput, self).__init__(attrs)

    def get_context(self, name, value, attrs=None):
        context = {}
        context['attrs'] = self.build_attrs(attrs)
        context['name'] = name
        context['value'] = value
        context['toolbar_items'] = self.toolbar_items

        # make sure that context has an id
        if "tag_id" not in context:
            context['tag_id'] = id_generator()

        # add the default css class if doesn't exists
        if "class" in context['attrs']:
            classes = context['attrs']['class'].split(" ")
            if self.css_class not in classes:
                classes.append(self.css_class)
                context['attrs']['class'] = " ".join(classes)
        else:
            context['attrs']['class'] = self.css_class

        return context

    def render(self, name, value, attrs=None):
        """returns the html of wysiwyg input"""
        context = self.get_context(name, value, attrs)
        return loader.render_to_string(
            self.template_name,
            context
        )
