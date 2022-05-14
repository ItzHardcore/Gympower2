from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.inicio, name="home"),
    path('login/', views.loginPage, name="login"),
    path('registar/', views.registerPage, name="registar"),
    path('logout/', views.logoutUtilizador, name="logout"),

#Cliente
    path('landpage/', views.clienteInicial, name="cliente_home"),
    path('cliente_treino/', views.cliente_treino, name="cliente_treino"),
    path('cliente_dieta/', views.cliente_dieta, name="cliente_dieta"),
    path('cliente_pt/', views.cliente_pt, name="cliente_pt"),
    path('cliente_aulas/', views.cliente_aulas, name="cliente_aulas"),
    path('cliente_perfil/', views.cliente_perfil, name="cliente_perfil"),
    path('cliente_perfil_update/', views.cliente_perfil_update, name="cliente_perfil_update"),

#Admin
    path('admin/', views.adminInicial, name="admin_home"),
    path('admin_procurarcliente/', views.admin_procurarcliente, name="admin_procurarcliente"),
    path('admin_aulas/', views.admin_aulas, name="admin_aulas"),
    path('admin_pt/', views.admin_pt, name="admin_pt"),

#PT
    path('pt/', views.ptInicial, name="pt_home"),
    path('pt_perfil/', views.pt_perfil, name="pt_perfil"),
    path('pt_perfil_update/', views.pt_perfil_update, name="pt_perfil_update"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()