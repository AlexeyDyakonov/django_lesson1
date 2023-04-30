from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from time_functions import get_duration
from time_functions import is_visit_long
from time_functions import format_duration


def passcard_info_view(request, passcode):

    this_passcard_visits_list = []
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:

        duration = get_duration(visit)
        formated_duration_time = format_duration(duration)
        is_strange = is_visit_long(visit)
        this_passcard_visits = {
                "entered_at": visit.created_at,
                "duration": formated_duration_time,
                "is_strange": is_strange
            }

        this_passcard_visits_list.append(this_passcard_visits)

    context = {
            'passcard': passcard,
            'this_passcard_visits': this_passcard_visits_list
        }
    return render(request, 'passcard_info.html', context)
