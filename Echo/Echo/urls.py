

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.views.decorators.csrf import csrf_exempt
from Echo.schema import schema,customer_schema,product_schema,supplier_schema
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productupdate/', include('Product.urls')),
    path("echo/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path("product/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=product_schema))),
    path("customer/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=customer_schema))),
    path("supplier/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=supplier_schema))),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)