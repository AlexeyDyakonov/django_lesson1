from django.utils.timezone import localtime

def get_duration(visit):

    delta = localtime(visit.leaved_at) - visit.created_at
    return delta
def is_visit_long(visit, minutes=60):

    duration = get_duration(visit)
    seconds = duration.total_seconds()
    spent_minutes = int(seconds) // 60
    return spent_minutes > minutes
def format_duration(duration):

    seconds = duration.total_seconds()
    hours = int(seconds) // 3600
    minutes = (int(seconds) % 3600) // 60
    return f'{hours}ч {minutes}мин'
