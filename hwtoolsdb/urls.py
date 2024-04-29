from django.urls import path
from . import views

urlpatterns = [
    path('tool/<int:id>/', views.add_or_edit_tool, name='edit-tool'),
    path('tool/new/', views.add_or_edit_tool, name='new-tool'),
    path('', views.tools_list, name='tools-list'),  # Assume you create a view to list tools
]
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tools/', include('hwtoolsdb.urls')),
]
