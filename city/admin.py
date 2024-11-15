from django.contrib import admin
from .models import*

# Register your models here.
admin.site.register(Complaint)
admin.site.register(Queries)
admin.site.register(MyUser)
admin.site.register(GreenInitiative)
admin.site.register(GreenInitiativeComment)
admin.site.register(Feedback)
admin.site.register(Service)
admin.site.register(Manager)

admin.site.site_header = 'Clean Dream'                    # default: "Django Administration"
admin.site.index_title = 'ADMIN'                 # default: "Site administration"
admin.site.site_title = 'Clean Dream'                 # default: "Site administration"



