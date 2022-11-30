from django.db import models
from account.models import User
from django.shortcuts import reverse


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos', verbose_name='اسم', default=True)
    body = models.TextField(verbose_name='متن')
    slug = models.SlugField(unique=True, null=True, blank=True, allow_unicode=True, verbose_name="عنوان")
    about_video = models.TextField(verbose_name="درباره فیلم")
    video = models.FileField(upload_to="video/", verbose_name='ویدیو')
    image = models.ImageField(upload_to="image/", verbose_name='عکس')
    views = models.IntegerField(blank=True, default=0, verbose_name='بازدید')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان')
    time = models.TimeField(auto_now_add=True, verbose_name="ساعت")
    status = models.BooleanField(null=True, blank=True, verbose_name="وضیعت")

    class Meta:
        ordering = ["-user",]


    def __str__(self):
        return f'{self.time} - {self.status} - {self.views}'

    def get_absolute_url(self):
        return reverse("account:panel_user")

    class Meta:
        verbose_name = "ویدیو ها"
        verbose_name_plural = "ویدیو"



class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="parents")
    body = models.TextField()
    comment_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f"{self.user.username} - {self.body[:10]}"

    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes", verbose_name="لایک")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="likes", verbose_name="لایک کاربر")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user.username} - {self.video.slug}'


    class Meta:
        verbose_name = "لیک"
        verbose_name_plural = "لایک ها"
        ordering = ("created_at",)


class Notification(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="notification",verbose_name="نام کاربری", default=True)
    body = models.TextField(verbose_name="متن اعلان")
    time_created=models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ثبت")
    is_admin = models.BooleanField(default=True)
    active = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="notification",null=True,blank=True,verbose_name="فعال هست یا خیر", default=True)

    def get_absulot_url(self):
        return reverse("account:panel_user")

    def __str__(self):
        return f'{self.is_admin} - {self.active}'

    class Meta:
        ordering=("-active",)
        verbose_name = "اطلاع رسانی"
        verbose_name_plural = "اطلاع رسانی ها"

