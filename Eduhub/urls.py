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
    
 

    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
