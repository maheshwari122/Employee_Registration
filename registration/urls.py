from django.urls import *
from rest_framework.routers import DefaultRouter
from .views import * 

router = DefaultRouter()
router.register("employee", EmployeeRegistrationFormViewSet)

urlpatterns = [
    # *router.urls,
    path('', include(router.urls)),
    path('registration_form',Registration, name='submit_reg'),
    path('export_excel/<int:id>/', ExportEmployeeExcel, name='export_excel'),
]
