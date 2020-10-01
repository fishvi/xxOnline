from django.db import models
from DjangoUeditor.models import UEditorField

from apps.users.models import BaseModel
from apps.organizations.models import Teacher, CourseOrg


class Course(BaseModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='讲师')
    course_org = models.ForeignKey(CourseOrg, null=True, blank=True, on_delete=models.CASCADE, verbose_name='课程机构')
    name = models.CharField(max_length=50, verbose_name='课程名')
    desc = models.CharField(max_length=300, verbose_name='课程描述')
    learn_time = models.IntegerField(default=0, verbose_name='学习时长(分钟数)')
    degree = models.CharField(choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级')), max_length=2, verbose_name='难度')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    notice = models.CharField(default='', max_length=300, verbose_name='课程公告')
    category = models.CharField(default='', max_length=20, verbose_name='课程类别')
    advice = models.CharField(default='', max_length=300, verbose_name='课程须知')
    teacher_tell = models.CharField(default='', max_length=300, verbose_name='老师告诉你')
    detail = UEditorField(width=600, height=300, imagePath='courses/ueditor/images/',
                          filePath='courses/ueditor/files/', default='', verbose_name='课程详情')
    image = models.ImageField(upload_to='courses/%Y/%m', max_length=100, verbose_name='封面图')
    is_classic = models.BooleanField(default=False, verbose_name='是否经典')
    is_banner = models.BooleanField(default=False, verbose_name='是否广告位')

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def lesson_nums(self):
        return self.lesson_set.all().count()


class BannerCourse(Course):
    class Meta:
        verbose_name = '广告位'
        verbose_name_plural = verbose_name
        proxy = True


class CourseTag(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    tag = models.CharField(max_length=10, verbose_name='课程标签')

    class Meta:
        verbose_name = '课程标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='章节名')
    learn_time = models.IntegerField(default=0, verbose_name='学习时长(分钟数)')

    class Meta:
        verbose_name = '章节信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='章节')
    name = models.CharField(max_length=100, verbose_name='视频名')
    learn_time = models.IntegerField(default=0, verbose_name='学习时长(分钟数)')
    url = models.CharField(max_length=1000, verbose_name='访问地址')

    class Meta:
        verbose_name = '课程视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='名称')
    file = models.FileField(upload_to='course/resource/%Y/%m', max_length=200, verbose_name='下载地址')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
