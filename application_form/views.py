from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.forms.formsets import formset_factory
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings

from easy_pdf.views import PDFTemplateView
from easy_pdf.rendering import render_to_pdf_response

from jsignature.utils import draw_signature

from . forms import *
from . models import *

import os, shutil, datetime, random, string

# Create your views here.

@login_required()
def tmp_form(request):
	scheme = request.scheme
	http_host = request.META['HTTP_HOST']
	appdetails_form = AppDetailsForm()
	appsource_form = AppSourceForm()
	personaldata_form = PersonalDataForm()
	permanentaddress_form = PermanentAddressForm()
	currentaddress_form = CurrentAddressForm()
	spouse_form = SpouseForm()
	college_form = CollegeForm()
	highschool_form = HighSchoolForm()
	emergencycontact_form = EmergencyContactForm()

	backgroundinfo_form = BackgroundInformationForm()
	passport_form = PassportForm()
	sbook_form = SBookForm()
	coc_form = COCForm()
	license_form = LicenseForm()
	src_form = SRCForm()
	goc_form = GOCForm()
	usvisa_form = USVisaForm()
	schengenvisa_form = SchengenVisaForm()
	yellowfever_form = YellowFeverForm()
	seaservice_form = formset_factory(SeaServiceForm, extra=10)
	app_form = AppForm()


	if request.method == 'POST':
		request.POST = request.POST.copy()
		if request.POST['position_applied'] == 'Position Applied':
			request.POST['position_applied'] = ''
		if request.POST['alternative_position'] == 'Alternative Position':
			request.POST['alternative_position'] = ''
		if request.POST['civil_status'] == 'Civil Status':
			request.POST['civil_status'] = ''

		print request.POST

		appdetails_form = AppDetailsForm(request.POST)
		appsource_form = AppSourceForm(request.POST)
		personaldata_form = PersonalDataForm(request.POST)
		permanentaddress_form = PermanentAddressForm(request.POST)
		currentaddress_form = CurrentAddressForm(request.POST)
		spouse_form = SpouseForm(request.POST)
		college_form = CollegeForm(request.POST)
		highschool_form = HighSchoolForm(request.POST)
		emergencycontact_form = EmergencyContactForm(request.POST)

		backgroundinfo_form = BackgroundInformationForm(request.POST)
		passport_form = PassportForm(request.POST)
		sbook_form = SBookForm(request.POST)
		coc_form = COCForm(request.POST)
		license_form = LicenseForm(request.POST)
		src_form = SRCForm(request.POST)
		goc_form = GOCForm(request.POST)
		usvisa_form = USVisaForm(request.POST)
		schengenvisa_form = SchengenVisaForm(request.POST)
		yellowfever_form = YellowFeverForm(request.POST)

		seaservice_form = seaservice_form(request.POST)
		app_form = AppForm(request.POST)


		if appdetails_form.is_valid() and appsource_form.is_valid() and personaldata_form.is_valid() and permanentaddress_form.is_valid() and currentaddress_form.is_valid() and spouse_form.is_valid() and college_form.is_valid() and highschool_form.is_valid() and emergencycontact_form.is_valid() and backgroundinfo_form.is_valid() and passport_form.is_valid() and sbook_form.is_valid() and coc_form.is_valid() and license_form.is_valid() and src_form.is_valid() and goc_form.is_valid() and usvisa_form.is_valid() and schengenvisa_form.is_valid() and yellowfever_form.is_valid() and seaservice_form.is_valid() and app_form.is_valid():
			first_name = request.POST['first_name']
			middle_name = request.POST['middle_name']
			last_name = request.POST['last_name']
			file_name = first_name+middle_name+last_name
			file_name = "".join(file_name.split())
			signature = app_form.cleaned_data.get('signatures')

			tmp_application_picture = request.POST['application_picture']
			tmp_application_picture = tmp_application_picture.replace(scheme+"://"+http_host+"/", "")
			print tmp_application_picture
			application_picture = "media/photos/"+file_name+".jpg"
			os.rename(tmp_application_picture, application_picture)
			application_picture = application_picture.replace("media/", "")
			appdetails = appdetails_form.save(commit=False)
			appsource = appsource_form.save(commit=False)
			appsource.specific = request.POST['specific']
			appsource.save()
			appdetails.appsource = appsource 
			appdetails.picture = application_picture
			appdetails.save()
			
			permanentaddress = permanentaddress_form.save()
			currentaddress = currentaddress_form.save()
			spouse = spouse_form.save()
			personaldata = personaldata_form.save(commit=False)
			personaldata.permanent_address = permanentaddress
			personaldata.current_address = currentaddress
			personaldata.spouse = spouse
			personaldata.save()

			college_form = college_form.save()
			highschool_form = highschool_form.save()
			education = Education.objects.create(college=college_form, highschool=highschool_form)

			emeregency = emergencycontact_form.save()

			backgroundinfo = backgroundinfo_form.save()

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
			
			for form in seaservice_form:
				m = form.save(commit=False)
				m.personal_data = personaldata
				m.save()

			app_form = app_form.save(commit=False)
			signature_path = "media/signature/"+file_name+".png"
			if signature:
				signature_picture = draw_signature(signature)
				_signature_file_path = draw_signature(signature, as_file=True)
				signature_file_path = settings.MEDIA_ROOT+"/signatures/"
				shutil.move(_signature_file_path, signature_file_path)
				_signature_file_path = _signature_file_path.replace('/tmp/', 'signatures/')
			app_form.app_details = appdetails
			app_form.signatures = _signature_file_path
			app_form.personal_data = personaldata
			app_form.education = education
			app_form.emergency_contact = emeregency
			app_form.background_information = backgroundinfo
			app_form.certificates_documents = certificates_documents
			app_form.save()

			return HttpResponseRedirect('/application-form/success/?id='+app_form)
			
			



		else:
			print appdetails_form.errors
			print appsource_form.errors
			print personaldata_form.errors
			print permanentaddress_form.errors
			print currentaddress_form.errors
			print spouse_form.errors
			print college_form.errors
			print highschool_form.errors
			print emergencycontact_form.errors

			print backgroundinfo_form.errors
			print passport_form.errors
			print sbook_form.errors
			print coc_form.errors
			print license_form.errors
			print src_form.errors
			print goc_form.errors
			print usvisa_form.errors
			print schengenvisa_form.errors
			print yellowfever_form.errors

			print seaservice_form.errors

			print app_form.errors


	template = "application_form/tmp_index.html"
	context_dict = {"title": "Application Form"}
	context_dict['appdetails_form'] = appdetails_form
	context_dict['appsource_form'] = appsource_form

	context_dict['personaldata_form'] = personaldata_form
	context_dict['permanentaddress_form'] = permanentaddress_form
	context_dict['currentaddress_form'] = currentaddress_form
	context_dict['spouse_form'] = spouse_form
	
	context_dict['college_form'] = college_form
	context_dict['highschool_form'] = highschool_form
	
	context_dict['emergencycontact_form'] = emergencycontact_form

	context_dict['backgroundinfo_form'] = backgroundinfo_form
	context_dict['passport_form']= passport_form
	context_dict['sbook_form']= sbook_form
	context_dict['coc_form']= coc_form
	context_dict['license_form']= license_form
	context_dict['src_form']= src_form
	context_dict['goc_form']= goc_form
	context_dict['usvisa_form']= usvisa_form
	context_dict['schengenvisa_form']= schengenvisa_form
	context_dict['yellowfever_form']= yellowfever_form

	context_dict['seaservice_form'] = seaservice_form

	context_dict['app_form'] = app_form

	return render(request, template, context_dict)


