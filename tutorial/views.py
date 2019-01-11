from django.shortcuts import render,redirect
from django_tables2 import RequestConfig
from .models import Ticket
from .tables import TicketTable

def tickets(request):
    table = TicketTable(Ticket.objects.all())
    RequestConfig(request).configure(table)
    return render(request, '../templates/tickets.html', {'table': table})