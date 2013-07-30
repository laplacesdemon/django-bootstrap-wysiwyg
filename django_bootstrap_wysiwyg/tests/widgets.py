from django.test import TestCase
from bs4 import BeautifulSoup
from django_bootstrap_wysiwyg.widgets import WysiwygInput


class WysiwygInputTests(TestCase):

    def test_render_simple(self):
        obj = WysiwygInput()
        attrs = {"id": "id_message"}
        html = obj.render("message", "my value", attrs)
        soup = BeautifulSoup(html)

        self.assertIn("my value", html)
        self.assertIn('class="editor"', html)

        message = soup.find(id="id_message")
        self.assertEqual(message.attrs, {'id': 'id_message', 'class': ['editor']})
        self.assertEqual(message.get_text(), u'\n    my value\n')

        # all toolbar items should be present by default
        toolbar_items = soup.find_all(attrs={"class": "btn-group"})
        self.assertEqual(8, len(toolbar_items))

        toolbar_items_context = obj.get_context("message", "")
        self.assertEqual(9, len(toolbar_items_context['toolbar_items']))

    def test_render_with_attrs(self):
        obj = WysiwygInput()
        attrs = {"class": "my-class", "style": "width:200px", "id": "id_message"}
        html = obj.render("message", "my value", attrs)
        soup = BeautifulSoup(html)

        self.assertIn("my value", html)
        self.assertIn('class="my-class editor"', html)

        message = soup.find(id="id_message")
        self.assertEqual(message.attrs, {'id': 'id_message', 'class': ['my-class', 'editor'], 'style': 'width:200px'})
        self.assertEqual(message.get_text(), u'\n    my value\n')

        # all toolbar items should be present by default
        toolbar_items = soup.find_all(attrs={"class": "btn-group"})
        self.assertEqual(8, len(toolbar_items))

        toolbar_items_context = obj.get_context("message", "")
        self.assertEqual(9, len(toolbar_items_context['toolbar_items']))

    def test_toolbar_options_font(self):
        obj = WysiwygInput(toolbar_items=['fonts'])
        attrs = {"id": "id_message"}
        html = obj.render("message", "my value", attrs)
        soup = BeautifulSoup(html)

        toolbar_items = soup.find_all(attrs={"class": "btn-group"})
        self.assertEqual(1, len(toolbar_items))

    def test_toolbar_options_font_size(self):
        obj = WysiwygInput(toolbar_items=['font_size'])
        attrs = {"id": "id_message"}
        html = obj.render("message", "my value", attrs)
        soup = BeautifulSoup(html)

        toolbar_items = soup.find_all(attrs={"class": "btn-group"})
        self.assertEqual(1, len(toolbar_items))
