from django.contrib import admin
from .models import*

# Register your models here.
admin.site.register(Complaint)
admin.site.register(Queries)
admin.site.register(MyUser)

admin.site.register(Feedback)



admin.site.site_header = 'Crowdsourced_complaints'                    # default: "Django Administration"
admin.site.index_title = 'ADMIN'                 # default: "Site administration"
admin.site.site_title = 'Crowdsourced_complaints'                 # default: "Site administration"