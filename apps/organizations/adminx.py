import xadmin
from apps.organizations.models import Teacher, CourseOrg, City


class TeacherAdmin(object):
    list_display = ['name', 'org', 'work_years', 'work_company']
    search_fields = ['name', 'org', 'work_years', 'work_company']
    list_filter = ['name', 'org', 'work_years', 'work_company']
    model_icon = 'fa fa-graduation-cap'


class CourseOrgAdmin(object):
    list_display = ['name', 'tag', 'category', 'city', 'click_nums', 'fav_nums']
    search_fields = ['name', 'tag', 'category', 'city', 'click_nums', 'fav_nums']
    list_filter = ['name', 'click_nums', 'fav_nums']
    readonly_fields = ['click_nums', 'fav_nums', 'students', 'add_time']
    model_icon = 'fa fa-handshake-o'
    style_fields = {
        'desc': 'ueditor'
    }


class CityAdmin(object):
    list_display = ['name', 'desc']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']
    list_editable = ['name', 'desc']
    model_icon = 'fa fa-map-marker'


xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(City, CityAdmin)
