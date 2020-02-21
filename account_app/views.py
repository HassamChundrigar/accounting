from django.shortcuts import render
from rest_framework import viewsets
from .models import Entry, SubEntry, SubHeadAccount, SubHead, Head
from .serializers import EntrySerializer, EntryListSerializer, SubEntrySerializer, SubEntryListSerializer, SubHeadAccountSerializer, SubHeadSerializer, SubHeadAccountListSerializer
from rest_framework import generics

from django.http import JsonResponse
# Create your views here.


class SubHeadViewSet(viewsets.ModelViewSet):
    queryset = SubHead.objects.all()
    serializer_class = SubHeadSerializer


class SubHeadAccountViewSet(viewsets.ModelViewSet):
    queryset = SubHeadAccount.objects.all()
    serializer_class = SubHeadAccountSerializer


class SubEntryViewSet(viewsets.ModelViewSet):
    queryset = SubEntry.objects.all()
    serializer_class = SubEntrySerializer


class SubEntryListViewSet(viewsets.ModelViewSet):
    queryset = SubEntry.objects.all()
    serializer_class = SubEntryListSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryListViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntryListSerializer


class SubHeadList(generics.ListAPIView):
    serializer_class = SubHeadSerializer

    def get_queryset(self):
        queryset = SubHead.objects.all()
        head = self.request.query_params.get('head', None)
        if head is not None:
            queryset = queryset.filter(head=head)
        return queryset


class SubHeadAccountList(generics.ListAPIView):
    serializer_class = SubHeadAccountSerializer

    def get_queryset(self):
        queryset = SubHeadAccount.objects.all()
        sub_head = self.request.query_params.get('sub_head', None)
        if sub_head is not None:
            queryset = queryset.filter(sub_head=sub_head)
        return queryset


def index(request):
    return render(request, 'entries/entries.html')


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

