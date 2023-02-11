from django.db import models
import django

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
    def get_duration(self):

        entered_at_your_timezone = django.utils.timezone.localtime(self.entered_at)
        try:
            residence_time = self.leaved_at - self.entered_at
        except TypeError:
            residence_time = django.utils.timezone.now() - entered_at_your_timezone

        time_seconds = residence_time.total_seconds()

        return time_seconds

    def is_visit_long(self, visit_duration, hours=1):
        return visit_duration >= hours

def format_duration(time_seconds):

    time_hours = int(time_seconds // 3600)
    time_minutes = int((time_seconds - time_hours * 3600) // 60)
    formated_time = f'{time_hours} ч : {time_minutes} мин'
    return formated_time