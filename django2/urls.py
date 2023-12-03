from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django2 import settings
from products.views import IndexPageView, IndexDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPageView.as_view(), name='index'),
    path('index/<int:pk>/', IndexDetailView.as_view(), name='index-detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('login', views.CustomLoginView.as_view()),
    # path('logout', views.LogoutView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
