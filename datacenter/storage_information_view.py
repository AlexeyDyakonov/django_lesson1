from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import format_duration

def storage_information_view(request):


    non_closed_visit_list = []
    not_leaved = Visit.objects.filter(leaved_at=None)
    for not_leave in not_leaved:
        who_entered = not_leave.passcard.owner_name
        entered_at = not_leave.entered_at
        time_seconds = not_leave.get_duration()
        time_hours = int(time_seconds // 3600)

        non_closed_visit = [
            {
                "who_entered": who_entered,
                "entered_at": entered_at,
                "duration": format_duration(not_leave.get_duration()),
            }
        ]
        non_closed_visit_list.extend(non_closed_visit)
        context = {
            "non_closed_visits": non_closed_visit_list  # не закрытые посещения
        }
    return render(request, 'storage_information.html', context)
