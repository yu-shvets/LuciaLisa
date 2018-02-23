"""LuciaLisa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from products.views import HomeView, CategoryFilterView, ItemDetailView, update_size, FeedbackCreateView
from cart.views import add_cart, cart_view, cart_remove
from company.views import EmailCreateView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^catalogue/$', CategoryFilterView.as_view(), name='catalogue'),
    url(r'^catalogue/items/(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item'),
    url(r'^update/(?P<item_id>\d+)/$', update_size, name='update_size'),
    url(r'^feedback_create/(?P<item_id>\d+)/$', FeedbackCreateView.as_view(), name='feedback'),

    url(r'^add_cart/$', add_cart, name='add'),
    url(r'^cart/$', cart_view, name='cart'),
    url(r'^remove/(?P<specs_id>\d+)/$', cart_remove, name='remove'),

    url(r'^email_create/$', EmailCreateView.as_view(), name='email'),

    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
