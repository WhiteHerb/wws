from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


class Schoolgroup(models.Model):
  schoolnameset = models.CharField(max_length=15,primary_key=True)

  def __str__(self):
    return self.schoolnameset

class Gradegroup(models.Model):
  student_count = models.IntegerField(default=0)
  subjects = models.CharField(max_length=100,default='')
  gradeset = models.IntegerField(default=0)
  school = models.ForeignKey('Schoolgroup',on_delete=models.CASCADE,related_name='school',db_column="school_id",default='')


  def __str__(self):
    return str(self.gradeset)+str(self.school)

class MyAccountManager(BaseUserManager):
  def create_user(self,email,username,schoolname,grade,stu_ID,password=None):
    if not email :
      raise ValueError('Users must have an email addrass')
    if not username :
      raise ValueError('User must have an username')
    
    user = self.model(
      email = self.normalize_email(email),
      username = username,
      schoolname = Schoolgroup.objects.get(schoolnameset=schoolname),
      grade_id = Gradegroup.objects.get(gradeset=grade),
      stu_ID = stu_ID,
    )

    user.set_password(password)
    user.save(using=self._db)

    return user
  
  def create_superuser(self,email,username,schoolname,grade,stu_ID,password=None):
    if not email :
      raise ValueError('Users must have an email addrass')
    if not username :
      raise ValueError('User must have an username')
    
    user = self.model(
      email = self.normalize_email(email),
      username = username,
      schoolname = Schoolgroup.objects.get(schoolnameset=schoolname),
      grade = Gradegroup.objects.get(gradeset=grade),
      stu_ID = stu_ID,
      is_admin = True,
      is_superuser = True,
      is_active = True,
      is_staff = True,
    )

    user.set_password(password)
    user.save(using=self._db)

    return user


class Account(AbstractUser,PermissionsMixin) :
  email = models.EmailField(verbose_name='email',max_length=80,unique=True)
  username = models.CharField(max_length=30)
  schoolname = models.ForeignKey('Schoolgroup',on_delete=models.CASCADE,related_name='schoolname',db_column="schoolname_id")
  grade = models.ForeignKey('Gradegroup',on_delete=models.CASCADE,related_name='grade', db_column="grade_id")
  stu_ID = models.CharField(max_length=5, unique=True)
  sub_res = models.JSONField(default={})
  userrank = models.IntegerField(default=0)


  date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
  last_login = models.DateTimeField(verbose_name='last login',auto_now=True)
  is_admin = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS=['username','schoolname','grade','stu_ID',]

  objects = MyAccountManager()

  def __str__(self):
    return self.username

  def has_perm(self, perm, odj=None):
    return self.is_admin
  
  def has_module_perms(self,app_label):
    return True