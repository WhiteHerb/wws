from django.db import models
from django.contrib.postgres.fields import ArrayField

class Uploadanswer(models.Model):
  schoolname = models.CharField(max_length=10)
  testname = models.CharField(max_length=20)
  examinfos = ArrayField(models.IntegerField())
  writer = models.CharField(max_length=5)

  def __str__(self):
    return self.testname

class Uploaduseranswer(models.Model):
  testname = models.CharField(max_length=20)
  schoolname = models.CharField(max_length=10)
  username = models.CharField(max_length=5)
  grade = models.CharField(max_length=5)
  stu_ID = models.CharField(max_length=7)
  subject = models.CharField(max_length=5)
  result = models.IntegerField()
  wrong = ArrayField(models.IntegerField())

  def __str__(self):
    i = self.testname +' '+self.schoolname+' '+self.stu_ID+' '+self.username
    return i

class checkClass():
  def check(self,schoolname,grade,name,stu_ID,subject,post,session):
    Answer = Uploadanswer.objects.get(
      schoolname=schoolname,
      grade=grade,
      subject=subject
    )
    self.anslist = Answer.examinfos #답지 db에서 받을 것(schoolname,grade,testname 고려)
    self.count = len(self.anslist)
    self.panslist = []
    self.result = 0
    self.wronglist = []
    for i in self.range(self.count) :
      self.panslist.append(post['answer_'+str(i)])
    for i in self.anslist :
      if i[1] == self.panslist[i[0]] :
        self.result += i[2]
      else : 
        self.wronglist.append(i[0])
    #답지 저장
    self.testinfos = session['testinfos']
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

class rankClass():
  def rank(self,schoolname,grade,name,stu_ID,subject):
    result_class = Uploaduseranswer()
    result_list = result_class.objests.get(
      schoolname=schoolname,
      grade=grade,
      subject=subject)
    print(result_list)
    result_list = result_list.order_by('result')
    for g in result_list :
      if g.stu_ID == stu_ID and g.name == name :
        return g
    return '결과 없음'