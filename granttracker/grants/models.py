from django.db import models


class Contact(models.Model):
	organization_name = models.CharField(max_length=255)
	address = models.CharField(max_length=255, null=True, blank=True)
	phone = models.CharField(max_length=255, null=True, blank=True)
	email = models.EmailField(max_length=255, null=True, blank=True)
	website = models.URLField(max_length=255, null=True, blank=True)
	contact_person = models.CharField(max_length=255, null=True, blank=True)
	charitable_number = models.CharField(max_length=255, null=True, blank=True)

	class Meta:
		verbose_name_plural = "Contacts"
		ordering = ['organization_name']

	def __str__(self):
		return u"%s" % self.organization_name


class Grant(models.Model):
	project_name = models.CharField(max_length=255)
	grant_requested = models.CharField(max_length=255, null=True, blank=True)
	grant_awarded = models.CharField(max_length=255, null=True, blank=True)
	funds_not_used = models.CharField(max_length=255, null=True, blank=True)
	sector = models.CharField(max_length=255, null=True, blank=True)
	partnership = models.CharField(max_length=255, null=True, blank=True)
	year = models.CharField(max_length=255, null=True, blank=True)
	grant_stream = models.CharField(max_length=255, null=True, blank=True)
	fund = models.CharField(max_length=255, null=True, blank=True)
	community_impact = models.TextField(max_length=10000, null=True, blank=True)
	contact = models.ForeignKey(Contact, on_delete=models.CASCADE, default=None)

	class Meta:
		verbose_name_plural = "grants"
		ordering = ['project_name']

	def __str__(self):
		return u"%s" % self.project_name


class Schedule(models.Model):
	date_funds_required = models.DateField()
	date_reports_due = models.DateField()
	reports_received = models.DateField()
	schedule = models.ForeignKey(Grant, on_delete=models.CASCADE, default=None)

	class Meta:
		verbose_name_plural = "schedules"


class File(models.Model):
	file = models.ForeignKey(Grant, on_delete=models.CASCADE, default=None)
	filename = models.CharField(max_length=255, default=None)
	attachment = models.FileField(upload_to='attachments', default=None)

	class Meta:
		verbose_name_plural = "files"
