from django.urls import path
from . import views

app_name = 'clientes_app'

urlpatterns = [
    path('', views.index, name='index'),
    
    # URLs para Cliente
    path('clientes/', views.ClienteListView.as_view(), name='cliente-list'),
    path('clientes/nuevo/', views.ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/<uuid:pk>/', views.ClienteDetailView.as_view(), name='cliente-detail'),
    path('clientes/<uuid:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/<uuid:pk>/eliminar/', views.ClienteDeleteView.as_view(), name='cliente-delete'),
    
    # URLs para Cliente Corporativo
    path('clientes-corporativos/', views.ClienteCorporativoListView.as_view(), name='cliente-corporativo-list'),
    path('clientes-corporativos/nuevo/', views.ClienteCorporativoCreateView.as_view(), name='cliente-corporativo-create'),
    path('clientes-corporativos/<uuid:pk>/', views.ClienteCorporativoDetailView.as_view(), name='cliente-corporativo-detail'),
    path('clientes-corporativos/<uuid:pk>/editar/', views.ClienteCorporativoUpdateView.as_view(), name='cliente-corporativo-update'),
    path('clientes-corporativos/<uuid:pk>/eliminar/', views.ClienteCorporativoDeleteView.as_view(), name='cliente-corporativo-delete'),
    
    # URLs para Producto
    path('productos/', views.ProductoListView.as_view(), name='producto-list'),
    path('productos/nuevo/', views.ProductoCreateView.as_view(), name='producto-create'),
    path('productos/<str:codigo_sku>/', views.ProductoDetailView.as_view(), name='producto-detail'),
    path('productos/<str:codigo_sku>/editar/', views.ProductoUpdateView.as_view(), name='producto-update'),
    path('productos/<str:codigo_sku>/eliminar/', views.ProductoDeleteView.as_view(), name='producto-delete'),
    
    # URL para búsqueda
    path('buscar/', views.buscar_producto, name='buscar-producto'),
]