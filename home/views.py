from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.core.paginator import Paginator
from videos.models import Video, Comment, Like
from django.http import JsonResponse

class Home(ListView):
    model = Video
    ordering = ['-user',]
    paginate_by = 6
    template_name = "home/home.html"


def VideoList(request):
    videos = Video.objects.all()
    page_number = request.GET.get("page")
    paginate = Paginator(videos, 6)
    object = paginate.get_page(page_number)
    context = {'object_list': object}
    return render(request, "home/video-list.html", context)


def Search(request):
    q = request.GET.get("q")
    videos = Video.objects.filter(slug__icontains=q)
    page_number = request.GET.get("page")
    paginate = Paginator(videos, 2)
    object = paginate.get_page(page_number)
    context = {'object_list': object}
    return render(request, "home/video-list.html", context)


def VideoDetail(request, pk, slug):
    video = get_object_or_404(Video, id=pk, slug=slug)
    # view
    object_list = Video.objects.get(id=pk)
    object_list.views = object_list.views + 1
    object_list.save()

    if request.method == "POST":
        parent_id = request.POST.get("parent_id")
        body = request.POST.get('body')
        Comment.objects.create(body=body, video=video, user=request.user, parent=parent_id)

    context = {'video': video}
    
    if request.user.is_authenticated:
        if request.user.likes.filter(video_id=pk, user_id=request.user.id).exists():
            context['is_liked'] = True
        else:
            context['is_liked'] = False
    else:
        return redirect('home:detail')

    return render(request, 'home/video-detail.html', context)


def likeDetail(request, slug, pk):
    try:
        like = Like.objects.get(video__slug=slug, user_id=request.user.id)
        like.delete()
        return JsonResponse({"response":"unliked"})
    except:
        Like.objects.create(video_id=pk, user_id=request.user.id)
    return JsonResponse({"response":"liked"})