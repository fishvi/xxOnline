import xadmin
from apps.courses.models import Course, BannerCourse, CourseTag, Lesson, Video, CourseResource


class GlobalSettings(object):
    site_title = 'xxOnline后台管理系统'
    site_footer = '在线教育网'
    # menu_style = 'accordion'


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class CourseAdmin(object):
    list_display = ['name', 'desc', 'degree', 'learn_time', 'students']
    search_fields = ['name', 'desc', 'degree', 'students']
    list_filter = ['name', 'teacher__name', 'desc', 'degree', 'learn_time', 'students']
    list_editable = ['desc', 'degree']
    readonly_fields = ['click_nums', 'fav_nums', 'students', 'add_time']
    # exclude = []  # 隐藏字段
    # ordering = []  # 列表排序
    model_icon = 'fa fa-book'
    style_fields = {
        'detail': 'ueditor'
    }

    def queryset(self):
        qs = super().queryset()
        if not self.request.user.is_superuser:
            qs = qs.filter(teacher=self.request.user.teacher)
        return qs


class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'learn_time', 'students']
    search_fields = ['name', 'desc', 'degree', 'students']
    model_icon = 'fa fa-play-circle-o'

    def queryset(self):
        qs = super().queryset().filter(is_banner=True)
        return qs


class CourseTagAdmin(object):
    list_display = ['course', 'tag', 'add_time']
    search_fields = ['course', 'tag']
    list_filter = ['course', 'tag', 'add_time']
    model_icon = 'fa fa-tags'


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']
    model_icon = 'fa fa-list-ul'


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']
    model_icon = 'fa fa-video-camera'


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'file', 'add_time']
    search_fields = ['course', 'name', 'file']
    list_filter = ['course', 'name', 'file', 'add_time']
    model_icon = 'fa fa-file'


xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(CourseTag, CourseTagAdmin)
