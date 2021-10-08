from django.db import models
from accounts.models import *

import json

class Uploadanswer(models.Model):
  schoolname = models.CharField(max_length=10)
  testname = models.CharField(max_length=20)
  grade = models.CharField(max_length=5,default='null')
  subject = models.CharField(max_length=5,default='null')
  examinfos = models.CharField(max_length=100,default='null')
  writer = models.CharField(max_length=5)
  date_upload = models.DateTimeField(verbose_name='date upload', auto_now_add=True,null=True)
  testrealname = models.CharField(max_length=30,default='')


  def __str__(self):
    return self.schoolname + self.grade + self.testname

class Uploaduseranswer(models.Model):
  testname = models.CharField(max_length=20)
  schoolname = models.CharField(max_length=10)
  username = models.CharField(max_length=5)
  grade = models.CharField(max_length=5)
  stu_ID = models.CharField(max_length=7)
  subject = models.CharField(max_length=5)
  result = models.IntegerField()
  wrong = models.CharField(max_length=50)
  date_upload = models.DateTimeField(verbose_name='date upload', auto_now_add=True,null=True)

  class Meta:
    ordering = ['result']

  def __str__(self):
    i = self.testname +' '+self.schoolname+' '+self.stu_ID+' '+self.username
    return i

class checkClass():
  def check(self,schoolname,grade,name,stu_ID,post,session):
    self.testinfos = session['testinfos']
    Answer = Uploadanswer.objects.get(
      schoolname=schoolname,
      grade=grade,
      subject=self.testinfos[1]
    )
    self.anslist = Answer.examinfos #답지 db에서 받을 것(schoolname,grade,testname 고려)
    self.anslist = self.anslist.split('/')
    self.anslist_ = []
    for obj in self.anslist :
      obj = obj.split(' ')
      self.anslist_.append(obj)
    del self.anslist_[0]
    print(self.anslist_)
    self.count = len(self.anslist_)
    self.panslist = []
    self.result = 0
    self.wronglist = ''
    for i in range(self.count) :
      self.panslist.append(post['examAnswer_'+str(i+1)])
    for i in self.anslist_ :
      print(self.panslist[int(i[0])-1], int(i[1]))
      if int(i[1]) == int(self.panslist[int(i[0])-1]) :
        print('정답')
        self.result += int(i[2])
      if int(i[1]) != int(self.panslist[int(i[0])-1]) :
        print('오답')
        self.wronglist = self.wronglist + ' ' + i[0]
    #결과 저장
    try:
      self.check = Uploaduseranswer.objects.get(
        schoolname=schoolname,
        username=name,
        grade=grade,
        stu_ID=stu_ID,
        subject=self.testinfos[1])
    except :
      print('none')

    if self.check is not None :
      self.uploader = Uploaduseranswer(
        testname=self.testinfos[0],
        schoolname=schoolname,
        username=name,
        grade=grade,
        stu_ID=stu_ID,
        subject=self.testinfos[1],
        result=self.result,
        wrong=self.wronglist
        )
      self.uploader.save()
    else :
      return '이미 결과가 존재합니다 관리자에게 문의하세요'

class rankClass():

  ranks = [4,11, 23, 40, 60, 77, 89, 96, 100]

  def rank(self,schoolname,grade,name,stu_ID,subject):
    self.result_list = list(Uploaduseranswer.objects.filter(
      schoolname=schoolname,
      grade=grade,
      subject=subject))
    self.useraccount = Account.objects.get(schoolname=schoolname,
                                           grade=grade,
                                           stu_ID=stu_ID,
                                           username=name)
    print(self.result_list)
    self.i = 1
    for self.g in self.result_list :
      # self.all_result += self.g.result
      if self.g.stu_ID == stu_ID and self.g.username == name :
        self.users = self.useraccount.grade.student_count
        self.cul = lambda x,y: round(y - self.users*(x/100))
        for i in range(len(rankClass.ranks)) :
          self.user_rank = self.i
          if self.cul(rankClass.ranks[i],self.user_rank) <= 0 :
            # self.grade = Gradegroup.objects.get(gradeset=self.useraccount.grade)
            self.subject = self.useraccount.grade.subjects.split('/')
            if subject in self.subject:
              try :
                self.res = json.loads(self.useraccount.sub_res)
              except :
                self.res = self.useraccount.sub_res
              self.res[subject] = i+1
              self.useraccount.sub_res = json.dumps(self.res)
              self.useraccount.save()

#            if subject == '수학':
#              self.useraccount.math_rank = i+1
#              self.useraccount.save()
#            if subject == '과학':
#              self.useraccount.sci_rank = i+1
#              self.useraccount.save()
#            if subject == '영어':
#              self.useraccount.eng_rank = i+1
#              self.useraccount.save()
#            if subject == '국어':
#              self.useraccount.kor_rank = i+1
#              self.useraccount.save()
#            if subject == '사회':
#              self.useraccount.soc_rank = i+1
#              self.useraccount.save()
#            if subject == '한국사':
#              self.useraccount.his_rank = i+1
#              self.useraccount.save()
            return self.i,i+1
      self.i += 1
    return '결과 없음'