from rest_framework import serializers

from authentication.serializers import UserSerializer
from organizations.models import Organization,OrganizationMember
from people.serializers import PersonSerializer

class OrganizationSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Organization

        fields = ('id','name','description','size','owner','email','telephone','address','municipality','region','postcode','country')
        read_only_fields = ['id']

class OrganizationMemberSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    person = PersonSerializer()
    added_by = PersonSerializer()

    class Meta:
        model = OrganizationMember

        fields = ('id','organization','person','role','involvement','join_date','added_by')
        read_only_fields = ['id']
