from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from .models import *
from datetime import date


# 404 page

def View_404Page(request, exception):
    return render(request, 'user/404.html', status=404)


# User section 

def HomePage(request):
    courses = course_details.objects.filter(active_status='0')
    instrs = instructors.objects.all()
    testims = testimonial.objects.all()
    offer= OfferBox.objects.all().first()
  
    return render(request, 'user/index.html',{'courses':courses,'instrs':instrs,'testims':testims,'offer':offer})

def AboutPage(request):
    instrs = instructors.objects.all()
    return render(request, 'user/about.html',{'instrs':instrs})

def CoursePage(request):
    courses = course_details.objects.filter(active_status='0')
    return render(request, 'user/course.html',{'courses':courses})

def CourseDetails(request,pk):
    courses = course_details.objects.get(id=pk)
    cid=courses.id
    ojt = courojt_details.objects.filter(course_id_id=cid)
    ojtpoints = courseojtPoints.objects.all()
    categ= Course_catgeorys.objects.filter(Cate_course_id_id=cid)
    return render(request, 'user/coursedetails.html',{'courses':courses,'ojt':ojt,'ojtpoints':ojtpoints,'categ':categ})

def PlacementPage(request):
    placement = placements.objects.all()
    return render(request, 'user/placement.html',{'placement':placement})

def EventsPage(request):
    eventsbox = events.objects.all().order_by('-id')
    gallery = gallerys.objects.all().order_by('-id')
    return render(request, 'user/events.html',{'eventsbox':eventsbox,'gallery':gallery})



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
    categ = Course_catgeorys.objects.filter(Type='1')
    courses = course_details.objects.filter(id__in=categ.values('Cate_course_id'))
    ojt = courojt_details.objects.all()
    ojtpoints = courseojtPoints.objects.all()
    return render(request, 'user/shortTeamInternship.html',{'courses':courses,'categ':categ,'ojt':ojt,'ojtpoints':ojtpoints})


def Internship(request):
    categ = Course_catgeorys.objects.filter(Type='2')
    courses = course_details.objects.filter(id__in=categ.values('Cate_course_id'))
    ojt = courojt_details.objects.all()

    ojtpoints = courseojtPoints.objects.all()
    return render(request, 'user/internship.html',{'courses':courses,'categ':categ,'ojt':ojt,'ojtpoints':ojtpoints})


def Course_full(request):
    categ = Course_catgeorys.objects.filter(Type='3')
    courses = course_details.objects.filter(id__in=categ.values('Cate_course_id'))
    ojt = courojt_details.objects.all()
    ojtpoints = courseojtPoints.objects.all()
    return render(request, 'user/coursefull.html',{'courses':courses,'categ':categ,'ojt':ojt,'ojtpoints':ojtpoints})
   


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
        enq.ctype = request.POST['join_course_type']
        enq.message = request.POST['join_message']
        enq.save()
        msg='We Appreciate Your Interest In Our Training Programme , Registration Successful '
        courses = course_details.objects.all()
        return render(request, 'user/registerform.html',{'courses':courses,'msg':msg})



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
            enquerys= Enquir.objects.filter(enq_date=date.today())
            enquerys_count= Enquir.objects.all().count()
      
            return render(request,'admin/DashboardHome.html',{'file_up_count':file_up_count,'enrolls':enrolls,'enrolls_count':enrolls_count,'enquerys':enquerys,'enquerys_count':enquerys_count})
        else:
            msg='Invalid Username or Password ! Try Again.'
            return render(request, 'user/login.html',{'msg':msg})
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
        coategs = Course_catgeorys.objects.all()
        return render(request,'admin/CoursePage.html',{'courses':courses,'coategs':coategs})
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
                course.description = request.POST['cdiscr']
                course.fee = request.POST['cfee']
                course.offer_head = request.POST['coffer_head']
                course.offer_fee = request.POST['coffer_fee']
                course.image = request.FILES.get('cimage')
                course.calttag = request.POST['coffer_fee']
                course.save()
                courses = course_details.objects.all()
                coategs = Course_catgeorys.objects.all()

                msg='Course added Success !'
                return render(request,'admin/CoursePage.html', {'msg':msg,'courses':courses,'coategs':coategs})
            
            else:
                return render(request,'admin/CoursePage.html')
        except:
            error_value=1
    else:
        return redirect('login_page')
    

