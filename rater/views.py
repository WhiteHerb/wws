import json

from django.shortcuts import render,redirect
from .models import Uploadanswer,checkClass,rankClass

from accounts.models import *

class rater :
  def main(request):
    if request.method == 'POST':
      if request.POST['goto'] == 'check':
        return redirect('checksite')
      elif request.POST['goto'] == 'rank':
        return redirect('ranksite')
      elif request.POST['goto'] == 'addanswer':
        return redirect('addanswersite')
    else:
      return render(request, 'index.html')

  def rank(request):

    if request.method == 'POST' :
      post = request.POST
      schoolname = request.user.schoolname #사용자 정보
      grade = request.user.grade #사용자 정보
      name = request.user.username
      stu_ID = request.user.stu_ID
      subject = post['subject']
      if request.session['type'] == 'loadrank' :
        rankloader = rankClass()
        userrank = rankloader.rank(schoolname,grade,name,stu_ID,subject) #랭크 불러오기
        del request.session['type']
        return render(request, 'rank.html', {'usercount' : userrank[0],'userrank' : userrank[1]})
    try:
      del request.session['type']
    except:
      print('no session: type')
    request.session['type'] = 'loadrank'
    grade = request.user.grade
    print(grade)
    sub_list = list(grade.subjects.keys())
    return render(request,'rank.html',{'sub_list':sub_list})

  def check(request):
    if request.method == 'POST':
      post = request.POST
      schoolname = request.user.schoolname #사용자 정보
      grade = request.user.grade #사용자 정보
      name = request.user.username
      stu_ID = request.user.stu_ID
      if request.session['type'] == 'inputinfo':
        testname = post['testname']
        subject = post['subject']
        count = post['count']
        request.session['testinfos'] = [testname,subject]
        request.session['type']='answercheck'
        return render(request, 'check.html', {'testname' : testname,'subject' : subject,
        'name':name,'schoolname':schoolname,'grade':grade, 'count':count})
      elif request.session['type'] == 'answercheck' :
        #체점 model로 실행
        Check = checkClass()
        result = Check.check(
          schoolname=schoolname,
          grade=grade,
          name=name,
          stu_ID=stu_ID,
          post=post,
          session=request.session)
        request.session['type']='showresult'
        return render(request, 'check.html',
        {'result' : Check.result, 'wronglist' : Check.wronglist,'name':name,'schoolname':schoolname,'grade':grade, 'error': result})
    else:
      try :
        del request.session['type']
      except:
        print('no session: type')
      request.session['type']='inputinfo'
      print(request.session)
      grade = request.user.grade
      sub_list = list(grade.subjects.keys())
      return render(request, 'check.html', {"sub_list":sub_list})

  def addanswer(request):
    if request.method == 'POST' :
      if request.session['type']=='inputinfos':
        post = request.POST
        schoolname = Schoolgroup(schoolnameset = request.user.schoolname) #사용자 정보
        grade = request.user.grade #사용자 정보
        print(grade)
        name = request.user.username
        testname = post['testname']
        count = int(post['count'])
        subject = post['subject']
        try :
          del request.session['examinfos']
        except:
          print('on session: examinfos')
        request.session['examinfos'] = {'schoolname':'schoolname','grade':'grade','name':name,'testname':testname,'count':count,'subject':subject}
        del request.session['type']
        request.session['type']='upload'
        return render(request,'addanswer.html', {
          'testname':testname,
          'count':count,
          'subject':subject,
          'schoolname':schoolname,
          'grade':grade,
          'name':name,})
      if request.session['type']=='upload' :
        post = request.POST
        examinfos = request.session['examinfos']
        answer_list = ''
        for i in range(examinfos['count']):
          try :
            answer_list = answer_list + '/' + str(i+1)+' '+post[f'examAnswer_{i+1}']+' '+post[f'examScore_{i+1}']
            print(answer_list)
          except :
            print('false')
            
        print(answer_list)
        examupload = Uploadanswer(
          schoolname=request.user.schoolname,
          grade=request.user.grade,
          subject=examinfos['subject'],
          testname=examinfos['testname'], 
          examinfos=answer_list, 
          writer=examinfos['name'],
          testrealname = str(request.user.schoolname)+str(request.user.grade)+str(examinfos['testname'])
        )
        examupload.save()
        del request.session['type']
        del request.session['examinfos']
        return redirect('/home')
    try:
      del request.session['type']
    except:
      pass
    school = request.user.schoolname
    grade = request.user.grade
    print(grade)
    sub_list = list(grade.subjects.keys())
    request.session['type'] = 'inputinfos'
    return render(request,'addanswer.html',{"sub_list":sub_list})
