from django.utils.safestring import mark_safe
from django.db.models import Q
from django import forms

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

from .models import *

class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class HorizontalCheckboxRenderer(forms.CheckboxSelectMultiple.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class SignatureForm(forms.Form):
	# pass
	signature = JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#000'}))

class AppDetailsForm(forms.ModelForm):
	POSITION_CHOICES = (
			('Position Applied', 'Position Applied'),
			('Captain', 'Captain'),
            ('Chief Mate', 'Chief Mate'),
            ('Chief Engineer', 'Chief Engineer'),
            ('2nd Engineer', '2nd Engineer'),
            ('Deck Engine', 'Deck Engine'),
            ('Cadet Engine', 'Cadet Engine'),
		)
	ALTERNATIVE_CHOICES = (
			('Alternative Position', 'Alternative Position'),
			('Captain', 'Captain'),
            ('Chief Mate', 'Chief Mate'),
            ('Chief Engineer', 'Chief Engineer'),
            ('2nd Engineer', '2nd Engineer'),
            ('Deck Engine', 'Deck Engine'),
            ('Cadet Engine', 'Cadet Engine'),
		)
	position_applied = forms.ChoiceField(choices=POSITION_CHOICES, error_messages={'invalid_choice': 'Please select a valid choice'})
	alternative_position = forms.ChoiceField(choices=ALTERNATIVE_CHOICES, error_messages={'invalid_choice': 'Please select a valid choice'})
	class Meta:
		model = AppDetails
		fields = ('application_date', 'position_applied', 'alternative_position')
		
class AppSourceForm(forms.ModelForm):
	SOURCE_CHOICES = (
			('Advertisement', 'Advertisement'),
			('Internet', 'Internet'),
			('Friends or Relatives', 'Friends or Relatives'),
			('Seafarer Center', 'Seafarer Center'),
		)
	source = forms.ChoiceField(widget=forms.RadioSelect, choices=SOURCE_CHOICES, error_messages={'required': 'Please let us know how you learned our company'})
	class Meta:
		model = AppSource
		fields = ('source', )

class PersonalDataForm(forms.ModelForm):
	age = forms.IntegerField(error_messages={'required': 'Please Fill up your Date of Birth'})
	flags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(renderer=HorizontalCheckboxRenderer), queryset=FlagDocuments.objects.filter(~Q(flags='None')), required=False)
	training_certificates = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(renderer=HorizontalCheckboxRenderer), queryset=TrainingCertificates.objects.all(), error_messages={'required': 'Please do not forget to select among the trainings and certificates'})
	class Meta:
		model = PersonalData
		fields = '__all__'
		exclude = ('permanent_address', 'spouse', 'current_address')

class PermanentAddressForm(forms.ModelForm):
	class Meta:
		model = PermanentAddress
		fields = '__all__'

class CurrentAddressForm(forms.ModelForm):
	class Meta:
		model = CurrentAddress
		fields = '__all__'

class SpouseForm(forms.ModelForm):
	class Meta:
		model = Spouse
		fields = '__all__'

class CollegeForm(forms.ModelForm):
	class Meta:
		model = College
		fields = '__all__'
		
class HighSchoolForm(forms.ModelForm):
	class Meta:
		model = HighSchool
		fields = '__all__'
		
class EmergencyContactForm(forms.ModelForm):
	class Meta:
		model = EmergencyContact
		fields = '__all__'

class BackgroundInformationForm(forms.ModelForm):
	CHOICES = (
			('1', 'Yes'),
			('0', 'No'),
		)
	visa_application = forms.NullBooleanField(widget=forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer))
	detained = forms.NullBooleanField(widget=forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer))
	disciplinary_action = forms.NullBooleanField(widget=forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer))
	
	class Meta:
		model = BackgroundInformation
		fields = '__all__'

	def clean(self):
		msg = "Please choose either yes or no"
		try:
			visa_application = selfdata['visa_application']
		except:
			visa_application = self.cleaned_data['visa_application']
		if visa_application is None:	
			self.add_error('visa_application', msg)
		try:
			detained = selfdata['detained']
		except:
			detained = self.cleaned_data['detained']
		if detained is None:	
			self.add_error('detained', msg)
		try:
			disciplinary_action = selfdata['disciplinary_action']
		except:
			disciplinary_action = self.cleaned_data['disciplinary_action']
		if disciplinary_action is None:	
			self.add_error('disciplinary_action', msg)


class PassportForm(forms.ModelForm):
	class Meta:
		model = Passport
		fields = ('passport', 'passport_expiry')
		
class SBookForm(forms.ModelForm):
	class Meta:
		model = SBook
		fields = ('sbook', 'sbook_expiry')
		
class COCForm(forms.ModelForm):
	class Meta:
		model = COC
		fields = ('coc', 'coc_expiry', 'coc_rank')
		
class LicenseForm(forms.ModelForm):
	class Meta:
		model = License
		fields = ('license', 'license_rank')
		
class SRCForm(forms.ModelForm):
	class Meta:
		model = SRC
		fields = ('src', 'src_rank')
		
class GOCForm(forms.ModelForm):
	class Meta:
		model = GOC
		fields = ('goc', 'goc_expiry')
		
class USVisaForm(forms.ModelForm):
	CHOICES = (
			('1', 'Yes'),
			('0', 'No'),
		)
	usvisa_type = forms.NullBooleanField(widget=forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer))
	class Meta:
		model = USVisa
		fields = ('usvisa_type', 'usvisa_expiry')

	def clean(self):
		try:
			value = selfdata['usvisa_type']
		except:
			value = self.cleaned_data['usvisa_type']
		if value is None:	
			msg = "Please choose either yes or no"
			self.add_error('usvisa_type', msg)


class SchengenVisaForm(forms.ModelForm):
	CHOICES = (
			('1', 'Yes'),
			('0', 'No'),
		)
	schengen_type = forms.NullBooleanField(widget=forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer))
	class Meta:
		model = SchengenVisa
		fields = ('schengen_type', 'schengen_expiry')

	def clean(self):
		try:
			value = selfdata['schengen_type']
		except:
			value = self.cleaned_data['schengen_type']
		if value is None:
			msg = "Please choose either yes or no"
			self.add_error('schengen_type', msg)
		
class YellowFeverForm(forms.ModelForm):
	class Meta:
		model = YellowFever
		fields = ('yellow_fever', 'yellow_fever_expiry')

class SeaServiceForm(forms.ModelForm):
	SEASERVICE_CHOICES = (
			('Cause of Discharge', 'Cause of Discharge'),
			('Finished Contract', 'Finished Contract'),
			('Compassionate Reason', 'Compassionate Reason'),
            ('Medical Repatriation', 'Medical Repatriation'),
            ('Promoted on Board', 'Promoted on Board'),
            ('Vessel Sold', 'Vessel Sold'),
            ('Vessel Scraped', 'Vessel Scraped'),
            ('Change Management', 'Change Management'),
            ('Own Request', 'Own Request'),
		)
	cause_of_discharge = forms.ChoiceField(choices=SEASERVICE_CHOICES)
	class Meta:
		model = SeaService
		fields = '__all__'
		exclude = ('personal_data', )

class AppForms(forms.ModelForm):
	signatures = JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#000'}), error_messages={'required': 'Please do not forget to sign before submitting'})	
	essay = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control essay", 'id':"essay"}))
	class Meta:
		model = AppForm
		fields = ('essay', 'signatures')