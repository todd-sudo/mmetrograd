from django.urls import path

from .views import (
    TenantTaskListView,
    TenantTaskDetailView,
    TenantTaskCreateView,
    TenantTaskDestroyView,
)


urlpatterns = [
    path(
        "tenant/<str:username>/tasks",
        TenantTaskListView.as_view(),
        name="tenant"
    ),
    path(
        "tenant/<str:username>/",
        TenantTaskDetailView.as_view(),
        name="task"
    ),
    path("tenant/<str:username>/create-task/", TenantTaskCreateView.as_view(), name="task_create"),
    path("tenant/<str:username>/delete-task/", TenantTaskDestroyView.as_view(), name="task_delete"),

]
