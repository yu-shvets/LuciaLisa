from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import EmailForm
from django.http import JsonResponse


class EmailCreateView(CreateView):
    form_class = EmailForm
    response_data = {}

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.save()
        self.response_data['message'] = 'Success!'
        return JsonResponse(self.response_data)


