from django.urls import path
from home.views import image_list, image_detail, image_delete   #ImageList
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', image_list, name="image_list"),
    path('view/<int:id>', image_detail, name="image_detail"),
    path('delete/<int:id>', image_delete, name="image_delete")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
