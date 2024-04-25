from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from ml_compare.core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('uploads/form/', views.model_form_upload, name='model_form_upload'),
    path('compare', views.compare_docs, name='compare_docs'),
    path('list/', views.list, name='list'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
