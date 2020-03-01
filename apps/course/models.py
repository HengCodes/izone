from django.conf import settings
from django.db import models
from mdeditor.fields import MDTextField
from django.shortcuts import reverse
import markdown
# Create your models here.


# 教程类目
class CourseTopic(models.Model):
    IMG_LINK = '/static/blog/img/summary.png'
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=150, verbose_name='教程类别')
    title = models.CharField(max_length=150, verbose_name='教程标题')
    summary = models.TextField('教程摘要', max_length=230, default='教程摘要等同于网页description内容，请务必填写...')
    img_link = models.CharField('图片地址', default=IMG_LINK, max_length=255)

    class Meta:
        verbose_name = '教程主题'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course:topic', kwargs={'slug': self.slug})

    def get_course_list(self):
        '''返回当前标签下所有发表的文章列表'''
        return CourseClauses.objects.filter(tags=self)


class CourseClauses(models.Model):
    IMG_LINK = '/static/blog/img/summary.png'
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.PROTECT)
    title = models.CharField(max_length=150, verbose_name='教程标题')
    summary = models.TextField('教程摘要', max_length=230, default='教程摘要等同于网页description内容，请务必填写...')
    body = MDTextField(verbose_name='文章内容')
    img_link = models.CharField('图片地址', default=IMG_LINK, max_length=255)
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    views = models.IntegerField('阅览量', default=0)
    slug = models.SlugField(unique=True)
    is_top = models.BooleanField('置顶', default=False)

    category = models.ForeignKey(CourseTopic, verbose_name='教程分类', on_delete=models.PROTECT)


    class Meta:
        verbose_name = '教程'
        verbose_name_plural = verbose_name
        ordering = ['-create_date']

    def __str__(self):
        return self.title[:20]

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def body_to_markdown(self):
        return markdown.markdown(self.body, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

    def update_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_pre(self):
        return CourseClauses.objects.filter(id__lt=self.id).order_by('-id').first()

    def get_next(self):
        return CourseClauses.objects.filter(id__gt=self.id).order_by('id').first()