from django.db.models import F, Sum, Window
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.decorators import permission_classes
from mainApp.models import Transaction, Sections
from mainApp.Serializers import TransactionSerializer, SectionSerializer
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models.functions import RowNumber


# authentication_classes = [SessionAuthentication, BasicAuthentication]
# permission_classes = [IsAuthenticated]


@api_view(['GET', 'POST'])
# @authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def transactions(request):
    if request.method == 'GET':
        result = (Transaction.objects.all().values('actionId', 'team_id', 'withdrawAmount').annotate(id=Window(
            expression=RowNumber())))
        serializer = TransactionSerializer(result, many=True)
        return Response(serializer.data)
    else:
        serializer = TransactionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def transactions_details(req, team_id):
    try:
        trans = (Transaction.objects.filter(team_id=team_id).values('actionId', 'team_id', 'withdrawAmount').annotate(
            id=Window(expression=RowNumber())))
    except Transaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if req.method == 'GET':
        serializer = TransactionSerializer(trans, many=True)
        return Response(serializer.data)


@api_view(['GET'])
# @authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def team_ranking(req):
    try:
        result = (Transaction.objects
            .values('team_id')
            .annotate(
            withdrawAmount=Sum('withdrawAmount'))

            .order_by('-withdrawAmount').
            annotate(id=Window(
            expression=RowNumber(),

            order_by=F('withdrawAmount').desc(),
        ), )
        )
    except Transaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if req.method == 'GET':
        serializer = TransactionSerializer(result, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def sections_details(req, sections_id):
    try:
        result = Sections.objects.filter(section_id=sections_id)

    except Sections.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if req.method == 'GET':
        serializer = SectionSerializer(result, many=True)
        return Response(serializer.data)
