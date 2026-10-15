from django.db import models
from django.contrib.auth.models import User

REGIONS = {
    'northeast': ("Northeast", 42, -75),
    'southeast': ("Southeast", 33, -84),
    'midwest': ("Midwest", 41.5, -89),
    'south_central': ("South Central", 31.5, -98),
    'mountain': ("Mountain West", 40.5, -109),
    'pacific': ("Pacific", 39, -121)
}
REGION_CHOICES = [(code, info[0]) for code, info in REGIONS.items()]

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    region = models.CharField(max_length=20, choices=REGION_CHOICES)
    def __str__(self):
        return self.user.username + ' - ' + self.get_region_display()
