from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,
										 PermissionRequiredMixin)
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView
from groups.models import Group, GroupMember

# Create your views here.
class CreateGroup(LoginRequiredMixin, CreateView):
	fields = ('name', 'description')
	model = Group


class SingleGroup(DeleteView):
	model = Group


class ListGroups(ListView):
	model = Group