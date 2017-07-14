from django.contrib import admin
from .models import Contact, Grant, Schedule, File
import csv
import datetime
from django.http import HttpResponse


def export_to_csv(modeladmin, request, queryset):
	opts = modeladmin.model._meta
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
	writer = csv.writer(response)

	fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
	# Write a first row with header information
	writer.writerow([field.verbose_name for field in fields])
	# Write data rows
	for obj in queryset:
		data_row = []
		for field in fields:
			value = getattr(obj, field.name)
			if isinstance(value, datetime.datetime):
				value = value.strftime('%d/%m/%Y')
			data_row.append(value)
		writer.writerow(data_row)
	return response
export_to_csv.short_description = 'Export to CSV'


class ContactAdmin(admin.ModelAdmin):
	list_display = ('organization_name', 'phone', 'email', 'website', 'contact_person')
	search_fields = ('organization_name', 'phone', 'email', 'website', 'contact_person')


class ScheduleInline(admin.StackedInline):
	model = Schedule


class FileInline(admin.TabularInline):
	model = File


class GrantAdmin(admin.ModelAdmin):
	list_filter = ('sector', 'year')
	list_display = ('project_name', 'grant_requested', 'grant_awarded', 'grant_stream', 'year')
	search_fields = ('project_name', 'grant_requested', 'grant_awarded', 'grant_stream', 'year')
	actions = [export_to_csv]
	inlines = [
		FileInline,
		ScheduleInline,
		]


admin.site.register(Contact, ContactAdmin)
admin.site.register(Grant, GrantAdmin)