def Course_active_deative(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        
        course = course_details.objects.get(id=pk)
        
        if course.active_status == '0' :
            course.active_status = 1
           
            course.save( )
            print(course.active_status)
          
        else :
            course.active_status = 0
            course.save()
            print(course.active_status)

        
        courses = course_details.objects.all()
        coategs = Course_catgeorys.objects.all()  
        return render(request,'admin/CoursePage.html', {'courses':courses,'coategs':coategs})
    else:
        return redirect('login_page')



def Course_catgeory(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        courses = course_details.objects.get(id=pk)
        coategs = Course_catgeorys.objects.filter(Cate_course_id=courses)
        return render(request,'admin/CourseCategory.html',{'courses':courses,'coategs':coategs})
    else:
        return redirect('login_page')
    

def Course_category_save(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        
        courses=course_details.objects.get(id=pk)

        try:

            if request.method=='POST':
                
                course=Course_catgeorys()
                course.Cate_course_id=courses
                course.Type = request.POST['ctype']
                course.Fee = request.POST['cfee']
                course.Offer_Head = request.POST['coffer_head']
                course.Offer_Fee = request.POST['coffer_fee']
                course.Duration = request.POST['cduriation']
                course.Start_date = request.POST['cstart']
                course.save()
                coategs = Course_catgeorys.objects.all()


                msg='Course Category added Success !'
                return render(request,'admin/CourseCategory.html', {'msg':msg,'courses':courses,'coategs':coategs})
            
            else:
                return render(request,'admin/CourseCategory.html')
        except:
            error_value=1
    else:
        return redirect('login_page')
    


def course_category_edit(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        coateg = Course_catgeorys.objects.get(id=pk)
        cid=coateg.Cate_course_id.id
        coategs = Course_catgeorys.objects.all()
        courses = course_details.objects.get(id=cid)
        return render(request,'admin/CourseCategory_edit.html',{'courses':courses,'coategs':coategs,'coateg':coateg})
    else:
        return redirect('login_page')
    
    


def Course_categoryedit_save(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')       

        if request.method=='POST':
                
                course=Course_catgeorys.objects.get(id=pk)
                course.Type = request.POST.get('ctype')
                course.Fee = request.POST.get('cfee')
                course.Offer_Head = request.POST.get('coffer_head')
                course.Offer_Fee = request.POST.get('coffer_fee')
                course.Duration = request.POST.get('cduriation')
                if request.POST.get('cstart'):
                    course.Start_date = request.POST.get('cstart')
                else:
                    course.Start_date = course.Start_date
                course.save()

                return redirect('Course_page')
            
        else:
                return render(request,'admin/CourseCategory.html')
    else:
        return redirect('login_page')
    


def course_category_remove(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        categ = Course_catgeorys.objects.get(id=pk)
        
        categ.delete()
        return redirect('Course_page')
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
                course.description = request.POST.get('cdiscr')
                course.fee = request.POST.get('cfee')
                course.offer_head = request.POST.get('coffer_head')
                course.offer_fee = request.POST.get('coffer_fee')

                if request.FILES.get('cimage'):
                    course.image = request.FILES.get('cimage')
                else:
                    course.image = course.image

                course.calttag = request.POST.get('calttag')

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
       
        course_ojt = courojt_details.objects.filter(course_id__id=pk)
        course_ojt_points = courseojtPoints.objects.all()
        return render(request,'admin/OJTcourseDetails.html', {'courses':courses,'course_ojt':course_ojt,'course_ojt_points':course_ojt_points})
        
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
               
                return render(request,'admin/OJTcourseDetails.html',{'courses':courses,'course_ojt_points':course_ojt_points})
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
                instr.instalttag = request.POST['instalt']
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
                instr.instalttag = request.POST.get('instalt')  
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
                pla.plaalttag = request.POST['plaalt'] 
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

                pla.plaalttag = request.POST.get('plaalt')      
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
                testim.testalttag = request.POST['testalt']
              
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
                testim.testalttag = request.POST.get('testalt')
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
        categ = Course_catgeorys.objects.filter(Type='1')
        couse=course_details.objects.filter(id__in=categ.values_list('Cate_course_id', flat=True))
        enqs= Enroll.objects.filter(course__in=couse).order_by('-id')
        print(enqs)
        return render(request,'admin/sti.html', {'enqs':enqs})
    else:
        return redirect('login_page')

def ojt_course(request):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
                return redirect('/')
        categ = Course_catgeorys.objects.filter(Type='3')
        couse=course_details.objects.filter(id__in=categ.values_list('Cate_course_id', flat=True))
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
        categ = Course_catgeorys.objects.filter(Type='2')
        couse=course_details.objects.filter(id__in=categ.values_list('Cate_course_id', flat=True))
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
    
    
def enroll_check(request,pk):
    
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        try:
           
            enqs = Enroll.objects.get(id=pk)
            confirm_msg='Data found.'
        except Enroll.DoesNotExist:
            confirm_msg='No data found.'
        return render(request,'admin/Enrollcheck.html', {'enqs':enqs,'confirm_msg':confirm_msg})
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
    

# ======== oFFERBox =============


def Offer_box(request):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        offer=OfferBox.objects.all().first()
        return render(request,'admin/Offerbox.html', {'offer':offer})
    else:
        return redirect('login_page')


def offer_save(request):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        
        if request.method == 'POST':

            if OfferBox.objects.all().first() :
                offer= OfferBox.objects.all().first() 
                offer.title_name= request.POST['offer_head']
                offer.offer_dics = request.POST['msg_disc']
                offer.save()
            else:
                offer = OfferBox()
                offer.title_name= request.POST['offer_head']
                offer.offer_dics = request.POST['msg_disc']
                offer.save()

            return render(request,'admin/Offerbox.html', {'offer':offer})
        else:
            return redirect('Offer_box')

    else:
        return redirect('login_page')
    

    
    
def status_change_offerbox(request):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        offer=OfferBox.objects.all().first()

        if offer.offer_status == '0':
            offer.offer_status = 1
        else:
            offer.offer_status = 0

        offer.save()
        return render(request,'admin/Offerbox.html', {'offer':offer})
    else:
        return redirect('login_page')
    


def Enroll_Candidate_Details(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        enroll_candidate = Enroll.objects.get(id=pk)
       
        categ_details = Course_catgeorys.objects.filter(Cate_course_id=enroll_candidate.course,Type=enroll_candidate.ctype)
       
        return render(request,'admin/Enroll_CandidateDetails.html',{'enroll_candidate':enroll_candidate,'categ_details':categ_details})
    else:
        return redirect('login_page')


# ======================== Gallery section ========================  

def GalPage(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        
        images=gallerys.objects.all()
        eventbox=events.objects.all()
        return render(request,'admin/Gallery_Images.html',{'images':images,'eventbox':eventbox})
    else:
        return redirect('login_page')

 # Image Save   

def Image_save(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        
        if request.method=='POST':
            evid= request.POST['evid']
            eventbox=events.objects.get(id=evid)
           
            for img in  request.FILES.getlist('images'):
                imgs=gallerys()
                imgs.event_id=eventbox
                imgs.img_tag = eventbox.event_type + '-' + eventbox.event_name
                imgs.images = img
                imgs.save()
            eventbox=events.objects.all()
            images=gallerys.objects.all()
            return render(request,'admin/Gallery_Images.html',{'images':images,'eventbox':eventbox})
    else:
        return redirect('login_page')

 # Image Edit    

def image_edit(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
       
        images=gallerys.objects.get(id=pk)
       
        return render(request,'admin/Gallery_Images_edit.html',{'images':images})
    
    else:
        return redirect('login_page')
    
#Image Edit Save



def Image_edit_save(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        
        if request.method=='POST':
            imgs=gallerys.objects.get(id=pk)

            if request.FILES.get('edit_images'):
                imgs.images = request.FILES.get('edit_images')
            else:
                imgs.images = imgs.images
            imgs.img_tag = request.POST.get('edit_img_tag')
            imgs.save()
            eventbox=events.objects.all()
            images=gallerys.objects.all()
            return render(request,'admin/Gallery_Images.html',{'images':images,'eventbox':eventbox})
    else:
        return redirect('login_page')
    
    
 # Image Remove    
def image_remove(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
       
        imgs=gallerys.objects.get(id=pk)
        imgs.delete()
        msg_delete='Image Deleted from DataBase.'
        images=gallerys.objects.all()
        eventbox=events.objects.all()
        return render(request,'admin/Gallery_Images.html',{'images':images,'msg_delete':msg_delete,'eventbox':eventbox})
    
    else:
        return redirect('login_page')
  
    

    

# ======================== Events section ========================  

def EvePage(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        eventbox=events.objects.all()
        return render(request,'admin/Events_Page.html',{'eventbox':eventbox})
    else:
        return redirect('login_page')
    
# Event Save
def event_save(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        if request.method=='POST':
            event=events()
            event.event_type =  request.POST['event_type']
            event.event_name =  request.POST['event_name']
            event.event_description =  request.POST['event_disc']
            event.event_link =  request.POST['event_link']
            event.event_image = request.FILES.get('event_post')
            event.event_tag = request.POST['event_name']
            event.save()
            eventbox=events.objects.all()
        return render(request,'admin/Events_Page.html',{'eventbox':eventbox})
    else:
        return redirect('login_page')
    

def event_edit(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        eventbox=events.objects.get(id=pk)
        return render(request,'admin/Events_Page_edit.html',{'eventbox':eventbox})
    else:
        return redirect('login_page')
    

def event_edit_save(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        event=events.objects.get(id=pk)
        event.event_type =  request.POST.get('event_type')
        event.event_name = request.POST.get('event_name')
        event.event_description =  request.POST.get('event_disc')
        event.event_link =  request.POST.get('event_link')

        if request.FILES.get('event_post'):
            event.event_image = request.FILES.get('event_post')
        else:
             event.event_image =  event.event_image 
             
        event.event_tag = request.POST.get('event_name')
        event.save()
        eventbox=events.objects.all()
        return render(request,'admin/Events_Page.html',{'eventbox':eventbox})
    else:
        return redirect('login_page')



def event_remove(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        event=events.objects.get(id=pk)
        event.delete()
        msg_delete='Image Deleted from DataBase.'
        eventbox=events.objects.all()
        return render(request,'admin/Events_Page.html',{'eventbox':eventbox,'msg_delete':msg_delete})
    else:
        return redirect('login_page')


#============ PASSWORD CHANGE ===============
def password_Change(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        users=User.objects.get(id=uid)
        return render(request,'admin/PasswordChange.html',{'users':users})
    else:
        return redirect('login_page')
    
def Password_changeSave(request,pk):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        if request.method == 'POST':
            psw=request.POST['psw']
            users=User.objects.get(id=pk)
            users.set_password(psw)
            users.save()
            msg='Password Changed.'
            return render(request,'admin/PasswordChange.html',{'users':users,'msg':msg})
    else:
        return redirect('login_page')


    

def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    
    return redirect('HomePage')






