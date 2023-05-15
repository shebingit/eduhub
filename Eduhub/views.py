from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from .models import *
from datetime import date



# User section 

def HomePage(request):
    courses = course_details.objects.all()
    instrs = instructors.objects.all()
    testims = testimonial.objects.all()
  
    return render(request, 'user/index.html',{'courses':courses,'instrs':instrs,'testims':testims})

def AboutPage(request):
    instrs = instructors.objects.all()
    return render(request, 'user/about.html',{'instrs':instrs})

def CoursePage(request):
    courses = course_details.objects.all()
    return render(request, 'user/course.html',{'courses':courses})

def PlacementPage(request):
    return render(request, 'user/placement.html')

def ContactPage(request):
    return render(request, 'user/contact.html')

def CarrerStart(request):
    return render(request, 'user/carrerstart.html')

def CarrerTransit(request):
    return render(request, 'user/carrertransit.html')

def BridgingGap(request):
    return render(request, 'user/bridginggap.html')

def CarrerRestart(request):
    return render(request, 'user/carrerrestart.html')


def RegisterForm(request):
    courses = course_details.objects.all()
    return render(request, 'user/registerform.html',{'courses':courses})


def saveEnquiry(request):

    if request.method == 'POST':
        enq=enquiry()
        
        enq.name = request.POST['join_name']
        enq.email = request.POST['join_email']
        enq.phone = request.POST['join_phone']
        enq.place = request.POST['join_place']
        enq.qualification = request.POST['join_qualific']
        enq.stream = request.POST['join_stream']
        enq.pasout_year = request.POST['join_passyear']
        enq.start_date = request.POST['join_sdate']
        enq.end_date = request.POST['join_edate']
        enq.expe = request.POST['join_exp']
        enq.expe_no = request.POST['join_expno']
        enq.designation = request.POST['join_desig']
        enq.course = course_details.objects.get(id=int(request.POST['join_course']))
        enq.message = request.POST['join_message']
        enq.save()

    return redirect('CoursePage')



