from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classifieds import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('classifieds/<int:id>/', views.classified_detail, name='classified_detail'),
    path('add-classified/', views.classified_add, name='classified_add'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
