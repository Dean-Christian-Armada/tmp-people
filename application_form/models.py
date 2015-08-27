from django.core.validators import RegexValidator
from django.db import models

# from jsignature.mixins import JSignatureFieldsMixin

# Create your models here.

# class JSignatureModel(JSignatureFieldsMixin):
# 	name = models.CharField(max_length=100, default=None)
# 	signatures = models.ImageField(upload_to='signatures', blank=True, default=None)


# class Sample(models.Model):
# 	picture = models.ImageField(upload_to='signatures', blank=True, default=None)
# 	name = models.CharField(max_length=100, default='dean')

# 	def __unicode__(self):
# 		return self.name

class AppDetails(models.Model):
	application_date = models.DateField()
	position_applied = models.CharField(max_length=50, default=None,)
	alternative_position = models.CharField(max_length=50, default=None,)
	picture = models.ImageField(upload_to='application_pictures', blank=True)
	appsource = models.OneToOneField('AppSource', default=None)
	
	def __str__(self):
		return str(self.application_date)

# class Source(models.Model):
# 	source = models.CharField(max_length=50, default=None)

# 	def __str__(self):
# 		return self.source


class AppSource(models.Model):
	source = models.CharField(max_length=50, default=None)
	specific = models.CharField(max_length=50, default=None, null=True, blank=True)

	def __str__(self):
		return "%s - %s" % (self.source, self.specific)



##### START Educational Information

class College(models.Model):
	school = models.CharField(max_length=100, default=None)
	degree_obtained = models.CharField(max_length=50, default=None)
	coll_from = models.DateField()
	coll_to = models.DateField()

	def __str__(self):
		return str(self.school)

class HighSchool(models.Model):
	school = models.CharField(max_length=100, default=None)
	hs_from = models.DateField()
	hs_to = models.DateField()

	def __str__(self):
		return str(self.school)


class Education(models.Model):
	college = models.OneToOneField('College')
	highschool = models.OneToOneField('HighSchool')

	def __str__(self):
		return self.tertiary.school

##### END Educational Information


class EmergencyContact(models.Model):
	name = models.CharField(max_length=100, default=None)
	contact = models.CharField(max_length=100, default=None)
	relationship = models.CharField(max_length=50, default=None)
	# address = models.CharField(max_length=100, default=None)
	street = models.CharField(max_length=50, default=None)
	baranggay = models.CharField(max_length=50, default=None)
	town = models.CharField(max_length=50, default=None)
	municipality = models.CharField(max_length=50, default=None)
	zip = models.PositiveIntegerField()

	def __str__(self):
		return str(self.name)

class BackgroundInformation(models.Model):
	visa_application = models.BooleanField()
	detained = models.BooleanField()
	disciplinary_action = models.BooleanField()

	def __str__(self):
		return "BackgroundInformation"


##### START National Certificates and Documents

class Passport(models.Model):
	passport = models.CharField(max_length=100, default=None, unique=True)
	expiry = models.DateField()
	place = models.CharField(max_length=50, default=None)

	def __str__(self):
		return str(self.passport)

class SBook(models.Model):
	sbook = models.CharField(max_length=100, default=None, unique=True)
	expiry = models.DateField()
	place = models.CharField(max_length=50, default=None)

	def __str__(self):
		return str(self.sbook)

class COC(models.Model):
	coc = models.CharField(max_length=100, default=None, unique=True)
	expiry = models.DateField()
	rank = models.CharField(max_length=50, default=None)

	def __str__(self):
		return str(self.coc)

class License(models.Model):
	license = models.CharField(max_length=50, default=None, unique=True)
	rank = models.CharField(max_length=50, default=None)

	def __str__(self):
		return str(self.license)

class SRC(models.Model):
	src = models.CharField(max_length=50, default=None, unique=True)
	rank = models.CharField(max_length=50, default=None)

	def __str__(self):
		return str(self.src)

class GOC(models.Model):
	goc = models.CharField(max_length=50, default=None, unique=True)
	expiry = models.DateField()

	def __str__(self):
		return str(self.goc)

class USVisa(models.Model):
	type = models.BooleanField()
	expiry = models.DateField()

	def __str__(self):
		return str(self.type)

class SchengenVisa(models.Model):
	type = models.BooleanField()
	expiry = models.DateField()

	def __str__(self):
		return str(self.type)

class YellowFever(models.Model):
	yellow_fever = models.PositiveIntegerField(unique=True)
	expiry = models.DateField()

	def __str__(self):
		return str(self.yellow_fever)

class CertificatesDocuments(models.Model):
	passport = models.OneToOneField('Passport')
	sbook = models.OneToOneField('SBook')
	coc = models.OneToOneField('COC')
	license = models.OneToOneField('License')
	src = models.OneToOneField('SRC')
	goc = models.OneToOneField('GOC')
	us_visa = models.OneToOneField('USVisa')
	schgengen_visa = models.OneToOneField('SchengenVisa')
	yellow_fever = models.OneToOneField('YellowFever')

	def __str__(self):
		return str(self.passport.passport)
##### END National Certificates and Documents


class FlagDocuments(models.Model):
	flags = models.CharField(max_length=100, default=None)

	def __str__(self):
		return str(self.flags)

class TrainingCertificates(models.Model):
	trainings_certificates = models.CharField(max_length=100, default=None)

	def __str__(self):
		return str(self.trainings_certificates)

class Spouse(models.Model):
	name =  models.CharField(max_length=100, null=True)
	birthdate = models.DateField(default=None, null=True)
	contact = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.name

