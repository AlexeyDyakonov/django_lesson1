from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import format_duration
from datacenter.models import get_duration

def storage_information_view(request):

    non_closed_visit_list = []
    not_leaved = Visit.objects.filter(leaved_at__isnull=True)

    for visit in not_leaved:
        who_entered = visit.passcard.owner_name

        duration = get_duration(visit)

        formated_duration_time = format_duration(duration)
        non_closed_visit = [
            {
                "who_entered": who_entered,
                "entered_at": visit.created_at,
                "duration":  formated_duration_time,
            }
        ]
        non_closed_visit_list.extend(non_closed_visit)

    context = {
            "non_closed_visits": non_closed_visit_list
        }
    return render(request, 'storage_information.html', context)
