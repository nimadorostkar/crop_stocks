from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.dispatch import receiver
from django.db import models
import uuid




#------------------------------------------------------------------------------
class Submitted_files(models.Model):
    user = models.ManyToManyField(User)
    title = models.CharField(max_length=200,null=True, blank=True,verbose_name = " عنوان ")
    file = models.FileField(upload_to='user_uploads/files',null=True, blank=True,verbose_name = "فایل های ارسال شده")
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    class Meta:
        verbose_name = "فایل ارسال شده"
        verbose_name_plural = "فایل های ارسال شده"

    def __str__(self):
        return self.title



#------------------------------------------------------------------------------
class Notice(models.Model):
    user = models.ManyToManyField(User)
    title = models.CharField(max_length=200,null=True, blank=True,verbose_name = " عنوان ")
    content = models.TextField(null=True, blank=True,verbose_name = " متن ")
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    class Meta:
        verbose_name = "اعلان"
        verbose_name_plural = " اعلانات "

    def __str__(self):
        return self.title



#------------------------------------------------------------------------------
class Money_req(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name = "کاربر")
    req_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount =  models.CharField(max_length=500,null=True, blank=True,verbose_name = "مقدار به تومان")
    descriptions = models.CharField(max_length=300,null=True, blank=True,verbose_name = "توضیحات")
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)


    def user_name(self):
          return str(self.user)

    class Meta:
        ordering = ['-created_on']

    class Meta:
        verbose_name = "درخواست پول"
        verbose_name_plural = " درخواست های پول "

    def __str__(self):
        return str(self.created_on)







#------------------------------------------------------------------------------
class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name = "کاربر")
    ticket_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=300,null=True, blank=True,verbose_name = " عنوان ")
    descriptions = models.TextField(max_length=800,null=True, blank=True,verbose_name = "توضیحات")
    CHOICES1 = ( ('تیکت','تیکت'), ('پاسخ','پاسخ') )
    status = models.CharField(max_length=20,choices=CHOICES1,default='تیکت',verbose_name = "وضعیت")
    CHOICES2 = ( ('🔴New','🔴New'), ('Answered','Answered') )
    case = models.CharField(max_length=20,choices=CHOICES2,default='🔴New',verbose_name = "حالت")
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    def user_name(self):
          return str(self.user)

    class Meta:
        ordering = ['-created_on']

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = " Tickets "

    def __str__(self):
        return str(self.created_on)




#------------------------------------------------------------------------------
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name = "کاربر")
    descriptions = models.CharField(max_length=300,null=True, blank=True,verbose_name = "توضیحات")
    photo=models.ImageField(upload_to='user_uploads/payments',default='user_uploads/payments/default.png',null=True, blank=True,verbose_name = " تصویر فیش بانکی")
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)


    def image_tag(self):
          return format_html("<img width=50 src='{}'>".format(self.photo.url))

    def user_name(self):
          return str(self.user)

    class Meta:
        ordering = ['-created_on']

    class Meta:
        verbose_name = "پرداخت"
        verbose_name_plural = " پرداخت ها "

    def __str__(self):
        return str(self.created_on)



#------------------------------------------------------------------------------
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True,related_name='profile',verbose_name = "کاربر")
  father_name = models.CharField(max_length=50,null=True, blank=True,verbose_name = " نام پدر  ")
  phone = models.CharField(max_length=50,null=True, blank=True,verbose_name = " شماره تماس  ")
  identity_number = models.CharField(max_length=50,unique=True,null=True, blank=True,verbose_name = "شماره شناسنامه")
  national_code = models.CharField(max_length=50,unique=True,null=True, blank=True,verbose_name = " کد ملی ")
  address = models.CharField(max_length=250,null=True, blank=True,verbose_name = " آدرس  ")
  bank_name = models.CharField(max_length=50,null=True, blank=True,verbose_name = " نام بانک")
  account_holder = models.CharField(max_length=150,null=True, blank=True,verbose_name = " نام صاحب حساب ")
  cardـnumber = models.CharField(max_length=16,null=True, blank=True,verbose_name = " شماره کارت بانک  ")
  user_photo=models.ImageField(upload_to='user_uploads/user_photo',default='user_uploads/user_photo/default.png',null=True, blank=True,verbose_name = "تصویر کاربر")
  signature=models.ImageField(upload_to='user_uploads/signature',default='user_uploads/signature/default.png',null=True, blank=True,verbose_name = "امضاء")
  personalـphoto=models.ImageField(upload_to='user_uploads/personalـphoto',default='user_uploads/personalـphoto/default.png',null=True, blank=True,verbose_name = "عکس پرسنلی ۳*۴")


  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
      if created:
          Profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()


  def image_tag(self):
        return format_html("<img width=50 src='{}'>".format(self.user_photo.url))

  def user_name(self):
        return str(self.user)


  class Meta:
      verbose_name = "پروفایل"
      verbose_name_plural = " پروفایل ها "


  def __str__(self):
    return "پروفایل : " + str(self.user)












#------------------------------- Models End -----------------------------------
