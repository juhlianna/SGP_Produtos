
from django.contrib import admin
from django.urls import path, include

# URL caminho padrão para acesso
urlpatterns = [
    #path('grappelli/', include('grappelli.urls')),

    path('admin/', admin.site.urls),
]
