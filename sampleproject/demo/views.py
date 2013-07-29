from django.views.generic.edit import FormView, CreateView, UpdateView
from .forms import MessageForm, MultipleInputForm
from .models import Message


class MessageCreateView(CreateView):
    template_name = 'demo/message.html'
    model = Message
    form_class = MessageForm


class MessageUpdateView(UpdateView):
    template_name = 'demo/message.html'
    model = Message
    form_class = MessageForm


class MultipleTextView(FormView):
    template_name = 'demo/multiple.html'
    form_class = MultipleInputForm
    success_url = '/'
