from django.shortcuts import render
from .models import showRank

class rankcal :
  def backmain(request):
    subs = request.user.grade.subjects

    return render(request, 'rankcal/backmain.html', {'subs': subs})

  def main(request):
    name = request.user.username
    schoolname = request.user.schoolname
    grade = request.user.grade
    stu_ID = request.user.stu_ID
    useremail = request.user.email
    subint_list = request.GET['subint_list'].split('/')
    obj = showRank()
    print(subint_list)
    result = obj.rank(schoolname,grade,name,stu_ID,useremail,subint_list)
    return render(request, 'rankcal/index.html', {'result':result})