class PermanentAddress(models.Model):
	permanent_street = models.CharField(max_length=50, default=None)
	permanent_baranggay = models.CharField(max_length=50, default=None)
	permanent_town = models.CharField(max_length=50, default=None)
	permanent_municipality = models.CharField(max_length=50, default=None)
	permanent_zip = models.PositiveIntegerField()

	def __str__(self):
		address = "%s %s %s %s %s" % (self.permanent_street, self.permanent_baranggay, self.permanent_town, self.permanent_municipality, self.permanent_zip)
		return address

class CurrentAddress(models.Model):
	current_street = models.CharField(max_length=50, default=None)
	current_baranggay = models.CharField(max_length=50, default=None)
	current_town = models.CharField(max_length=50, default=None)
	current_municipality = models.CharField(max_length=50, default=None)
	current_zip = models.PositiveIntegerField()

	def __str__(self):
		address = "%s %s %s %s %s" % (self.current_street, self.current_baranggay, self.current_town, self.current_municipality, self.current_zip)
		return address

class PersonalData(models.Model):
	CIVIL_CHOICES = (
			('Civil Status', 'Civil Status'),
			('M', 'Married'),
            ('S', 'Single'),
		)
	last_name = models.CharField(max_length=50, default=None)
	first_name = models.CharField(max_length=50, default=None)
	middle_name = models.CharField(max_length=50, default=None)
	age = models.PositiveIntegerField()
	birth_date = models.DateField()
	birth_place = models.CharField(max_length=50, default=None)
	landline_1 = models.PositiveIntegerField(null=True)
	mobile_1 = models.CharField(max_length=50, null=True)
	email_address_1 = models.EmailField(null=True)
	landline_2 = models.PositiveIntegerField(default=None, blank=True, null=True)
	mobile_2 = models.CharField(max_length=50, blank=True, null=True)
	email_address_2 = models.EmailField(default=None, blank=True, null=True)
	preferred_vessel_type = models.CharField(max_length=50, default=None)
	availability_date = models.CharField(max_length=50, default=None)
	sss = models.CharField(max_length=50, default=None)
	philhealth = models.CharField(max_length=50, default=None)
	tin = models.CharField(max_length=50, default=None)
	pagibig = models.CharField(max_length=50, default=None)
	civil_status = models.CharField(max_length=50, default=None, choices=CIVIL_CHOICES)
	married_date = models.DateField(default=None, null=True, blank=True)
	father_name = models.CharField(max_length=100, null=True)
	mother_name = models.CharField(max_length=100, null=True)
	permanent_address = models.ForeignKey(PermanentAddress, default=None)
	current_address = models.ForeignKey(CurrentAddress, default=None)
	spouse = models.ForeignKey(Spouse, default=None)

	def __str__(self):
		name = "%s %s %s" % (self.first_name, self.middle_name, self.last_name, )
		return name

class Reference(models.Model):
	verified_by = models.CharField(max_length=100, null=True, blank=True, default=None)
	date = models.DateField()
	company_name = models.CharField(max_length=50, null=True, blank=True, default=None)
	person_contacted = models.CharField(max_length=100, null=True, blank=True, default=None)
	veracity_history = models.CharField(max_length=50, null=True, blank=True, default=None)
	health_problem = models.CharField(max_length=50, null=True, blank=True, default=None)
	financial_liability = models.CharField(max_length=50, null=True, blank=True, default=None)
	character = models.TextField(null=True, blank=True,)
	comments = models.TextField(null=True, blank=True,)

	def __str__(self):
		return self.verified_by

class AppForm(models.Model):
	# form_reference = models.CharField(max_length=50, default=None)
	app_details = models.OneToOneField('AppDetails')
	personal_data = models.OneToOneField('PersonalData')
	education = models.OneToOneField('Education')
	emergency_contact = models.OneToOneField('EmergencyContact')
	background_information = models.OneToOneField('BackgroundInformation')
	certificates_documents = models.OneToOneField('CertificatesDocuments')
	reference = models.OneToOneField('Reference', default=None)
	flags = models.ManyToManyField(FlagDocuments)
	training_certificates = models.ManyToManyField(TrainingCertificates)
	# sea_service = models.ForeignKey('SeaService', default=None)
	essay = models.TextField(default=None)
	signature = models.ImageField(upload_to='signatures', default=None)

	def __str__(self):
		appform = "%s %s %s : %s" % (self.personal_data.first_name, self.personal_data.middle_name, self.personal_data.last_name, self.app_details.application_date )
		return appform

class SeaService(models.Model):
	app_form = models.ForeignKey('AppForm', default=None)
	vessel_name = models.CharField(max_length=50, default=None)
	vessel_type = models.CharField(max_length=50, default=None)
	flag = models.CharField(max_length=50, default=None)
	grt = models.PositiveIntegerField()
	dwt = models.PositiveIntegerField(default=None)
	year_built = models.PositiveIntegerField()
	engine_type = models.CharField(max_length=50, default=None)
	hp = models.PositiveIntegerField()
	kw = models.PositiveIntegerField(default=None)
	manning_agency = models.CharField(max_length=50, default=None)
	principal = models.CharField(max_length=50, default=None)
	date_joined = models.DateField()
	date_left = models.DateField()
	duration = models.PositiveIntegerField()
	rank = models.CharField(max_length=50, default=None)
	cause_of_discharge = models.CharField(max_length=100, default=None)

	def __str__(self):
		return self.vessel_name