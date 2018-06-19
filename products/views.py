from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, ListView
from django_filters import FilterSet, ModelMultipleChoiceFilter, OrderingFilter
from django import forms
from django_filters.views import FilterView
from .models import Category, Item, Specs
from .forms import SizesForm, FeedbackForm
from django.http import JsonResponse
from django.urls import reverse
from company.forms import EmailForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.dateformat import DateFormat
from django.db.models import Q
from django.contrib import messages
from company.models import News


class HomeView(ListView):
    template_name = 'index.html'
    model = Item
    queryset = Item.objects.filter(sales__isnull=False)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = EmailForm
        context['categories'] = Category.objects.all()
        context['news'] = News.objects.all()
        return context

    def get_queryset(self):
        if self.kwargs.get('category_id'):
            return self.queryset.filter(category=self.kwargs['category_id'])
        return self.queryset


class CategoryFilter(FilterSet):

    category = ModelMultipleChoiceFilter(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Item
        fields = ['category']

    ordering = OrderingFilter(
        fields=(('specs__price', 'price'),)
    )


class CategoryFilterView(FilterView):
    template_name = 'products/catalogue.html'
    filterset_class = CategoryFilter
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(CategoryFilterView, self).get_context_data(**kwargs)
        context['paginate_by'] = int(self.request.GET.get('paginate_by', self.paginate_by))
        return context

    def get_paginate_by(self, queryset):
        print('')
        print(queryset)
        return int(self.request.GET.get('paginate_by', self.paginate_by))


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


def search(request):
    query = request.GET.get('query').strip()
    if query:
        items = Item.objects.filter(Q(title__icontains=query) |
                                    Q(category__title__icontains=query))
        return render(request, 'products/search_result.html', {'object_list': items, 'query': query})
    messages.error(request, "Please, enter a search string.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
