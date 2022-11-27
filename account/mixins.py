from django.http import Http404
from videos.models import Video
from django.shortcuts import get_object_or_404

class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin:
            self.fields = "__all__"
        elif request.user:
            self.fields = ['body', 'slug', 'about_video', 'video', 'image']
        else:
            raise Http404
        return super(FieldsMixin, self).dispatch(request, *args, **kwargs)


class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_admin:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.user = self.request.user
            self.obj.status = None
        return super().form_valid(form)


class UpdateMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        videos = get_object_or_404(Video, pk=pk)
        if videos.user == request.user or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404
        
