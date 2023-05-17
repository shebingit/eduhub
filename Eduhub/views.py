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
    placement = placements.objects.all()
    return render(request, 'user/placement.html',{'placement':placement})

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


def shortTeamInternship(request):
    courses = course_details.objects.filter(type='1')
    course_points=courseinternship_details.objects.all()
    return render(request, 'user/shortTeamInternship.html',{'courses':courses,'course_points':course_points})

def Internship(request):
    courses = course_details.objects.filter(type='2')
    course_points=courseinternship_details.objects.all()
    return render(request, 'user/internship.html',{'courses':courses,'course_points':course_points})


def Course_full(request):
    courses = course_details.objects.filter(type='3')
    ojt = courojt_details.objects.all()
    ojtcourse_sub=courseinternship_details.objects.all()
    ojtpoints = courseojtPoints.objects.all()
    return render(request, 'user/coursefull.html',{'courses':courses,'ojt':ojt,'ojtcourse_sub':ojtcourse_sub,'ojtpoints':ojtpoints})
   


def RegisterForm(request):
    courses = course_details.objects.all()
    return render(request, 'user/registerform.html',{'courses':courses})

def EnquirForm(request):
    return render(request, 'user/enquirform.html')



def saveEnquiry(request):

    if request.method == 'POST':
        enq=Enroll()
        
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
     
        contactus(name = name, email = email, subject = subject, message = message).save()
        msg='We have recieved your mail, We will get back to you as soon as possible.'
        return render(request, 'user/contact.html',{'msg':msg})

    return redirect('ContactPage')


