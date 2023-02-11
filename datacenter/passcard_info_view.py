from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404

def passcard_info_view(request, passcode):

    this_passcard_visits_list = []
    passcard = Passcard.objects.filter(passcode=passcode).get()
    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        entered_at = visit.entered_at
        time_seconds = visit.get_duration()
        time_hours = int(time_seconds // 3600)
        time_minutes = int((time_seconds - time_hours * 3600) // 60)
        this_passcard_visits = [
            {
                "entered_at": entered_at,
                "duration": f'{time_hours} ч : {time_minutes} мин',
                "is_strange": visit.is_visit_long(time_hours)
            },
        ]
        this_passcard_visits_list.extend(this_passcard_visits)

        context = {
            'passcard': passcard,
         'this_passcard_visits': this_passcard_visits_list
        }
    return render(request, 'passcard_info.html', context)
