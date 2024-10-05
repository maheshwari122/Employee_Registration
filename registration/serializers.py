from rest_framework import serializers
from registration.models import EmployeeRegistrationForm


class EmployeeRegistrationFormSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRegistrationForm
        fields = '__all__'

