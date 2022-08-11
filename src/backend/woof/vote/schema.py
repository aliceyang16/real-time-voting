from email.policy import default
from xmlrpc.client import DateTime
import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation
from django.shortcuts import render
from rest_framework import generics
from .forms import BallotsForm

from .models import Ballots

# Create your views here.
class BallotsType(DjangoObjectType):
    class Meta:
        fields = ["id", "dog_vote", "cat_vote", "voted_at"]


class Query(graphene.ObjectType):
    all_ballots = DjangoFilterConnectionField(BallotsType)

    def resolve_all_ballots(root, info, **kwargs):
        return Ballots.objects.all()


class BallotsMutation(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        dog_vote = graphene.Boolean(default=False)
        cat_vote = graphene.Boolean(default=False)

    def mutate(cls, root, info, **input):
        Ballots.objects.create(dog_vote=dog_vote, cat_vote=cat_vote)
        return cls(ok=True)


class Mutation(graphene.ObjectType):
    insert_ballots = BallotsMutation.Field()
