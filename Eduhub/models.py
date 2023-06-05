from django.db import models



class about_model(models.Model):
    video_file = models.FileField(upload_to='videos/',null= True)
    description = models.CharField(max_length=255,null=True,blank=True)

class course_details(models.Model):
    image = models.ImageField(null=True,blank = True,upload_to = 'img/courses')
    course_name = models.CharField(max_length=255, null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    offer_head=models.CharField(max_length=100,null=True,blank=True,default='')
    offer_fee =models.CharField(max_length=100,null=True,blank=True,default='')
    fee = models.CharField(max_length=100,null=True,blank=True,default='')
    calttag = models.TextField(null=True,blank=True,default='')  
    active_status = models.CharField(max_length=10,null=True,blank=True,default='0')

    


class Course_catgeorys(models.Model):
    Cate_course_id = models.ForeignKey(course_details, on_delete=models.CASCADE, null=True,default='')
    Type = models.CharField(max_length=50,null=True,blank=True)
    Offer_Head=models.CharField(max_length=100,null=True,blank=True,default='')
    Offer_Fee =models.CharField(max_length=100,null=True,blank=True,default='')
    Fee = models.CharField(max_length=100,null=True,blank=True,default='')
    Duration = models.CharField(max_length=100,null=True,blank=True)
    Start_date = models.DateField(null=True,blank=True)
    

class courojt_details(models.Model):
    course_id = models.ForeignKey(course_details, on_delete=models.CASCADE, null=True,default='')
    course_subhead =  models.CharField(max_length=255,null=True,blank=True)
    course_subetails = models.TextField(null=True,blank=True,default='')   

class courseojtPoints(models.Model):
    courseojt_id = models.ForeignKey(courojt_details, on_delete=models.CASCADE, null=True,default='')
    courseojt_points = models.TextField(null=True,blank=True,default='')



class instructors(models.Model):
    image = models.ImageField(null=True,blank = True,upload_to = 'img/instructors')
    name = models.CharField(max_length=255, null=True,blank=True)
    designation = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    instalttag = models.TextField(null=True,blank=True,default='')   

    
class placements(models.Model):
    image = models.ImageField(null=True,blank = True,upload_to = 'img/placement')
    name = models.CharField(max_length=255, null=True,blank=True)
    company = models.CharField(max_length=255,null=True,blank=True)
    desig = models.CharField(max_length=255,null=True,blank=True)
    plyear = models.CharField(max_length=255,null=True,blank=True)
    plaalttag = models.TextField(null=True,blank=True,default='')   


class testimonial(models.Model):
    image = models.ImageField(null=True,blank = True,upload_to = 'img/testimonial')
    name = models.CharField(max_length=255, null=True,blank=True)
    profession = models.CharField(max_length=255,null=True,blank=True)
    company = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    testalttag = models.TextField(null=True,blank=True,default='')   


class events(models.Model):
    event_image = models.ImageField(null=True,blank = True,upload_to = 'img/event')
    event_type = models.CharField(max_length=255, null=True,blank=True)
    event_name = models.CharField(max_length=255, null=True,blank=True)
    event_link = models.CharField(max_length=100,null=True,blank=True)
    event_description = models.TextField(null=True,blank=True,default='') 
    event_tag = models.TextField(null=True,blank=True,default='') 

class gallerys(models.Model):
    event_id = models.ForeignKey(events, on_delete=models.CASCADE, null=True,default='')
    images = models.ImageField(null=True,blank = True,upload_to = 'img/gallery')
    img_tag = models.TextField(null=True,blank=True,default='') 

    


class contactus(models.Model):

    name = models.CharField(max_length=255, null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    subject = models.CharField(max_length=255,null=True,blank=True)
    message = models.CharField(max_length=100,null=True,blank=True)
    msg_date = models.DateField(auto_now_add=True,blank=False,null=True)
    msg_status = models.CharField(max_length=50,null=True,default=0)


class Enroll(models.Model):
    name = models.CharField(max_length=255, null=True,blank=True,default='')
    email = models.CharField(max_length=255,null=True,blank=True,default='')
    phone = models.CharField(max_length=100,null=True,blank=True,default='')
    place = models.CharField(max_length=100,null=True,blank=True,default='')
    qualification = models.CharField(max_length=100,null=True,blank=True)
    stream = models.CharField(max_length=100,null=True,blank=True,default='')
    pasout_year = models.CharField(max_length=100,null=True,blank=True,default='')
    start_date = models.DateField(auto_now_add=False,blank=False,null=True,)
    end_date = models.DateField(auto_now_add=False,blank=False,null=True,)
    expe = models.CharField(max_length=100,null=True,blank=True,default='')
    expe_no = models.CharField(max_length=100,null=True,blank=True,default='')
    course = models.ForeignKey(course_details, on_delete=models.CASCADE, null=True,default='')
    ctype = models.CharField(max_length=25,null=True,blank=True,default='')
    message = models.CharField(max_length=255,null=True,blank=True,default='')
    designation = models.CharField(max_length=255,null=True,blank=True,default='')
    enq_status = models.CharField(max_length=50,null=True,default=0)
    enq_date = models.DateField(auto_now_add=True,blank=False,null=True)

class Enquir(models.Model):
    name = models.CharField(max_length=255, null=True,blank=True,default='')
    email = models.CharField(max_length=255,null=True,blank=True,default='')
    phone = models.CharField(max_length=100,null=True,blank=True,default='')
    place = models.CharField(max_length=100,null=True,blank=True,default='')
    enq_msg = models.TextField(null=True,blank=True,default='')
    enq_date = models.DateField(auto_now_add=True,blank=False,null=True)
    enq_status = models.CharField(max_length=50,null=True,blank=True,default='0')


class OfferBox(models.Model):
    title_name = models.CharField(max_length=255, null=True,blank=True,default='')
    offer_dics = models.TextField(null=True,blank=True,default='')
    offer_status = models.CharField(max_length=10, null=True,blank=True,default=0)