def enquery_save(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        place = request.POST['place']
        ph = request.POST['phno']
        message = request.POST['msg']
    
        Enquir(name = name, email = email,place = place, phone = ph, enq_msg = message).save()
        msg='We have recieved your mail, We will get back to you as soon as possible.'
        return render(request, 'user/enquirform.html',{'msg':msg})

    return redirect('EnquirForm')





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
            enrolls = Enroll.objects.filter(enq_date=date.today())
            enrolls_count= Enroll.objects.all().count()
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
        enrolls = Enroll.objects.filter(enq_date=date.today())
        enrolls_count= Enroll.objects.all().count()
        enquerys= Enquir.objects.filter(enq_date=date.today())
        enquerys_count= Enquir.objects.all().count()
      
        return render(request,'admin/DashboardHome.html',{'file_up_count':file_up_count,'enrolls':enrolls,'enrolls_count':enrolls_count,'enquerys':enquerys,'enquerys_count':enquerys_count})
    else:
        return redirect('login_page')
    


# =================== Course Add =====================

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
    
def Course_pageedit(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        courses = course_details.objects.get(id=pk)
        return render(request,'admin/CoursePageedit.html',{'courses':courses})
    else:
        return redirect('login_page')
    

    
def Course_edit_save(request,pk):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        if request.method=='POST':
                
                course=course_details.objects.get(id=pk)
                course.course_name = request.POST.get('cname')
                course.type = request.POST.get('ctype')
                course.description = request.POST.get('cdiscr')
                course.fee = request.POST.get('cfee')
                course.offer_head = request.POST.get('coffer_head')
                course.offer_fee = request.POST.get('coffer_fee')
                course.duration = request.POST.get('cduriation')
               

                if request.POST.get('cstart'):
                    course.start_date = request.POST.get('cstart')
                else:
                    course.start_date = course.start_date 

                if request.FILES.get('cimage'):
                    course.image = request.FILES.get('cimage')
                else:
                    course.image = course.image
                course.save()
                courses=course_details.objects.get(id=pk)

                msg='Course Edit Success !'
                return render(request,'admin/CoursePageedit.html',{'msg':msg,'courses':courses})
            
        else:
                msg='Course Error !'
                courses=course_details.objects.get(id=pk)
                return render(request,'admin/CoursePageedit.html',{'msg':msg,'courses':courses})

   

            
        
    else:
        return redirect('login_page')


def Course_Delete(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        course = course_details.objects.get(id=pk)
        course.delete()
        courses = course_details.objects.all()
        msg_delete='Course Deleted Success !'
        return render(request,'admin/CoursePage.html', {'msg_delete':msg_delete,'courses':courses})
    else:
        return redirect('login_page')
    

def Course_Details(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        courses = course_details.objects.get(id=pk)
        if courses.type == '3':
            course_ojt = courojt_details.objects.filter(course_id__id=pk)
            course_ojt_points = courseojtPoints.objects.all()
            return render(request,'admin/OJTcourseDetails.html', {'courses':courses,'course_ojt':course_ojt,'course_ojt_points':course_ojt_points})
        
        else:
            course_inter = courseinternship_details.objects.filter(course_id__id=pk)
            return render(request,'admin/CourseDetails.html', {'courses':courses,'course_inter':course_inter})
    else:
        return redirect('login_page')
    
def Courseinternship_save(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        
        courses = course_details.objects.get(id=pk)

        try:

            if request.method=='POST':
                
                course=courseinternship_details()
                course.course_id=courses
                course.course_points = request.POST['cinter_points']
                course.save()
                courses = course_details.objects.get(id=pk)
                course_inter = courseinternship_details.objects.filter(course_id__id=pk)

                msg='Course Point added. !'
                return render(request,'admin/CourseDetails.html', {'msg':msg,'courses':courses,'course_inter':course_inter})
            
            else:
                course_inter = courseinternship_details.objects.filter(course_id=pk)
                return render(request,'admin/CourseDetails.html',{'courses':courses,'course_inter':course_inter})
        except:
            error_value=1
    else:
        return redirect('login_page')
    
    

def Coursepoint_edit(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        
        course_inter = courseinternship_details.objects.get(id=pk)
        courses = course_details.objects.get(id=course_inter.course_id.id)

        return render(request,'admin/CourseDetailspointsEdit.html', {'courses':courses,'course_inter':course_inter})
    else:
        return redirect('login_page')
    

def Courseinternship_edit_save(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        
        if request.method=='POST':
                
                course=courseinternship_details.objects.get(id=pk)
                course.course_points = request.POST.get('cinter_points')
                course.save()
                cid=course.course_id.id
                return redirect('Course_Details',cid)

    else:
        return redirect('login_page')
    
    
def Coursepoint_delete(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        course_points = courseinternship_details.objects.get(id=pk)
        cid=course_points.course_id.id
        course_points.delete()
        return redirect('Course_Details',cid)
        
        
    else:
        return redirect('login_page')
    


# =============== Ojt Course Section ================

def Courseojt_save(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        
        courses = course_details.objects.get(id=pk)
        course_ojt_points = courseojtPoints.objects.all()

        try:

            if request.method=='POST':
                
                ojt=courojt_details()
                ojt.course_id=courses
                ojt.course_subhead = request.POST['ojtsub_head']
                ojt.course_subetails = request.POST['ojtsub_disc']
                ojt.save()
                courses = course_details.objects.get(id=pk)
                course_ojt = courojt_details.objects.filter(course_id__id=pk)
              

                msg='Course Sub Details added. !'
                return render(request,'admin/OJTcourseDetails.html', {'msg':msg,'courses':courses,'course_ojt':course_ojt,'course_ojt_points':course_ojt_points})
            
            else:
                course_inter = courseinternship_details.objects.filter(course_id=pk)
                return render(request,'admin/OJTcourseDetails.html',{'courses':courses,'course_inter':course_inter,'course_ojt_points':course_ojt_points})
        except:
            error_value=1
    else:
        return redirect('login_page')
    
    
def ojtpoints_page(request,pk):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
       
        course_ojt = courojt_details.objects.get(id=pk)
        courses = course_details.objects.get(id=course_ojt.course_id.id)
        try:
            course_ojt_points = courseojtPoints.objects.filter(courseojt_id__id=pk)
        except courseojtPoints.DoesNotExist:
            course_ojt_points=None
        return render(request,'admin/OJTcourseDetailspoints.html', {'courses':courses,'course_ojt':course_ojt,'course_ojt_points':course_ojt_points})
         
    else:
        return redirect('login_page')
    
    
def Ojt_save(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        
        course_ojt = courojt_details.objects.get(id=pk)
        courses = course_details.objects.get(id=course_ojt.course_id.id)

        try:

            if request.method=='POST':
                
                ojtpoint=courseojtPoints()
                ojtpoint.courseojt_id=course_ojt
                ojtpoint.courseojt_points = request.POST['ojt_points']
                ojtpoint.save()

                course_ojt_points = courseojtPoints.objects.filter(courseojt_id__id=pk)
                msg='OJT Course Point added. !'
                return render(request,'admin/OJTcourseDetailspoints.html', {'msg':msg,'courses':courses,'course_ojt':course_ojt,'course_ojt_points':course_ojt_points})
                
               
            else:
               return('Course_page')
        except:
            error_value=1
    else:
        return redirect('login_page')
    


def ojtsubcontent_edit(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        course_ojt = courojt_details.objects.get(id=pk)
        courses = course_details.objects.get(id=course_ojt.id)
       
        return render(request,'admin/OJTcourseDetailsedit.html', {'courses':courses,'course_ojt':course_ojt})
        
    else:
        return redirect('login_page')
    

def Courseojtedit_save(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        
        ojt=courojt_details.objects.get(id=pk)
        cid=ojt.course_id.id

        if request.method=='POST':
                
                ojt=courojt_details.objects.get(id=pk)
                ojt.course_subhead = request.POST.get('ojtsub_head')
                ojt.course_subetails = request.POST.get('ojtsub_disc')
                ojt.save()
                return redirect('Course_Details',cid)

        else:
            return redirect('Course_Details',cid)
  
    else:
        return redirect('login_page')
    


def ojtsubcontent_remove(request,pk):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
       
        course_ojt = courojt_details.objects.get(id=pk)
        cid=course_ojt.course_id.id
        course_ojt.delete()
        return redirect('Course_Details',cid)
         
    else:
        return redirect('login_page')
    

def ojtpoints_edit(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        ojtpoint=courseojtPoints.objects.get(id=pk)
        ojtsub=courojt_details.objects.get(id=ojtpoint.courseojt_id.id)
        return render(request,'admin/OJTpoints_edit.html',{'ojtpoint':ojtpoint,'ojtsub':ojtsub})
            
    else:
        return redirect('login_page')



def ojtpoints_edit_save(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        
        course_ojt_point=courseojtPoints.objects.get(id=pk)
      


        if request.method =='POST':
           
            course_ojt_point.courseojt_points =request.POST['ojt_point']
            course_ojt_point.save()
               
            return redirect('Course_page')
               
        else:
            return redirect('Course_page')
        
    else:
        return redirect('login_page')


def ojtpoints_remove(request,pk):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
       
        course_ojt_point = courseojtPoints.objects.get(id=pk)
        cid=course_ojt_point.courseojt_id.course_id.id
        course_ojt_point.delete()
        return redirect('Course_Details',cid)
         
    else:
        return redirect('login_page')
    
    

# =================== Instructor Section =======================

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
    
 
def instuctor_edit(request,pk):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        instrs = instructors.objects.get(id=pk)

        return render(request,'admin/InstructorPageedit.html', {'instrs':instrs})
    else:
        return redirect('login_page')
    

def Instructoredit_save(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        instrs = instructors.objects.all()
        try:

            if request.method=='POST':
                
                instr=instructors.objects.get(id=pk)
                instr.name = request.POST.get('instname')
                instr.designation = request.POST.get('instdesig')
                instr.description = request.POST.get('instdiscr')

                if request.FILES.get('instimage'):

                    instr.image = request.FILES.get('instimage')
                else:
                      instr.image = instr.image 
                instr.save()
              

                msg='Instructor edit Success !'
                return render(request,'admin/InstructorPage.html', {'msg':msg,'instrs':instrs})
            
            else:
                return render(request,'admin/InstructorPage.html',{'instrs':instrs})
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
    


# =================== Placements Section =======================


def Placementpage(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        placement = placements.objects.all()
        return render(request,'admin/Placements.html',{'placement':placement})
    else:
        return redirect('login_page')
    

def Placement_save(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        try:

            if request.method=='POST':
                
                pla=placements()
                pla.name = request.POST['planame']
                pla.company = request.POST['placompny']
                pla.desig = request.POST['pladesig']
                pla.plyear = request.POST['playear']
                
                pla.image = request.FILES.get('plaimage')
                pla.save()
                placement = placements.objects.all()

                msg='Placement added Success !'
                return render(request,'admin/Placements.html', {'msg':msg,'placement':placement})
            
            else:
                return render(request,'admin/Placements.html')
        except:
            error_value=1
            return render(request,'admin/Placements.html')
    else:
        return redirect('login_page')
    

def Placementpageedit(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        placement = placements.objects.get(id=pk)
        return render(request,'admin/Placementsedit.html',{'placement':placement})
    else:
        return redirect('login_page')
    
    

def Placementedit_save(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        try:

            if request.method=='POST':
                
                pla=placements.objects.get(id=pk)
                pla.name = request.POST.get('planame')
                pla.company = request.POST.get('placompny')
                pla.desig = request.POST.get('pladesig')
                pla.plyear = request.POST.get('playear')
                
                if request.FILES.get('plaimage'):
                    pla.image = request.FILES.get('plaimage')
                else:
                     pla.image = pla.image
                pla.save()
                placement = placements.objects.all()

                msg='Placement edit Success !'
                return render(request,'admin/Placements.html', {'msg':msg,'placement':placement})
            
            else:
                return render(request,'admin/Placements.html')
        except:
            error_value=1
            return render(request,'admin/Placements.html')
    else:
        return redirect('login_page')
    

        
def Placement_remove(request,pk):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        instrs = placements.objects.get(id=pk)
        instrs.delete()
        msg_delete='placement Deleted Success !'
        placement = placements.objects.all()
    
        return render(request,'admin/InstructorPage.html', {'msg_delete':msg_delete,'placement':placement})
    else:
        return redirect('login_page')
    

# =================== Testimonial Section ======================= 

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
    
    
def Testimonial_edit(request,pk):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        testims = testimonial.objects.get(id=pk)
        return render(request,'admin/TestimonialPageedit.html',{'testims':testims})
    else:
        return redirect('login_page')
    

    
def Testimonial_edit_save(request,pk):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        try:

            if request.method=='POST':
                
                testim=testimonial.objects.get(id=pk)
                testim.name = request.POST.get('testname')
                testim.profession = request.POST.get('testprof')
                testim.company = request.POST.get('testcomp')
                testim.description = request.POST.get('testdiscr')
                
                if request.FILES.get('testimage'):
                    testim.image = request.FILES.get('testimage')
                else:
                     testim.image = testim.image
                testim.save()
                testims = testimonial.objects.all()

                msg='Testimonial edit Success !'
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
        enqs= Enroll.objects.filter(course__in=couse).order_by('-id')
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
        enqs= Enroll.objects.filter(course__in=couse).order_by('-id')
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
        enqs= Enroll.objects.filter(course__in=couse).order_by('-id')
        return render(request,'admin/sti.html', {'enqs':enqs})
    else:
        return redirect('login_page')
    


#================== Enroll section ================================

def enroll_view(request):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        enqs= Enroll.objects.all().order_by('-id')
        return render(request,'admin/Enroll.html', {'enqs':enqs})
    else:
        return redirect('login_page')
    

def enroll_remove(request,pk):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        try:
           
            enqs = Enroll.objects.get(id=pk)
            enqs.delete()
            confirm_msg='Enquery Removed'

        except Enroll.DoesNotExist:
            confirm_msg='No data found.'
        enqs= Enroll.objects.all().order_by('-id')
        return render(request,'admin/Enroll.html', {'enqs':enqs,'confirm_msg':confirm_msg})
    else:
        return redirect('login_page')


def enroll_update(request,pk):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        enqs= Enroll.objects.get(id=pk)
        enqs.enq_status=1
        enqs.save()
        confirm_msg='Enquery Updated'
        enqs= Enroll.objects.all().order_by('-id')
        return render(request,'admin/Enquiry.html', {'enqs':enqs,'confirm_msg':confirm_msg})
    else:
        return redirect('login_page')
    


#================ Enquiry Section =========================


def enquery_view(request):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        enqs= Enquir.objects.all().order_by('-id')
        return render(request,'admin/Enquiry.html', {'enqs':enqs})
    else:
        return redirect('login_page')
    

def enquery_upadte(request,pk):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        enq=Enquir.objects.get(id=pk)
        enq.enq_status=1
        enq.save()
        enqs= Enquir.objects.all().order_by('-id')
        return render(request,'admin/Enquiry.html', {'enqs':enqs})
    else:
        return redirect('login_page')
    

def enquery_remove(request,pk):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        enq=Enquir.objects.get(id=pk)
        enq.delete()
        enqs= Enquir.objects.all().order_by('-id')
        return render(request,'admin/Enquiry.html', {'enqs':enqs})
    else:
        return redirect('login_page')

    

def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    
    return redirect('HomePage')






