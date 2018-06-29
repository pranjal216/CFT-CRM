import logging
from django.shortcuts import render,HttpResponseRedirect,HttpResponse,reverse
from .models import Salary_calculations,CTC_breakdown
from .forms import SalaryForm,CtcForm
from django.contrib.auth import get_user_model
from django.contrib import messages

def salary(request):
    context=CTC_breakdown.objects.all()
    return render(request,'work/salary.html',{'context':context})
# def salary(request):
#     context=get_user_model().objects.all()
#     return render(request,'work/salary.html',{'context':context})

def edit_salary(request,id):
    if request.method == 'POST':
        # form = CtcForm(request.POST)
        # if form.is_valid():
        #     form.save()
        # else:
        #     print(form.errors)
        a=CTC_breakdown.objects.get(employee_id=id)
        if 'ctc' in request.POST:
            a.ctc= int(request.POST['ctc'])
        if 'given_bonus' in request.POST:
            a.given_bonus=int(request.POST['given_bonus'])
        a.save()
        return HttpResponseRedirect(reverse('salary_percentages:edit_salary',kwargs={'id' : id}))
    ctc_objects=CTC_breakdown.objects.get(employee_id=id)
    return render(request,'work/edit_salary.html',{'ctc_objects':ctc_objects})

def edit_ctc(request,id):
    form=CtcForm()
    return render(request,'work/edit_ctc.html',{'form':form,'request_id':id})

def edit_bonus(request,id):
    form=CtcForm()
    return render(request,'work/edit_bonus.html',{'form':form,'request_id':id})

def salary_structure(request):
    context = Salary_calculations.objects.all()
    return render(request,'work/salary_struct_table.html',{'context':context})

def add(request):
    if request.method=="POST":
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("salary_percentages:salary_structure"))
        else:
            return HttpResponse('Sorry! The salary_structure for this year has already been formed')
    else :
        form = SalaryForm()
        return render(request,'work/salary_struct_form.html',{'form':form})

def upload_csv(request):

    data={}
    if request.method=="GET":
        return render(request,'work/upload_csv.html',data)

    try:
        csv_file = request.FILES('csv_file')

        if not csv_file.name.endswith('.csv'):
            messages.error('Sorry!! This file is not csv type')
            return HttpResponseRedirect(reverse("salary_percentages:upload_csv"))

        if csv_file.multiple_chunks():
            messages.error("Uploaded file is too big(%.2f MB) " % (csv_file.size / (1000*1000)))
            return HttpResponseRedirect(reverse("salary_percentages:upload_csv"))

        file_data = csv_file.read().decode('utf-8')
        lines=file_data.split("\n")

        for line in lines:
            fields=line.split(",")

            data_dict = {}
            data_dict["financial_year"] = fields[0]
            data_dict["allowances"] = fields[1]
            data_dict["hra_percentage"] = fields[2]
            data_dict["ppf_percentage"] = fields[3]
            print(data_dict)
            salary_percentages = Salary_calculations(**data_dict)
            salary_percentages.save()

    except Exception as e:

        logging.getLogger("error_logger").error("Unable to upload file" + repr(e))
        return HttpResponseRedirect(reverse("salary_percetages:upload_csv"))




