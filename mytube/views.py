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
            return JsonResponse(serializer.data, status=200)
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
            return JsonResponse(status=400)


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
            return JsonResponse(status=400)


@csrf_exempt
def comment_upload(request):
    if request.method == 'POST':
        token = request.POST["token"]
        comment_text = request.POST["comment"]
        videoid = request.POST["videoid"]
        data = {'token': token, 'comment': comment_text, 'videoid': videoid}
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'token': token, 'comment': comment_text, 'videoid': videoid},
                                status=200)
        else:
            return JsonResponse(status=400)


@csrf_exempt
def comment_view_all(request):
    if request.method == 'GET':
        query_set = Comment.objects.all()
        serializer = CommentSerializer(query_set, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def comment_view(request, videoid):
    if request.method == 'GET':
        # url1 = 'https://image-mellow.s3.amazonaws.com/media/Youtube/1812_overture_-_usarmy_band.mp4'
        # url2 = 'https://image-mellow.s3.amazonaws.com/media/Youtube/dance_dont_delay_-_twin_musicom.mp4'
        query_set = Comment.objects.all().filter(videoid=videoid)
        serializer = CommentSerializer(query_set, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)


# @csrf_exempt
# def comment_view(request):
#     if request.method == 'GET':
#
#     if request.method == 'POST':
#         url = request.POST["url"]
#         query_set = Comment.objects.filter(url=url)
#         serializer = CommentSerializer(query_set, many=True)
#         return JsonResponse(serializer.data, safe=False)

# @csrf_exempt
# def comment_view_all(request):
#     if request.method == 'GET':
#         url1 = 'https://image-mellow.s3.amazonaws.com/media/Youtube/1812_overture_-_usarmy_band.mp4'
#         url2 = 'https://image-mellow.s3.amazonaws.com/media/Youtube/dance_dont_delay_-_twin_musicom.mp4'
#         query_set = Comment.objects.filter(url=url1)
#         serializer = CommentSerializer(query_set, many=True)
#         return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def comment_delete(request):
    if request.method == 'POST':
        token = request.POST["token"]
        videoid = request.POST["videoid"]
        commentid = request.POST["commentid"]

        obj = Comment.objects.get(commentid=commentid, token=token)
        if obj is not None and (token == obj.token):
            obj.delete()
            return JsonResponse({'responseok': token}, status=200)

        else:
            return JsonResponse(status=400)
