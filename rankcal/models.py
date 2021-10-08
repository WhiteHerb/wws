from django.db import models
from rater.models import rankClass
from accounts.models import Account

class rankdata(models.Model):
  name = models.CharField(max_length=5)
  personalRank = models.IntegerField()


class showRank :
  def rank(self,schoolname,grade,name,stu_ID,email,sub_rank) :
    self.subints = {}
    self.user = Account.objects.get(email=email)
    self.subjects = self.user.grade.subjects.split('/')
    print(sub_rank)
    for a in range(len(self.subjects)):
      self.subints[self.subjects[a]] = sub_rank[a]
    self.obj = rankClass()
    self.rank_result = 0
    for i in self.subjects :
      try:
        self.rank = self.obj.rank(schoolname,grade,name,stu_ID,i)
      except:
        return '모든 과목을 체점해 주세요'
      print(type(self.rank_result))
      print(self.subints)
      self.rank_result += int(self.rank[0])*int(float(self.subints[i]))
    self.rank_result = int(self.rank_result)/self.user.grade.student_count
    self.user.userrank = self.rank_result
    self.user.save()
    return self.rank_result


      