def contactuss(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['msg']
        print(name)
    
        contactus(name = name, email = email, subject = subject, message = message).save()
        msg='We Recived your mail, We will get you soon as posible.'
        return render(request, 'user/contact.html',{'msg':msg})

    return redirect('/contact')







 # =================================== DashBoard ================================

def login_page(request):
    return render(request, 'user/login.html')


def loginadmin(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)
    
        
        if user is not None:
            request.session["uid"]=user.id
    
            auth.login(request,user)    
            file_up_count=course_details.objects.all().count
            enrolls = enquiry.objects.filter(enq_date=date.today())
            enrolls_count= enquiry.objects.all().count()
            return render(request,'admin/DashboardHome.html',{'file_up_count':file_up_count,'enrolls':enrolls,'enrolls_count':enrolls_count})
        else:
            messages.info(request, 'Invalid Username or Password. Try Again.')
            return redirect('login_page')
    else:
        return redirect('login_page')


def loginDashboard(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        file_up_count=course_details.objects.all().count
        enrolls = enquiry.objects.filter(enq_date=date.today())
        enrolls_count= enquiry.objects.all().count()
        # enquerys = enquiry.objects.filter(enq_date=date.today())
        return render(request,'admin/DashboardHome.html',{'file_up_count':file_up_count,'enrolls':enrolls,'enrolls_count':enrolls_count})
    else:
        return redirect('login_page')


def Course_page(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        courses = course_details.objects.all()
        return render(request,'admin/CoursePage.html',{'courses':courses})
    else:
        return redirect('login_page')


def Course_save(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')

        try:

            if request.method=='POST':
                
                course=course_details()
                course.course_name = request.POST['cname']
                course.type = request.POST['ctype']
                course.description = request.POST['cdiscr']
                course.fee = request.POST['cfee']
                course.offer_head = request.POST['coffer_head']
                course.offer_fee = request.POST['coffer_fee']
                course.duration = request.POST['cduriation']
                course.start_date = request.POST['cstart']
                course.image = request.FILES.get('cimage')
                course.save()
                courses = course_details.objects.all()

                msg='Course added Success !'
                return render(request,'admin/CoursePage.html', {'msg':msg,'courses':courses})
            
            else:
                return render(request,'admin/CoursePage.html')
        except:
            error_value=1
    else:
        return redirect('login_page')


def Course_Delete(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        courses = course_details.objects.all()
        msg_delete='Course Deleted Success !'
        return render(request,'admin/CoursePage.html', {'msg_delete':msg_delete,'courses':courses})
    else:
        return redirect('login_page')


def InstructorPage(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        instrs = instructors.objects.all()
        return render(request,'admin/InstructorPage.html',{'instrs':instrs})
    else:
        return redirect('login_page')

def Instructor_save(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        try:

            if request.method=='POST':
                
                instr=instructors()
                instr.name = request.POST['instname']
                instr.designation = request.POST['instdesig']
                instr.description = request.POST['instdiscr']
                
                instr.image = request.FILES.get('instimage')
                instr.save()
                instrs = instructors.objects.all()

                msg='Instructor added Success !'
                return render(request,'admin/InstructorPage.html', {'msg':msg,'instrs':instrs})
            
            else:
                return render(request,'admin/InstructorPage.html')
        except:
            error_value=1
            return render(request,'admin/InstructorPage.html')
    else:
        return redirect('login_page')
    
    
def instuctor_remove(request,pk):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        instrs = instructors.objects.get(id=pk)
        instrs.delete()
        msg_delete='Insrtuctor Deleted Success !'
        instrs = instructors.objects.all()
    
        return render(request,'admin/InstructorPage.html', {'msg_delete':msg_delete,'instrs':instrs})
    else:
        return redirect('login_page')



def TestimonialPage(request):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        testims = testimonial.objects.all()
        return render(request,'admin/TestimonialPage.html',{'testims':testims})
    else:
        return redirect('login_page')


def Testimonial_save(request):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        try:

            if request.method=='POST':
                
                testim=testimonial()
                testim.name = request.POST['testname']
                testim.profession = request.POST['testprof']
                testim.company = request.POST['testcomp']
                testim.description = request.POST['testdiscr']
                
                testim.image = request.FILES.get('testimage')
                testim.save()
                testims = testimonial.objects.all()

                msg='Testimonial added Success !'
                return render(request,'admin/TestimonialPage.html', {'msg':msg,'testims':testims})
            
            else:
                return render(request,'admin/TestimonialPage.html')
        except:
            error_value=1
            return render(request,'admin/TestimonialPage.html')
    else:
        return redirect('login_page')



def Testimonial_remove(request,pk):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        testims = testimonial.objects.get(id=pk)
        testims.delete()
        msg_delete='Testimonial Deleted Success !'
        testims = testimonial.objects.all()
    
        return render(request,'admin/TestimonialPage.html', {'msg_delete':msg_delete,'testims':testims})
    else:
        return redirect('login_page')




def inbox_view(request):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        inboxmsg = contactus.objects.all().order_by('-id')
        return render(request,'admin/MessageInbox.html', {'inboxmsg':inboxmsg})
    else:
        return redirect('login_page')


def inboxmsg_remove(request,pk):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        try:
            contactus.objects.get(id=pk)
            inboxmsg = contactus.objects.get(id=pk)
            inboxmsg.delete()
            confirm_msg='Message Removed'

        except contactus.DoesNotExist:
            confirm_msg='No data found.'
        inboxmsg = contactus.objects.all().order_by('-id')
    
        return render(request,'admin/MessageInbox.html', {'inboxmsg':inboxmsg,'confirm_msg':confirm_msg})
    else:
        return redirect('login_page')



def shot_course(request):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        couse=course_details.objects.filter(type='1')
        enqs= enquiry.objects.filter(course__in=couse).order_by('-id')
        return render(request,'admin/sti.html', {'enqs':enqs})
    else:
        return redirect('login_page')

def ojt_course(request):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
                return redirect('/')
        couse=course_details.objects.filter(type='3')
        enqs= enquiry.objects.filter(course__in=couse).order_by('-id')
        return render(request,'admin/sti.html', {'enqs':enqs})
    else:
        return redirect('login_page')
    

def internship_course(request):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        couse=course_details.objects.filter(type='2')
        enqs= enquiry.objects.filter(course__in=couse).order_by('-id')
        return render(request,'admin/sti.html', {'enqs':enqs})
    else:
        return redirect('login_page')



def enquery_view(request):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        enqs= enquiry.objects.all().order_by('-id')
        return render(request,'admin/Enquery.html', {'enqs':enqs})
    else:
        return redirect('login_page')
    

def enq_remove(request,pk):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        try:
            enquiry.objects.get(id=pk)
            enqs = enquiry.objects.get(id=pk)
            enqs.delete()
            confirm_msg='Enquery Removed'

        except enquiry.DoesNotExist:
            confirm_msg='No data found.'
        enqs= enquiry.objects.all().order_by('-id')
        return render(request,'admin/Enquery.html', {'enqs':enqs,'confirm_msg':confirm_msg})
    else:
        return redirect('login_page')


def enq_update(request,pk):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        enqs= enquiry.objects.get(id=pk)
        enqs.enq_status=1
        enqs.save()
        confirm_msg='Enquery Updated'
        enqs= enquiry.objects.all().order_by('-id')
        return render(request,'admin/Enquery.html', {'enqs':enqs,'confirm_msg':confirm_msg})
    else:
        return redirect('login_page')
    

def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    
    return redirect('HomePage')






