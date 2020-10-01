from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from apps.courses.models import Course, CourseTag, CourseResource, Video
from apps.operations.models import UserFavorite, UserCourses, CourseComments


class CourseListView(View):
    def get(self, request, *args, **kwargs):
        all_courses = Course.objects.order_by('-add_time')
        hot_courses = Course.objects.order_by('-click_nums')[:3]

        # 搜索
        keywords = request.GET.get('keywords', '')
        s_type = 'course'
        if keywords:
            all_courses = all_courses.filter(
                Q(name__icontains=keywords) | Q(desc__icontains=keywords) | Q(detail__icontains=keywords)
            )

        # 排序
        sort = request.GET.get('sort', '')
        if sort == 'students':
            all_courses = all_courses.order_by('-students')
        if sort == 'hot':
            all_courses = all_courses.order_by('-click_nums')

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, per_page=9, request=request)
        courses = p.page(page)
        return render(request, 'course-list.html', {
            'all_courses': courses,
            'sort': sort,
            'hot_courses': hot_courses,
            'keywords': keywords,
            's_type': s_type
        })


class CourseDetailView(View):
    def get(self, request, course_id, *args, **kwargs):
        course = Course.objects.get(id=int(course_id))
        course.click_nums += 1
        course.save()

        # 收藏
        has_fav_course = False
        has_fav_org = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True

        # 推荐
        tags = course.coursetag_set.all()
        tag_list = [tag.tag for tag in tags]
        course_tags = CourseTag.objects.filter(tag__in=tag_list).exclude(course__id=course.id)
        related_courses = set()
        for course_tag in course_tags:
            related_courses.add(course_tag.course)
        return render(request, 'course-detail.html', {
            'course': course,
            'has_fav_course': has_fav_course,
            'has_fav_org': has_fav_org,
            'related_courses': related_courses
        })


class CourseLessonView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, course_id, *args, **kwargs):
        course = Course.objects.get(id=int(course_id))
        course.click_nums += 1
        course.save()
        user_courses = UserCourses.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_course = UserCourses(user=request.user, course=course)
            user_course.save()
            course.students += 1
            course.save()

        # 该课的同学还学过
        user_courses = UserCourses.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        course_resources = CourseResource.objects.filter(course=course)
        all_courses = UserCourses.objects.filter(user_id__in=user_ids).order_by('-course__click_nums')[:5]
        related_courses = []
        for item in all_courses:
            if item.course.id != course.id:
                related_courses.append(item.course)
        return render(request, 'course-video.html', {
            'course': course,
            'course_resources': course_resources,
            'related_courses': related_courses
        })


class CourseCommentsView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, course_id, *args, **kwargs):
        course = Course.objects.get(id=int(course_id))
        course.click_nums += 1
        course.save()
        comments = CourseComments.objects.filter(course=course)
        user_courses = UserCourses.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        course_resources = CourseResource.objects.filter(course=course)
        all_courses = UserCourses.objects.filter(user_id__in=user_ids).order_by('-course__click_nums')[:5]
        related_courses = []
        for item in all_courses:
            if item.course.id != course.id:
                related_courses.append(item.course)
        return render(request, 'course-comment.html', {
            'course': course,
            'course_resources': course_resources,
            'related_courses': related_courses,
            'comments': comments
        })


class VideoView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, course_id, video_id, *args, **kwargs):
        course = Course.objects.get(id=int(course_id))
        course.click_nums += 1
        course.save()
        video = Video.objects.get(id=int(video_id))
        user_courses = UserCourses.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_course = UserCourses(user=request.user, course=course)
            user_course.save()
            course.students += 1
            course.save()

        # 该课的同学还学过
        user_courses = UserCourses.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        course_resources = CourseResource.objects.filter(course=course)
        all_courses = UserCourses.objects.filter(user_id__in=user_ids).order_by('-course__click_nums')[:5]
        related_courses = []
        for item in all_courses:
            if item.course.id != course.id:
                related_courses.append(item.course)
        return render(request, 'course-play.html', {
            'course': course,
            'course_resources': course_resources,
            'related_courses': related_courses,
            'video': video
        })
