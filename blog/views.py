from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Article
from .forms import CommentaireForm

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    commentaires = article.commentaires.filter(approuve=True)

    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.article = article
            commentaire.save()
            messages.success(request, "Votre commentaire a été ajouté et sera visible après validation.")
            return redirect('blog:detail', pk=article.pk)
    else:
        form = CommentaireForm()
    return render(request, 'blog/article_detail.html', {'article': article, 'commentaires': commentaires,'form': form,})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

@login_required
def ajouter_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('blog:detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'blog/ajouter_article.html', {'form': form})