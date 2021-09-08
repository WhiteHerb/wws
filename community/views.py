from django.shortcuts import render, get_object_or_404, redirect
from .models import Post,Comment
from django.utils import timezone
from  .forms import PostForm
from django.contrib import messages
import math


class community :
  def post_list(request):
    page = int(request.GET.get('page', 1))
    paginated_by = 2
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    total_count = len(posts)
    total_page = math.ceil(total_count/paginated_by)
    page_range = range(1,total_page+1)
    start_index = paginated_by*(page-1)
    end_index = paginated_by*page
    posts = posts[start_index:end_index]

    return render(request, 'community/post_list.html', {'object_list' : posts,'total_page':total_page,'page_range':page_range})

  def post_detail(request, pk):
    post_detail = get_object_or_404(Post,pk=pk)
    comments = Comment.objects.filter(post = pk)
    if request.method == "POST":
      if request.POST['body']:
        comment = Comment()
        comment.post = post_detail
        comment.body = request.POST['body']
        comment.date = timezone.now()
        comment.save()
      else :
        messages.success(request, '내용을 입력해 주세요')
    return render(request, 'community/post_detail.html',{'post':post_detail, 'comments': comments})

  def post_new(request):
    if request.method == 'POST':
      form = PostForm(request.POST)
      if request.user.is_authenticated :
        if form.is_valid():
          post = form.save(commit=False)
          post.author = request.user
          post.published_date = timezone.now()
          post.save()
          return redirect('post_detail', pk=post.pk)
      else :
          return render(request, 'community/post_detail.html')
    else:
      form = PostForm()
    return render(request, 'community/post_edit.html', {'form':form})
