from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from .models import Artist
from .serializers import ArtistSerializer, ArtistListSerializer, ArtistUpdateSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def artist_list_or_create(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def artist_detail(request, artist_pk):
    artist = Artist.objects.get(pk=artist_pk)
    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ArtistUpdateSerializer(artist, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        artist.delete()
        data = {
            'delete': f'등록 번호 {artist_pk} 번의 {artist.name}을 삭제하였습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def artist_condition_list(request):
    # request.query_params : URL에서 쿼리 매개변수를 담고 있는 객체 (딕셔너리 형태로 저장)
    query_param = request.query_params.get('is_group', False)
    # query_param가 있다면 다음 조건으로 이동
    if query_param:
        if query_param == 'True' or query_param == 'true':
            artists = Artist.objects.filter(is_group=True)
        else:
            artists = Artist.objects.filter(is_group=False)
    # query_param가 없다면 모든 데이터 전송
    else:
        artists = Artist.objects.all()
    
    serializer = ArtistSerializer(artists, many=True)


    return Response(serializer.data, status=status.HTTP_200_OK)