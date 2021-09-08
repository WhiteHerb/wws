from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout

from .forms import SignupForm

class accounts :
  def signup_main(request):
    context = {}

    if request.POST:
      
      form = SignupForm(request.POST)
      if form.is_valid() :
        print('save sign up')
        form.save()
        email = form.cleaned_data.get('email')
        raw_password = form.cleaned_data.get('password1')
        account = authenticate(email=email,password=raw_password)
        login(request,account)
        return redirect('home')
      else:
        context['signupForm'] = form
    else:
      form = SignupForm()
      context['signupForm'] = form
    
    return render(request,'signup.html', context)
        
  def login_main(request):
    if request.POST :
      email = request.POST['email']
      password = request.POST['password']
      user = authenticate(email=email,password=password)
      if user is not None:
        login(request,user)
        request.session['user'] = request.user.email
        return redirect('/home')
      else :
        return render(request, 'login.html',{'error': '이메일 또는 비밀번호가 틀렸습니다'})
    return render(request, 'login.html')


  def logout_main(request):
    logout(request)
    # def request.session['user']
    return redirect('home')