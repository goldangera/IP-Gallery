from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.gen_pics,name='generalPics'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^gen_pics/',views.gen_pics,name ='genaralPics')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)