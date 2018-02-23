from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import TemplateView, DetailView
from django_filters import FilterSet, ModelMultipleChoiceFilter
from django import forms
from django_filters.views import FilterView
from .models import Category, Item, Specs
from .forms import SizesForm, FeedbackForm
from django.http import JsonResponse
from django.urls import reverse
from company.forms import EmailForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.formats import date_format
from django.utils.dateformat import DateFormat


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = EmailForm
        return context


class CategoryFilter(FilterSet):
    category = ModelMultipleChoiceFilter(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Item
        fields = ['category']


class CategoryFilterView(FilterView):
    template_name = 'products/catalogue.html'
    filterset_class = CategoryFilter


class ItemDetailView(DetailView):
    model = Item
    template_name = 'products/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['form'] = SizesForm(pk=self.kwargs.get('pk'))
        context['feedback_form'] = FeedbackForm
        return context


def update_size(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    response_data = {}
    if request.method == 'POST':
        chosen_size = request.POST['size']
        specs = Specs.objects.filter(size=chosen_size, item=item).first()
        response_data['price'] = specs.price
        response_data['size_id'] = specs.id
    return JsonResponse(response_data)


class FeedbackCreateView(SuccessMessageMixin, CreateView):
    form_class = FeedbackForm
    success_message = 'Your feedback was successfully submitted'

    def form_valid(self, form):
        response_data = {}
        obj = form.save(commit=False)
        obj.item = Item.objects.get(pk=self.kwargs['item_id'])
        obj.save()
        response_data['feedback'] = obj.feedback
        response_data['name'] = obj.name
        response_data['created'] = DateFormat(obj.created).format('d-m-Y')
        return JsonResponse(response_data)

    def get_success_url(self):
        return reverse('item', args=(self.kwargs['item_id']))
