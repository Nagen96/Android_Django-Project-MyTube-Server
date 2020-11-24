from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import User, Video, Comment
from .serializers import VideoSerializer, CommentSerializer


# Create your views here.
@csrf_exempt
def upload_video(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VideoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def stream_video(request):
    if request.method == 'GET':
        query_set = Video.objects.all()
        serializer = VideoSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def login(request):
    if request.method == "POST":
        user_id = request.POST.get('userid', '')
        user_pw = request.POST.get('userpw', '')
        user = authenticate(username=user_id, password=user_pw)

        if user is not None:
            print("인증성공")
            return JsonResponse({'code': '0000', 'token': user_id},
                                status=200)
        else:
            print("인증실패")
            return JsonResponse(status=401)


@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        user_id = request.POST["userid"]
        user_pw = request.POST["userpw"]
        user_pc = request.POST["userpc"]
        email = "none"

        if user_pw == user_pc:
            user = User.objects.create_user(user_id, email, user_pw)
            user.save()
            return JsonResponse({'code': '0000', 'token': user_id},
                                status=200)

        else:
            return JsonResponse(status=401)


@csrf_exempt
def comment_upload(request):
    if request.method == 'POST':
        token = request.POST["token"]
        comment_text = request.POST["comment"]
        url = request.POST["url"]
        data = {'token': token, 'comment': comment_text, 'url': url}
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'token': token, 'comment': comment_text, 'url': url},
                                status=200)
        else:
            return JsonResponse(status=401)


@csrf_exempt
def comment_view(request):
    if request.method == 'GET':
        query_set = Comment.objects.all()
        serializer = CommentSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)


# @csrf_exempt
# def comment_view(request):
#     if request.method == 'GET':
#         url = request.POST["https://image-mellow.s3.amazonaws.com/media/Youtube/1812_overture_-_usarmy_band.mp4"]
#         query_set = Comment.objects.filter(url=url)
#         serializer = CommentSerializer(query_set, many=True)
#         return JsonResponse(serializer.data, safe=False)
