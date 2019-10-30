from tastypie.resources import ModelResource
from apps.jobs_app.models import *

class JobResource(ModelResource):
    class Meta:
        queryset = Job.objects.all()
        resource_name = 'job'