from django.shortcuts import render
from .forms import AddComment
from .models import Comment


# Create your views here.
def home(request):
    return render(request, "comments/index.html")


def about_me(request):
    return render(request, "comments/about_me.html")


def comments_page(request):
    comments = Comment.objects.all()
    if request.method == "POST":
        form = AddComment(request.POST)
        if form.is_valid():
            form.save()
            form = AddComment()
            return render(
                request,
                "comments/comments_page.html",
                context={"form": form, "comments": comments},
            )

    else:
        form = AddComment()
    return render(
        request,
        "comments/comments_page.html",
        context={"form": form, "comments": comments},
    )


def contact_me(request):
    return render(request, "comments/contact_me.html")
