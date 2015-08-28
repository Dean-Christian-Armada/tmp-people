from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.forms.formsets import formset_factory
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from easy_pdf.views import PDFTemplateView
from easy_pdf.rendering import render_to_pdf_response

from jsignature.utils import draw_signature

from . forms import *

import os, shutil, datetime, random, string

# Create your views here.

@login_required()
def tmp_form(request):
	scheme = request.scheme
	http_host = request.META['HTTP_HOST']
	# appdetails_form = AppDetailsForm()
	# appsource_form = AppSourceForm()
	# personaldata_form = PersonalDataForm()
	# permanentaddress_form = PermanentAddressForm()
	# currentaddress_form = CurrentAddressForm()
	# spouse_form = SpouseForm()
	# college_form = CollegeForm()
	# highschool_form = HighSchoolForm()
	# emergencycontact_form = EmergencyContactForm()

	# backgroundinfo_form = BackgroundInformationForm()
	passport_form = PassportForm()
	sbook_form = SBookForm()
	coc_form = COCForm()
	license_form = LicenseForm()
	src_form = SRCForm()
	goc_form = GOCForm()
	usvisa_form = USVisaForm()
	schengenvisa_form = SchengenVisaForm()
	yellowfever_form = YellowFeverForm()


	if request.method == 'POST':
		request.POST = request.POST.copy()
		# if request.POST['position_applied'] == 'Position Applied':
		# 	request.POST['position_applied'] = ''
		# if request.POST['alternative_position'] == 'Alternative Position':
		# 	request.POST['alternative_position'] = ''
		# if request.POST['civil_status'] == 'Civil Status':
		# 	request.POST['civil_status'] = ''

		print request.POST

		# appdetails_form = AppDetailsForm(request.POST)
		# appsource_form = AppSourceForm(request.POST)
		# personaldata_form = PersonalDataForm(request.POST)
		# permanentaddress_form = PermanentAddressForm(request.POST)
		# currentaddress_form = CurrentAddressForm(request.POST)
		# spouse_form = SpouseForm(request.POST)
		# college_form = CollegeForm(request.POST)
		# highschool_form = HighSchoolForm(request.POST)
		# emergencycontact_form = EmergencyContactForm(request.POST)

		# backgroundinfo_form = BackgroundInformationForm(request.POST)
		passport_form = PassportForm(request.POST)
		sbook_form = SBookForm(request.POST)
		coc_form = COCForm(request.POST)
		license_form = LicenseForm(request.POST)
		src_form = SRCForm(request.POST)
		goc_form = GOCForm(request.POST)
		usvisa_form = USVisaForm(request.POST)
		schengenvisa_form = SchengenVisaForm(request.POST)
		yellowfever_form = YellowFeverForm(request.POST)


		if passport_form.is_valid() and sbook_form.is_valid() and coc_form.is_valid() and license_form.is_valid() and src_form.is_valid() and goc_form.is_valid() and usvisa_form.is_valid() and schengenvisa_form.is_valid() and yellowfever_form.is_valid():
			# http://127.0.0.1:8003/media/photos/tmp/mpifcxpaoi.jpg
			# tmp_application_picture = request.POST['application_picture']
			# tmp_application_picture = tmp_application_picture.replace(scheme+"://"+http_host+"/", "")
			# print tmp_application_picture
			# application_picture = "media/photos/abcd.jpg"
			# os.rename(tmp_application_picture, application_picture)
			# application_picture = application_picture.replace("media/", "")

			# appdetails = appdetails_form.save(commit=False)
			# appsource = appsource_form.save(commit=False)
			# appsource.specific = request.POST['specific']
			# appsource.save()
			# appdetails.appsource = appsource 
			# appdetails.picture = application_picture
			# appdetails.save()
			
			# permanentaddress = permanentaddress_form.save()
			# currentaddress = currentaddress_form.save()
			# spouse = spouse_form.save()
			# personaldata = personaldata_form.save(commit=False)
			# personaldata.permanent_address = permanentaddress
			# personaldata.current_address = currentaddress
			# personaldata.spouse = spouse
			# personaldata.save()

			# college_form = college_form.save()
			# highschool_form = highschool_form.save()
			# education = Education.objects.create(college=college_form, highschool=highschool_form)

			# emergencycontact_form.save()

			passport = passport_form.save()
			sbook = sbook_form.save()
			coc = coc_form.save()
			license = license_form.save()
			src = src_form.save()
			goc = goc_form.save()
			usvisa = usvisa_form.save()
			schengenvisa = schengenvisa_form.save()
			yellowfever = yellowfever_form.save()
			certificates_documents = CertificatesDocuments.objects.create(passport=passport, sbook=sbook, coc=coc, license=license, src=src, goc=goc, us_visa=usvisa, schengen_visa=schengenvisa, yellow_fever=yellowfever)


		else:
			# print "guinto"
			# print appdetails_form.errors
			# print appsource_form.errors
			# print personaldata_form.errors
			# print permanentaddress_form.errors
			# print currentaddress_form.errors
			# print spouse_form.errors
			# print college_form.errors
			# print highschool_form.errors
			# print emergencycontact_form.errors

			# print backgroundinfo_form.errors
			print passport_form.errors
			print sbook_form.errors
			print coc_form.errors
			print license_form.errors
			print src_form.errors
			print goc_form.errors
			print usvisa_form.errors
			print schengenvisa_form.errors
			print yellowfever_form.errors

			# print backgroundinfo_form.errors
			print passport_form.errors
			print sbook_form.errors
			print coc_form.errors
			print license_form.errors
			print src_form.errors
			print goc_form.errors
			print usvisa_form.errors
			print schengenvisa_form.errors
			print yellowfever_form.errors


	template = "application_form/tmp_index.html"
	context_dict = {"title": "Application Form"}
	# context_dict['appdetails_form'] = appdetails_form
	# context_dict['appsource_form'] = appsource_form
	# context_dict['personaldata_form'] = personaldata_form
	# context_dict['permanentaddress_form'] = permanentaddress_form
	# context_dict['currentaddress_form'] = currentaddress_form
	# context_dict['spouse_form'] = spouse_form
	# context_dict['college_form'] = college_form
	# context_dict['highschool_form'] = highschool_form
	# context_dict['emergencycontact_form'] = emergencycontact_form

	# context_dict['backgroundinfo_form'] = backgroundinfo_form
	context_dict['passport_form']= passport_form
	context_dict['sbook_form']= sbook_form
	context_dict['coc_form']= coc_form
	context_dict['license_form']= license_form
	context_dict['src_form']= src_form
	context_dict['goc_form']= goc_form
	context_dict['usvisa_form']= usvisa_form
	context_dict['schengenvisa_form']= schengenvisa_form
	context_dict['yellowfever_form']= yellowfever_form

	return render(request, template, context_dict)


@login_required
def success(request):
	template = "application_form/success.html"
	context_dict = {}
	return render(request, template, context_dict)

@csrf_exempt
@login_required
def tmp_image(request):
	if request.method == 'POST':
		tmp_image_name = ''.join(random.choice(string.lowercase) for i in range(10))
		# does not work with starting slash
		x = 'media/photos/tmp/'+tmp_image_name+'.jpg'
		# y = 'media/photos/image.jpg'
		f = open(x, 'wb')
		f.write(request.body)
		f.close()
		# os.rename(x, y)
		scheme = request.scheme
		http_host = request.META['HTTP_HOST']
		return HttpResponse(scheme+"://"+http_host+"/"+x)
	else:
		return HttpResponse("No data")



@login_required
def pdf_report(request, template):
	if template:
		if template == 'sea-service':
			template = "application_form/pdf-report-sea-service.html"
	# returns hypertext protocol: http or https
		else:
			template = "application_form/pdf-report.html"

		domain = request.scheme
		domain += "://"
		# returns domain name
		domain += request.META["HTTP_HOST"]
		context_dict = {"domain":domain}
		return render_to_pdf_response(request, template, context_dict)
	else:
		raise Http404("System Error.")