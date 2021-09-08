from django.db import models
from rater.models import rankClass

subject = ['수학','과학','영어','사회','한국사','국어']
sub_rank = [8,8,8,8,6,8]

class rankdata(models.Model):
  name = models.CharField(max_length=5)
  personalRank = models.IntegerField()


class showRank :
  def rank(self,schoolname,grade,name,stu_ID) :
    self.obj = rankClass()
    self.rank_result = 0
    for i in subject :
      try:
        self.rank = self.obj.rank(schoolname,grade,name,stu_ID,i)
      except:
        return '모든 과목을 체점해 주세요'
      self.rank_result += self.rank*sub_rank[i]
    self.rank_result = self.rank_result/46
    self.obj = rankClass(
      name=name,
      personalRank=self.rank_result
    )
    self.obj.save()
    return self.rank_result


      
