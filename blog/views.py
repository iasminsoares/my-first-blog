from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm #importando o modelo de formulário
from django.shortcuts import redirect #podemos dizer: "vá para a página post_detail para o post recém-criado":

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
     if request.method == "POST":
         form = PostForm(request.POST)
         if form.is_valid(): #checar se o formulário está correto (todos os campos requeridos estão prontos e valores incorretos não serão salvos)
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm()
     return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
     post = get_object_or_404(Post, pk=pk)
     if request.method == "POST":
         form = PostForm(request.POST, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm(instance=post)
     return render(request, 'blog/post_edit.html', {'form': form})

     #Isso é quase igual à nossa view de post_new, né? Mas não inteiramente. Primeira coisa: passamos um parâmetro extra pk a partir da url. 
     #Em seguida, pegamos o modelo Post que queremos editar com get_object_or_404 (Post, pk=pk) e então, quando criamos um formulário, 
     #passamos este post como uma instância tanto quando salvamos o formulário…
