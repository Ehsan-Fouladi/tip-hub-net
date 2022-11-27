from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator
from videos.models import Video, Comment


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

    if request.method == "POST":
        parent_id = request.POST.get("parent_id")
        body = request.POST.get('body')
        Comment.objects.create(body=body, video=video, user=request.user, parent=parent_id)
    context = {'video': video}
    return render(request, 'home/video-detail.html', context)


