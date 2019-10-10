from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from userinfo.models import UserInfo, MicroLoan
from userinfo.serializers import UserInfoSerializer, MicroLoanSerializer


@api_view(['GET', 'POST'])
def userinfo_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        userinfo = UserInfo.objects.all()
        serializer = UserInfoSerializer(userinfo, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def userinfo_detail(request, pk):
    """
    Retrieve, update or delete a code UserInfo.
    """
    try:
        userinfo = UserInfo.objects.get(pk=pk)
    except UserInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserInfoSerializer(userinfo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserInfoSerializer(userinfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        userinfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def microloan_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        microloan = MicroLoan.objects.all()
        serializer = MicroLoanSerializer(microloan, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MicroLoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def microloan_detail(request, pk):
    """
    Retrieve, update or delete a code MicroLoan.
    """
    try:
        microloan = MicroLoan.objects.get(pk=pk)
    except MicroLoan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MicroLoanSerializer(microloan)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MicroLoanSerializer(microloan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        microloan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
