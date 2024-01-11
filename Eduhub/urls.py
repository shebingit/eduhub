from django.urls import path 
from.import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('',views.HomePage,name='HomePage'),
    path('About',views.AboutPage,name='AboutPage'),
    path('Course',views.CoursePage,name='CoursePage'),
    path('Placement',views.PlacementPage,name='PlacementPage'),
    path('Events',views.EventsPage,name='EventsPage'),
    path('Contact',views.ContactPage,name='ContactPage'),
    path('Blog',views.BlogPage,name='BlogPage'),
    path('Course-Details/<pk>',views.CourseDetails,name='CourseDetails'),


    path('Short-Team-Internship',views.shortTeamInternship,name='shortTeamInternship'),
    path('Internship',views.Internship,name='Internship'),
    path('On-Job-Training',views.Course_full,name='Course_full'),
    

    path('Course-Register-Form',views.RegisterForm,name='RegisterForm'),
    path('Jumpstart-Your-IT-Career',views.CarrerStart,name='CarrerStart'),
    path('Transitioning-to-IT',views.CarrerTransit,name='CarrerTransit'),
    path('Bridging-the-Gap',views.BridgingGap,name='BridgingGap'),
    path('Restart-Your-IT-Career',views.CarrerRestart,name='CarrerRestart'),

    path('contact-us',views.contactuss,name='contactuss'),
    path('Join',views.saveEnquiry,name='saveEnquiry'),
    path('Enquiry-Form',views.EnquirForm,name='EnquirForm'),
    path('Enquiry-Send',views.enquery_save,name='enquery_save'),
    
    
    





        # ====================== Dashboard Section =======================
    
    path('login',views.login_page,name="login_page"),
    path('login-Check',views.loginadmin,name="loginadmin"),
    path('Dashboard',views.loginDashboard,name="loginDashboard"),

    path('Course-page',views.Course_page,name="Course_page"),
    path('Course-Save',views.Course_save,name="Course_save"),
    path('Course-active_deative/<pk>',views.Course_active_deative,name="Course_active_deative"),

    path('Course-Category/<pk>',views.Course_catgeory,name="Course_catgeory"),
    path('Course-Category-Save/<pk>',views.Course_category_save,name="Course_category_save"),
    path('Course-Category-Edit/<pk>',views.course_category_edit,name="course_category_edit"),
    path('Course-Category-Edit-Save/<pk>',views.Course_categoryedit_save,name="Course_categoryedit_save"),
    path('Course-Category-Remove/<pk>',views.course_category_remove,name="course_category_remove"),

    path('Course-Edit-Page/<pk>',views.Course_pageedit,name ="Course_pageedit"),
    path('Course-Edit-Save/<pk>',views.Course_edit_save,name ="Course_edit_save"),
    path('Course-Delete/<pk>',views.Course_Delete,name ="Course_Delete"),

    path('CourseDetails/<pk>',views.Course_Details,name ="Course_Details"),
   

    path('OJT-Details-Save/<pk>',views.Courseojt_save,name = "Courseojt_save"),
    path('OJT-Subcontent-Edit/<pk>',views.ojtsubcontent_edit,name = "ojtsubcontent_edit"),
    path('OJT-Subcontent-Edit-Save/<pk>',views.Courseojtedit_save,name = "Courseojtedit_save"),
    path('OJT-Subcontent-Remove/<pk>',views.ojtsubcontent_remove,name = "ojtsubcontent_remove"),
    path('OJT-Points/<pk>',views.ojtpoints_page,name = "ojtpoints_page"),
    path('OJT-Points-Save/<pk>',views.Ojt_save,name = "Ojt_save"),
     path('OJT-Points-Edit/<pk>',views.ojtpoints_edit,name = "ojtpoints_edit"),
    path('OJT-Points-Edit-Save/<pk>',views.ojtpoints_edit_save,name = "ojtpoints_edit_save"),
    path('OJT-Points-Remove/<pk>',views.ojtpoints_remove,name = "oojtpoints_remove"),
    
    
    

    path('Instructors',views.InstructorPage,name="InstructorPage"),
    path('Instructors-Save',views.Instructor_save,name="Instructor_save"),
    path('Instuctor-Edit/<pk>',views.instuctor_edit,name = "instuctor_edit"),
    path('Instuctor-Edit-Save/<pk>',views.Instructoredit_save,name = "Instructoredit_save"),
    path('Instuctor-Remove/<pk>',views.instuctor_remove,name = "instuctor_remove"),

    path('Placement-Page',views.Placementpage,name="Placementpage"),
    path('Placement-Save',views.Placement_save,name="Placement_save"),
    path('Placement-Edit/<pk>',views.Placementpageedit,name = "Placementpageedit"),
    path('Placement-Edit-Save/<pk>',views.Placementedit_save,name = "Placementedit_save"),
    path('Placement-Remove/<pk>',views.Placement_remove,name = "Placement_remove"),

    path('Testimonial-Page',views.TestimonialPage,name="TestimonialPage"),
    path('Testimonial-save',views.Testimonial_save,name="Testimonial_save"),
    path('Testimonial-Edit/<pk>',views.Testimonial_edit,name = "Testimonial_edit"),
    path('Testimonial-Edit-Save/<pk>',views.Testimonial_edit_save,name = "Testimonial_edit_save"),
    path('Testimonial-Remove/<pk>',views.Testimonial_remove,name = "Testimonial_remove"),
    
    path('Message-Inbox',views.inbox_view,name="inbox_view"),
    path('Inboxmsg-Remove/<pk>',views.inboxmsg_remove,name = "inboxmsg_remove"),
    path('Shot_course',views.shot_course,name="shot_course"),
    path('OJT_course',views.ojt_course,name="ojt_course"),
    path('Internship_course',views.internship_course,name="internship_course"),

    path('Enroll',views.enroll_view,name="enroll_view"),
    path('Enroll-Remove/<pk>',views.enroll_remove,name = "enroll_remove"),
    path('Enroll-Check/<pk>',views.enroll_check,name = "enroll_check"),
    path('Enroll-Update/<pk>',views.enroll_update,name = "enroll_update"),
    path('Enquiry-Candidate/<pk>',views.Enroll_Candidate_Details,name = "Enroll_Candidate_Details"),

    path('Enquiry',views.enquery_view,name="enquery_view"),
    path('Enquiry-Remove/<pk>',views.enquery_remove,name = "enquery_remove"),
    path('Enquiry-Update/<pk>',views.enquery_upadte,name = "enquery_upadte"),

    

    path('Offer-Box',views.Offer_box,name="Offer_box"),  
    path('Offer-Box-Save',views.offer_save,name="offer_save"),
    path('Offer-Change-Status',views.status_change_offerbox,name="status_change_offerbox"),

    path('Gallery-Image',views.GalPage,name="GalPage"),
    path('Gallery-Image-Save',views.Image_save,name="Image_save"), 
    path('Image-Edit/<pk>',views.image_edit,name = "image_edit"),
    path('Image-Save-Edit/<pk>',views.Image_edit_save,name = "Image_edit_save"),
    path('Image-Remove/<pk>',views.image_remove,name = "image_remove"),


    path('Events-Section',views.EvePage,name="EvePage"),
    path('Events-Save',views.event_save,name="event_save"),   
    path('Events-Edit/<pk>',views.event_edit,name = "event_edit"),
    path('Events-Edit-Save/<pk>',views.event_edit_save,name = "event_edit_save"),  
    path('Events-Remove/<pk>',views.event_remove,name = "event_remove"),
    
    
    #---- Blog Section --------------
    path('BlogListPage-Section',views.BlogListPage,name="BlogListPage"),
    path('BlogPage-Section',views.blog_page,name="blog_page"),
    path('Blog-Details/<pk>',views.blog_details,name="blog_details"),
    path('Blog-Edit/<pk>',views.blog_details_edit,name="blog_details_edit"),
    path('Blog-Remove/<pk>',views.blog_remove,name="blog_remove"),
    


    path('Password-Change',views.password_Change,name="password_Change"),
    path('Password-Change-Save/<pk>',views.Password_changeSave,name = "Password_changeSave"),
    path('logout',views.logout,name="logout"),

    
    
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



