from django.shortcuts import redirect, render

from .models import *

# Create your views here.

def form(request):
    if request.method == "POST":
        Scheme_name =request.POST.get('Scheme_name')
        tire_name = request.POST.get('tire-name')
        employers_name = request.POST.get('employers_name')
        enrolment_no = request.POST.get('enrolment_no')
        employer_address = request.POST.get('employer_address')
        branch = request.POST.get('branch')
        entry_date = request.POST.get('entry_date')
        employee_gender = request.POST.get('employee_gender')

        member_title = request.POST.get('member_title')
        surname = request.POST.get('surname')
        firstname = request.POST.get('firstname')
        othername = request.POST.get('othername')
        identification_number = request.POST.get('idnumber')
        marital_status = request.POST.get('marital_status')
        identification_type = request.POST.get('idtype')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        age = request.POST.get('age')
        placeofbirth = request.POST.get('placeofbirth')
        region = request.POST.get('region')
        district = request.POST.get('district')
        town = request.POST.get('town')
        residential_address = request.POST.get('residential_address')
        postal_address = request.POST.get('postal_address')
        telephone_number = request.POST.get('telephone_number')
        work_number = request.POST.get('work_number')
        employer_address1 = request.POST.get('employer_address1')
        employer_gender = request.POST.get('employer_gender')
        fathers_name = request.POST.get('fathers_name')
        fathers_address = request.POST.get('fathers_address')
        mothers_name = request.POST.get('mothers_name')
        mothers_address = request.POST.get('mothers_address')
        ssnit_number = request.POST.get('ssnit_number')
        date_of_entry = request.POST.get('date_of_entry')

        trustee_title = request.POST.get('trustee_title')
        member_name = request.POST.get('member_name')
        employee_number = request.POST.get('employee_number')
        employer_name = request.POST.get('employer_name')
        employer_branch = request.POST.get('employer_branch')

        dependant_surname = request.POST.get('depndant_surname')
        dependant_firstname = request.POST.get('dependant_firstname')
        dependant_gender = request.POST.get('dependant_gender')
        dependant_dob = request.POST.get('dependant_dob')
        percentage_benefit = request.POST.get('percentage_benefit')
        relationship = request.POST.get('relationship')

        dependant_surname1 = request.POST.get('depndant_surname1')
        dependant_firstname1 = request.POST.get('dependant_firstname1')
        dependant_gender1 = request.POST.get('dependant_gender1')
        dependant_dob1 = request.POST.get('dependant_dob1')
        percentage_benefit1 = request.POST.get('percentage_benefit1')
        relationship1 = request.POST.get('relationship1')

        dependant_surname2 = request.POST.get('depndant_surname2')
        dependant_firstname2 = request.POST.get('dependant_firstname2')
        dependant_gender2 = request.POST.get('dependant_gender2')
        dependant_dob2 = request.POST.get('dependant_dob2')
        percentage_benefit2 = request.POST.get('percentage_benefit2')
        relationship2 = request.POST.get('relationship2')
        
        dependant_surname3 = request.POST.get('depndant_surname3')
        dependant_firstname3 = request.POST.get('dependant_firstname3')
        dependant_gender3 = request.POST.get('dependant_gender3')
        dependant_dob3 = request.POST.get('dependant_dob3')
        percentage_benefit3 = request.POST.get('percentage_benefit3')
        relationship3 = request.POST.get('relationship3')

        dependant_surname4 = request.POST.get('depndant_surname4')
        dependant_firstname4 = request.POST.get('dependant_firstname4')
        dependant_gender4 = request.POST.get('dependant_gender4')
        dependant_dob4 = request.POST.get('dependant_dob4')
        percentage_benefit4 = request.POST.get('percentage_benefit4')
        relationship4 = request.POST.get('relationship4')

        Details.objects.create(
            Scheme_name = Scheme_name,
            tire_name = tire_name,
            employers_name = employers_name,
            enrolment_no = enrolment_no,
            employer_address = employer_address,
            branch = branch,
            entry_date = entry_date,
            employee_gender = employee_gender,
            member_title = member_title,
            surname = surname,
            firstname = firsname,
            othername = othername,
            identification_number = identification_number,
            identification_type = identification_type,
            marital_status = marital_status,
            gender = gender,
            date_of_birth = date_of_birth,
            age = age,
            placeofbirth = placeofbirth,
            region = region,
            district = district,
            town = town,
            residential_address = residential_address,
            postal_address = postal_address,
            telephone_number = telephone_number,
            work_number = work_number,
            employer_address1 = employer_address1,
            employer_gender = employer_gender,
            fathers_name = fathers_name,
            fathers_address = fathers_address,
            mothers_name = mothers_name,
            mothers_address = mothers_address,
            ssnit_number = ssnit_number,
            date_of_entry = date_of_entry,
            trustee_title = trustee_title,
            member_name = member_name,
            employee_number = employee_number,
            employer_branch = employer_branch,
            employer_name = employer_name,

            dependant_surname = dependant_surname,
            dependant_firstname = dependant_firstname,
            dependant_gender = dependant_gender,
            dependant_dob = dependant_dob,
            percentage_benefit = percentage_benefit,
            relationship = relationship,

            dependant_surname1 = dependant_surname1,
            dependant_firstname1 = dependant_firstname1,
            dependant_gender1 = dependant_gender1,
            dependant_dob1 = dependant_dob1,
            percentage_benefit1 = percentage_benefit1,
            relationship1 = relationship1,

            dependant_surname2 = dependant_surname2,
            dependant_firstname2 = dependant_firstname2,
            dependant_gender2 = dependant_gender2,
            dependant_dob2 = dependant_dob2,
            percentage_benefit2 = percentage_benefit2,
            relationship2 = relationship2,

            dependant_surname3 = dependant_surname3,
            dependant_firstname3 = dependant_firstname3,
            dependant_gender3 = dependant_gender3,
            dependant_dob3 = dependant_dob3,
            percentage_benefit3 = percentage_benefit3,
            relationship3 = relationship3,

            dependant_surname4 = dependant_surname4,
            dependant_firstname4 = dependant_firstname4,
            dependant_gender4 = dependant_gender4,
            dependant_dob4 = dependant_dob4,
            percentage_benefit4 = percentage_benefit4,
            relationship4 = relationship4,

        )

    return render(request, 'index.html', {})

def home(request):
    if request.method=="POST":
        ssnit_number = request.POST.get('SSNITNUMBER')
        form = Details.objects.filter(ssnit_number=ssnit_number)
        return render(request, 'index3.html', {'form': form})
    else:
        return render(request, 'index2.html')

def details(request, pk):
    if request.method=="POST":
        form = Details.objects.filter(ssnit_number=pk)
    return render(request, 'index3.html', {'form': form})