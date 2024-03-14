from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_length(url):
    if not (15 <= len(url) <= 60):
        raise ValidationError('URL의 길이는 15에서 60 사이여야 합니다.')

class APIInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    api_url = models.URLField(validators=[URLValidator(schemes=['http', 'https']), validate_length])
    documentation_url = models.URLField(max_length=200)
    auth_required = models.BooleanField()
    additional_info = models.JSONField(blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)