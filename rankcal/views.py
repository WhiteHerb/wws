from django.shortcuts import render
from .models import showRank

class rankcal :
  def main(request):
    name = request.user.username
    schoolname = request.user.schoolname
    grade = request.user.grade
    stu_ID = request.user.stu_ID
    obj = showRank()
    result = obj.rank(schoolname,grade,name,stu_ID)
    return render(request, 'rankcal/index.html', {'result':result})