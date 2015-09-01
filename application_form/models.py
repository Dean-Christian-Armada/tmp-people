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
	college = models.CharField(max_length=100, default=None)
	degree_obtained = models.CharField(max_length=50, default=None)
	coll_from = models.PositiveIntegerField()
	coll_to = models.PositiveIntegerField()

	def __str__(self):
		return str(self.college)

class HighSchool(models.Model):
	highschool = models.CharField(max_length=100, default=None)
	hs_from = models.PositiveIntegerField()
	hs_to = models.PositiveIntegerField()

	def __str__(self):
		return str(self.highschool)


class Education(models.Model):
	college = models.OneToOneField('College')
	highschool = models.OneToOneField('HighSchool')

	def __str__(self):
		return self.college.college

##### END Educational Information


class EmergencyContact(models.Model):
	emergency_name = models.CharField(max_length=100, default=None)
	emergency_contact = models.CharField(max_length=100, default=None)
	relationship = models.CharField(max_length=50, default=None)
	# address = models.CharField(max_length=100, default=None)
	emergency_street = models.CharField(max_length=50, default=None)
	emergency_baranggay = models.CharField(max_length=50, default=None)
	# emergency_town = models.CharField(max_length=50, default=None)
	emergency_municipality = models.CharField(max_length=50, default=None)
	emergency_zip = models.PositiveIntegerField()

	def __str__(self):
		return str(self.emergency_name)

class BackgroundInformation(models.Model):
	visa_application = models.NullBooleanField()
	detained = models.NullBooleanField()
	disciplinary_action = models.NullBooleanField()

	def __str__(self):
		return "BackgroundInformation"


##### START National Certificates and Documents

class Passport(models.Model):
	passport = models.CharField(max_length=100, default=None, unique=True)
	passport_expiry = models.DateField()

	def __str__(self):
		return str(self.passport)

class SBook(models.Model):
	sbook = models.CharField(max_length=100, default=None, unique=True)
	sbook_expiry = models.DateField()

	def __str__(self):
		return str(self.sbook)

class COC(models.Model):
	coc = models.CharField(max_length=100, default=None, unique=True)
	coc_expiry = models.DateField()
	coc_rank = models.CharField(max_length=50, default=None)

	def __str__(self):
		return str(self.coc)

class License(models.Model):
	license = models.CharField(max_length=50, default=None, unique=True)
	license_rank = models.CharField(max_length=50, default=None)

	def __str__(self):
		return str(self.license)

class SRC(models.Model):
	src = models.CharField(max_length=50, default=None, unique=True)
	src_rank = models.CharField(max_length=50, default=None)

	def __str__(self):
		return str(self.src)

class GOC(models.Model):
	goc = models.CharField(max_length=50, default=None, unique=True)
	goc_expiry = models.DateField()

	def __str__(self):
		return str(self.goc)

class USVisa(models.Model):
	usvisa_type = models.NullBooleanField()
	usvisa_expiry = models.DateField()

	def __str__(self):
		return str(self.usvisa_type)

class SchengenVisa(models.Model):
	schengen_type = models.NullBooleanField()
	schengen_expiry = models.DateField()

	def __str__(self):
		return str(self.schengen_type)

class YellowFever(models.Model):
	yellow_fever = models.PositiveIntegerField(unique=True)
	yellow_fever_expiry = models.DateField()

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
	schengen_visa = models.OneToOneField('SchengenVisa')
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
	spouse_name =  models.CharField(max_length=100, null=True, blank=True)
	birthdate = models.DateField(default=None, null=True, blank=True)
	spouse_contact = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.spouse_name

class PermanentAddress(models.Model):
	permanent_street = models.CharField(max_length=50, default=None)
	permanent_baranggay = models.CharField(max_length=50, default=None)
	# permanent_town = models.CharField(max_length=50, default=None)
	permanent_municipality = models.CharField(max_length=50, default=None)
	permanent_zip = models.PositiveIntegerField()

	def __str__(self):
		address = "%s %s %s %s" % (self.permanent_street, self.permanent_baranggay, self.permanent_municipality, self.permanent_zip)
		return address

class CurrentAddress(models.Model):
	current_street = models.CharField(max_length=50, default=None)
	current_baranggay = models.CharField(max_length=50, default=None)
	# current_town = models.CharField(max_length=50, default=None)
	current_municipality = models.CharField(max_length=50, default=None)
	current_zip = models.PositiveIntegerField()

	def __str__(self):
		address = "%s %s %s %s" % (self.current_street, self.current_baranggay, self.current_municipality, self.current_zip)
		return address

class PersonalData(models.Model):
	CIVIL_CHOICES = (
			('Civil Status', 'Civil Status'),
			('M', 'Married'),
            ('S', 'Single'),
            ('LS', 'Legally Separated'),
            ('W', 'Widow'),
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
	sss = models.CharField(max_length=50, blank=True, null=True, default=None)
	philhealth = models.CharField(max_length=50, blank=True, null=True, default=None)
	tin = models.CharField(max_length=50, blank=True, null=True, default=None)
	pagibig = models.CharField(max_length=50, blank=True, null=True, default=None)
	civil_status = models.CharField(max_length=50, default=None, choices=CIVIL_CHOICES)
	married_date = models.DateField(default=None, null=True, blank=True)
	father_name = models.CharField(max_length=100, null=True)
	mother_name = models.CharField(max_length=100, null=True)
	permanent_address = models.ForeignKey(PermanentAddress, default=None)
	current_address = models.ForeignKey(CurrentAddress, default=None)
	spouse = models.ForeignKey(Spouse, default=None)
	flags = models.ManyToManyField(FlagDocuments, blank=True)
	training_certificates = models.ManyToManyField(TrainingCertificates)

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
	# reference = models.OneToOneField('Reference', default=None)
	# sea_service = models.ForeignKey('SeaService', default=None)
	essay = models.TextField(default=None)
	# signature = models.ImageField(upload_to='signatures', default=None)
	signatures = models.ImageField(upload_to='signatures', default=None, blank=True)

	def __str__(self):
		# appform = "dean"
		return str(self.id)

class SeaService(models.Model):
	personal_data = models.ForeignKey('PersonalData', default=None)
	vessel_name = models.CharField(max_length=50, default=None, blank=True, null=True)
	vessel_type = models.CharField(max_length=50, default=None, blank=True, null=True)
	flag = models.CharField(max_length=50, default=None, blank=True, null=True)
	grt = models.PositiveIntegerField(blank=True, null=True)
	dwt = models.PositiveIntegerField(default=None, blank=True, null=True)
	year_built = models.PositiveIntegerField(blank=True, null=True)
	engine_type = models.CharField(max_length=50, default=None, blank=True, null=True)
	hp = models.DecimalField(blank=True, null=True, decimal_places=1, max_digits=10)
	kw = models.DecimalField(default=None, blank=True, null=True, decimal_places=1, max_digits=10)
	manning_agency = models.CharField(max_length=50, default=None, blank=True, null=True)
	principal = models.CharField(max_length=50, default=None, blank=True, null=True)
	date_joined = models.DateField(blank=True, null=True)
	date_left = models.DateField(blank=True, null=True)
	duration = models.PositiveIntegerField(blank=True, null=True)
	rank = models.CharField(max_length=50, default=None, blank=True, null=True)
	cause_of_discharge = models.CharField(max_length=100, default=None, blank=True, null=True)

	def __str__(self):
		return self.vessel_name

	def save(self, *args, **kwargs):
		if self.vessel_name == '':
			return False
		super(SeaService, self).save(*args, **kwargs)