from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
admin.site.index_title = "CafeUz"
admin.site.site_title = "CafeUz"
admin.site.site_header='CafeUz'
urlpatterns = [
    path('owner/', admin.site.urls),
    path('api/v1/',include('app.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)