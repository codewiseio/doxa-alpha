from rest_framework import permissions,status,generics,viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404

from contacts.models import Contact
from contacts.managers import ContactManager
from contacts.serializers import ContactSerializer
from people.models import Person
from people.serializers import PersonSerializer
from members.models import Member
from members.serializers import MemberSerializer

from django.db import transaction
from doxa.exceptions import HttpException, StorageException

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.order_by('id')
    serializer_class = MemberSerializer


    
class MembersItemView(generics.RetrieveUpdateAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects

    def retrieve(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(self.object)
        
        member = serializer.data
        member['entity'] = self.get_entity(member['entity'])
        member['contacts'] = ContactManager.get_primary_contacts(member['entity'])

        return Response(member)

    def get_entity(self, moniker):
        print('Getting entity')
        print (moniker)

        mold, id = moniker.split(':')


        print(mold)
        print(id)

        if mold == 'person':
            entity = Person.objects.get(id=id)
            serializer = PersonSerializer(entity)
            return serializer.data
        else:
            raise Http404("Poll does not exist")




class MembersListView(generics.ListAPIView):    
    serializer_class = MemberSerializer
    lookup_url_kwarg = "owner"
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        owner = self.kwargs.get('owner')
        members = Member.objects.filter(owner=owner)
        return members

    def list(self, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = MemberSerializer(queryset, many=True)
        
        members = serializer.data
        members = self.get_entity_data(members)

        return Response(members, status=status.HTTP_201_CREATED)

    def get_entity_data(self, members):

        monikers = []
        for member in members:
            entity_moniker = member.get('entity')
            entity_id = entity_moniker.split(':')[1];
            
            person = Person.objects.get(id=entity_id)
            serializer = PersonSerializer(person)
            member['entity'] = serializer.data

        return members

class MembersCreateView(generics.CreateAPIView):

    @transaction.atomic
    def create(self, request):
        """ Handle post data to create a member."""
        
        data = request.data
        print(data)
        
        try:
            with transaction.atomic():
                person = self._create_person(data['entity'])

                owner = 'organization:{}'.format(data['owner']['id'])
                entity = 'person:{}'.format(person.id)

                # create member object
                data['member']['owner'] = owner
                data['member']['entity'] = entity
                member = self._create_member(data['member'])

                # create contacts
                contacts = self._save_contacts(entity, data['contacts'])

        except HttpException as e:
            return Response(e.response, e.status)
        
        # except Exception as e:
        #     print(e)
        #     return Response({
        #             'status': 'Unknown Error',
        #             'message': 'Oops. Something bad happened.. {}'.format(e.args[0]),
        #             'details': e.args[0]
        #         }, status=status.HTTP_400_BAD_REQUEST)
        
        # if we have reached this point everything completed successfully
        return Response({'status':'Created'}, status=status.HTTP_201_CREATED)
        


    def _create_person(self, data):
        """ Create a person object from given form data """
        # validate supplied user data
        serializer = PersonSerializer( data=data )
        if serializer.is_valid():
            # create record
            person = Person.objects.create(**serializer.validated_data)
            
        else:
            # data not valid, return bad request response
            raise HttpException({
                'status': 'Bad request',
                'message': 'Record could not be created with received data.',
                'details': 'Could not create person record.'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        return person


    def _create_member(self, data):
        """ Create a person object from given form data """
        # validate supplied user data
        print( data )

        serializer = MemberSerializer( data=data )
        if serializer.is_valid():
            # create record
            person = Member.objects.create(**serializer.validated_data)
            
        else:
            # data not valid, return bad request response
            raise HttpException({
                'status': 'Bad request',
                'message': 'Record could not be created with received data.',
                'details': 'Could not create member record.'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        return person

    def _save_contacts(self, entity, data):
        serialized_data = []
        errors = []
        
        # iterate over items in array
        try:
            for item in data:
                if not item.get('id'):
                    item['owner'] = entity
                serialized_data.append( ContactManager.save( item ) )
        except StorageException as err:
                errors.merge( err.args[1] )

                
        if ( len(errors) > 0 ):
            raise StorageException( 'Could not update contact information', errors );
        else:
            return serialized_data;
