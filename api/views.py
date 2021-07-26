from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import requires_csrf_token, csrf_exempt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import VotingOption
from rest_framework.decorators import api_view, permission_classes
from .serializers import VotingOptionSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

import socket

VISITAS = 0

@api_view(['GET'])
def index(request):
    return Response({'status': 'running'}, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes((AllowAny,))
@csrf_exempt
def vote_option(request, option_id):
    option = VotingOption.objects.get(id=option_id)
    option.voteFor()
    option.save()
    return Response(VotingOptionSerializer(option).data, status=status.HTTP_202_ACCEPTED)

@api_view(['PUT'])
@permission_classes((AllowAny,))
@csrf_exempt
def reset_option(request, option_id):
    option = VotingOption.objects.get(id=option_id)
    option.clearVotes()
    option.save()
    return Response(VotingOptionSerializer(option).data, status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
@permission_classes((AllowAny,))
@csrf_exempt
def get_option(request, option_id):
    return Response(VotingOptionSerializer(VotingOption.objects.get(id=option_id)).data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((AllowAny,))
@csrf_exempt
def get_all_options(request):
    return Response(VotingOptionSerializer(VotingOption.objects.all(), many=True).data, status=status.HTTP_200_OK)

