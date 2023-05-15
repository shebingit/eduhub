from django.urls import path 
from.import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('',views.HomePage,name='HomePage'),
    path('About',views.AboutPage,name='AboutPage'),
    path('Course',views.CoursePage,name='CoursePage'),
    path('Placement',views.PlacementPage,name='PlacementPage'),
    path('Contact',views.ContactPage,name='ContactPage'),

    path('Course-Register-Form',views.RegisterForm,name='RegisterForm'),
    path('Jumpstart-Your-IT-Career',views.CarrerStart,name='CarrerStart'),
    path('Transitioning-to-IT',views.CarrerTransit,name='CarrerTransit'),
    path('Bridging-the-Gap',views.BridgingGap,name='BridgingGap'),
    path('Restart-Your-IT-Career',views.CarrerRestart,name='CarrerRestart'),

    path('contact-us',views.contactuss,name='contactuss'),
    path('Join',views.saveEnquiry,name='saveEnquiry'),
    





        # ====================== Dashboard Section =======================
    
    path('login',views.login_page,name="login_page"),
    path('login-Check',views.loginadmin,name="loginadmin"),
    path('Dashboard',views.loginDashboard,name="loginDashboard"),

    path('Course-page',views.Course_page,name="Course_page"),
    path('Course-Save',views.Course_save,name="Course_save"),
    path('Course_Delete/<pk>',views.Course_Delete,name = "Course_Delete"),
    path('Instructors',views.InstructorPage,name="InstructorPage"),
    path('Instructors-Save',views.Instructor_save,name="Instructor_save"),
    path('Instuctor-Remove/<pk>',views.instuctor_remove,name = "instuctor_remove"),
    path('Testimonial-Page',views.TestimonialPage,name="TestimonialPage"),
    path('Testimonial-save',views.Testimonial_save,name="Testimonial_save"),
    path('Testimonial-Remove/<pk>',views.Testimonial_remove,name = "Testimonial_remove"),
    
    path('Message-Inbox',views.inbox_view,name="inbox_view"),
    path('Inboxmsg-Remove/<pk>',views.inboxmsg_remove,name = "inboxmsg_remove"),
    path('Shot_course',views.shot_course,name="shot_course"),
    path('OJT_course',views.ojt_course,name="ojt_course"),
    path('Internship_course',views.internship_course,name="internship_course"),
    path('Enquery',views.enquery_view,name="enquery_view"),
    path('Enquery-Remove/<pk>',views.enq_remove,name = "enq_remove"),
    path('Enquery-Update/<pk>',views.enq_update,name = "enq_update"),

    path('logout',views.logout,name="logout"),

    
    
    

    
    
 

    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
