from django.shortcuts import render, redirect
from django.contrib.auth import logout

class Home :
  def home_main(request):
    user_id = None
    try:
      user_id = request.session['user']
    except :
      pass
    if user_id:
      print(user_id)
      print('재접')
    else:
      logout(request)
      return render(request,'home/index.html')
    return render(request,'home/index.html')      

  def go_to_community(request):
    if request.user.is_authenticated :
      print('l')
      return redirect('/community')
    else :
      return render(request,'index.html', {'error':'please login first'})