@login_required
def success(request):
	template = "application_form/success.html"
	context_dict = {"title": "Thank You For Applying at Manship"}
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



# @login_required
# def pdf_report(request, template):
# 	if template:
# 		if template == 'sea-service':
# 			template = "application_form/pdf-report-sea-service.html"
# 	# returns hypertext protocol: http or https
# 		else:
# 			template = "application_form/pdf-report.html"

# 		domain = request.scheme
# 		domain += "://"
# 		# returns domain name
# 		domain += request.META["HTTP_HOST"]
# 		context_dict = {"domain":domain}
# 		return render_to_pdf_response(request, template, context_dict)
# 	else:
# 		raise Http404("System Error.")

@login_required
def pdf_report_sea_services(request, id):
	if id:
		sea_service = SeaService.objects.filter(personal_data=id)
		template = "application_form/pdf-report-sea-service.html"
		context_dict = {}
		context_dict['sea_service'] = sea_service
		return render_to_pdf_response(request, template, context_dict)


@login_required
def pdf_report(request, id):
	if id:
		appform = AppForm.objects.get(id=id)
		appdetails = appform.app_details
		appsource = appdetails.appsource
		personaldata = appform.personal_data
		education = appform.education
		emergency = appform.emergency_contact
		backgroundinfo = appform.background_information
		certificatesdocuments = appform.certificates_documents
			
		cayman_islands = personaldata.flags.filter(flags='Caymen Islands')
		marshall_islands = personaldata.flags.filter(flags='Marshall Islands')
		liberia = personaldata.flags.filter(flags='Liberia')
		cyprus = personaldata.flags.filter(flags='Cyprus')
		singapore = personaldata.flags.filter(flags='Singapore')
		greek = personaldata.flags.filter(flags='Greek')

		cop_bt = personaldata.training_certificates.filter(trainings_certificates='Certificate of Proficiency / Basic Training')
		cop_btoc = personaldata.training_certificates.filter(trainings_certificates='Certificate of Proficiency / Basic Training for Oil and Chemical Tanker')
		cop_atot = personaldata.training_certificates.filter(trainings_certificates='Certificate of Proficiency / Advance Training for Oil Tanker')
		cop_atct = personaldata.training_certificates.filter(trainings_certificates='Certificate of Proficiency / Advance Training for Chemical Tanker')
		cop_pfrb = personaldata.training_certificates.filter(trainings_certificates='Certificate of Proficiency / Proficiency in Fast Rescue Boat')
		cop_aff = personaldata.training_certificates.filter(trainings_certificates='Certificate of Proficiency / Advance Fire Fighting')
		cop_mefa = personaldata.training_certificates.filter(trainings_certificates='Certificate of Proficiency / Medical Emergency First Aid')
		cop_meca = personaldata.training_certificates.filter(trainings_certificates='	Certificate of Proficiency / Meical Care')
		cop_sso = personaldata.training_certificates.filter(trainings_certificates='Certificate of Proficiency / Ship Security Officer')
		cop_pscrb = personaldata.training_certificates.filter(trainings_certificates='	Certificate of Proficiency / Proficiency in Survival Craft and Rescue Boat')
		cop_ssa_sdsd = personaldata.training_certificates.filter(trainings_certificates='Certificate of Proficiency / Ship Security Awareness / Seafarers with Designated Security Duties')
		bt = personaldata.training_certificates.filter(trainings_certificates='Basic Training')
		pscrb = personaldata.training_certificates.filter(trainings_certificates='Proficiency in Survival Craft and Recue Boat')
		aff = personaldata.training_certificates.filter(trainings_certificates='Advance Fire Fighting')
		mefa = personaldata.training_certificates.filter(trainings_certificates='Medical Emergency First Aid')
		meca = personaldata.training_certificates.filter(trainings_certificates='Medical Care')
		pfrb = personaldata.training_certificates.filter(trainings_certificates='Proficiency in Fast Rescue Boat')
		ssbt = personaldata.training_certificates.filter(trainings_certificates='Ship Simulator and Bridge Team Work')
		brm = personaldata.training_certificates.filter(trainings_certificates='Bridge Resource Management')
		btm = personaldata.training_certificates.filter(trainings_certificates='Bridge Team Management')
		btoc = personaldata.training_certificates.filter(trainings_certificates='Basic Training for Oil and Chemical Tanker Cargo Operations')
		sbff = personaldata.training_certificates.filter(trainings_certificates='Shore Based Fire Fighting')
		atot = personaldata.training_certificates.filter(trainings_certificates='Advance Training for Oil Tanker')
		atct = personaldata.training_certificates.filter(trainings_certificates='Advance Training for Chemical Tanker')
		inmarsat = personaldata.training_certificates.filter(trainings_certificates='International Maritime Satellite')
		gmdss = personaldata.training_certificates.filter(trainings_certificates='Global Maritime Distress and Safety System')
		padams = personaldata.training_certificates.filter(trainings_certificates='Prevention of Alcohol and Drug Abuse in the Maritime Sector')
		hazmat = personaldata.training_certificates.filter(trainings_certificates='Hazardous Material')
		cow_igs = personaldata.training_certificates.filter(trainings_certificates='Crude Oil Washing / Inert Gas System')
		ers_erm = personaldata.training_certificates.filter(trainings_certificates='Engine Room Simulator with Engine Room Management')
		srroc = personaldata.training_certificates.filter(trainings_certificates='Ship Restricted Radiotelephone Operator Course')
		framo = personaldata.training_certificates.filter(trainings_certificates='FRAMO')
		sos = personaldata.training_certificates.filter(trainings_certificates='Ship Security Officer')
		soc = personaldata.training_certificates.filter(trainings_certificates='Safety Officer Course')
		bwk_ewk = personaldata.training_certificates.filter(trainings_certificates='Deck Watch Keeping / Engine Watch Keeping')
		rsc = personaldata.training_certificates.filter(trainings_certificates='Radar Simulator Course')
		ism = personaldata.training_certificates.filter(trainings_certificates='International Safety Management')
		ssmep = personaldata.training_certificates.filter(trainings_certificates='Shipboard Managerial Skills Enhancement Program')
		acni = personaldata.training_certificates.filter(trainings_certificates='Accident and Near-miss Investigation')
		ssa_sdsd = personaldata.training_certificates.filter(trainings_certificates='Ship Security Awareness / Seafarers with Designated Security Duties')
		arpa_ropa = personaldata.training_certificates.filter(trainings_certificates='Radar Navigation / Radar Plotting and use of ARPA ROPA')
		ecdis_generic = personaldata.training_certificates.filter(trainings_certificates='Electronic Chart Display and Information System')
		mlc_deck = personaldata.training_certificates.filter(trainings_certificates='Management Level Course - Deck')
		marpol = personaldata.training_certificates.filter(trainings_certificates='Marine Pollution I-VI')
		mlc_engine = personaldata.training_certificates.filter(trainings_certificates='Management Level Course - Engine')
		ecdis_specific = personaldata.training_certificates.filter(trainings_certificates='Electronic Chart Display and Information System Specific')
		ship_vetting = personaldata.training_certificates.filter(trainings_certificates='Ship Vetting')
		ship_handling = personaldata.training_certificates.filter(trainings_certificates='Ship Handling')
		maritime_eng = personaldata.training_certificates.filter(trainings_certificates='Maritime Eng.')





		domain = request.scheme
		domain += "://"
		# returns domain name
		domain += request.META["HTTP_HOST"]
		media = domain+"/media/"
		picture = media+str(appdetails.picture)
		signature = media+str(appform.signatures)
		check = domain+"/static/img/check.jpg"
		uncheck = domain+"/static/img/uncheck.jpg"
		logo = domain+"/static/img/small_logo.png"



		template = "application_form/pdf-report.html"
		context_dict = { "appform":appform, "appdetails":appdetails, "personaldata":personaldata, "education":education, "emergency":emergency, "backgroundinfo":backgroundinfo, "certificatesdocuments":certificatesdocuments, "domain":domain, "picture":picture , "signature":signature, "check":check, "uncheck":uncheck, "logo":logo, "appsource":appsource, "cayman_islands": cayman_islands, "marshall_islands": marshall_islands, "liberia":liberia, "cyprus":cyprus, "singapore":singapore, "greek":greek, "cop_bt":cop_bt, "cop_btoc":cop_btoc, "cop_atot":cop_atot, "cop_atct":cop_atct, "cop_pfrb":cop_pfrb, "cop_aff":cop_aff, "cop_mefa":cop_mefa, "cop_meca":cop_meca, "cop_sso":cop_sso, "cop_pscrb":cop_pscrb, "cop_ssa_sdsd":cop_ssa_sdsd, "bt":bt, "pscrb":pscrb, "aff":aff, "mefa":mefa, "meca":meca, "pfrb":pfrb, "ssbt":ssbt, "brm":brm, "btm":btm, "btoc":btoc, "sbff":sbff, "atot":atot, "atct":atct, "inmarsat":inmarsat, "gmdss":gmdss, "padams":padams, "hazmat":hazmat, "cow_igs":cow_igs, "ers_erm":ers_erm, "srroc":srroc, "framo":framo, "sos":sos, "soc":soc, "bwk_ewk":bwk_ewk, "rsc":rsc, "ism":ism, "ssmep":ssmep, "acni":acni, "ssa_sdsd":ssa_sdsd, "arpa_ropa":arpa_ropa, "ecdis_generic":ecdis_generic, "mlc_deck":mlc_deck, "marpol":marpol, "mlc_engine":mlc_engine, "ecdis_specific":ecdis_specific, "ship_vetting":ship_vetting, "ship_handling":ship_handling, "maritime_eng":maritime_eng}
		return render_to_pdf_response(request, template, context_dict)
	else:
		raise Http404("System Error.")