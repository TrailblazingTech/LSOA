from django import template

from ..models import Course

register = template.Library()


@register.filter
def contains(observations, construct):
    return any(o.level.construct == construct for o in observations)


@register.filter
def observation_pks(observations):
    return [o.pk for o in observations]


@register.filter
def course_from_session_or_first(request):
    if request.user.is_authenticated:
        if request.user.default_course:
            return request.user.default_course.pk
        else:
            return request.session.get('course') or Course.objects.first().id
    else:
        return request.session.get('course')


@register.filter
def get_color_for_sublevel(obj, observations):
    return obj.get_color(len(observations))


@register.simple_tag(takes_context=True)
def get_color_star_chart_4(context, sublevel, level_observations):
    return sublevel.get_color_dark(len(level_observations), context['observations_count'])
