
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from myapp.views import Basetabledata,Propertiesdata,Imagesdata,Dimensionsdata,Productdata
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('openapi', get_schema_view(
        title="RESTAPI Project",
        description="API for all things",
        version="1.0.0"),
         name='api-schema'),
]

router = routers.SimpleRouter()
router.register('Base',Basetabledata)
router.register('Prop',Propertiesdata)
router.register('Dimension',Dimensionsdata)
router.register('Image',Imagesdata)
router.register('Prod',Productdata)

urlpatterns += router.urls