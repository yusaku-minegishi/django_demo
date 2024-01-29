from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Post, User

def top_view(request):
    return render(request, "sns/top.html")

@login_required
def list_view(request):
    object_list = Post.objects.all().order_by("updated_at")
    context = {"object_list": object_list}
    return render(request, "sns/post_list.html", context)

@login_required
def user_list_view(request, user):
    selected_user = User.objects.get(username=user)
    object_list = Post.objects.filter(username=selected_user).order_by("updated_at")
    context = {"selected_user": selected_user, "object_list": object_list}
    return render(request, "sns/post_user_list.html", context)

@login_required
def detail_view(request, pk):
    object = Post.objects.get(pk=pk)
    context = {"object": object}
    return render(request, "sns/post_detail.html", context)

@login_required
def create_view(request):
    if request.method == "POST":
        username = request.user
        text = request.POST["text"]
        Post.objects.create(username=username, text=text)
        return redirect("sns:list")
    if request.method == "GET":
        return render(request, "sns/post_form.html")

@login_required
def update_view(request, pk):
    object = Post.objects.get(pk=pk)
    if request.method == "POST":
        object.text = request.POST["text"]
        object.save()
        return redirect("sns:detail", pk)
    else:
        context = {"object": object}
        return render(request, "sns/post_update.html", context)

@login_required
def delete_view(request, pk):
    object = Post.objects.get(pk=pk)
    if request.method == "POST":
        object.delete()
        return redirect("sns:userlist", object.username)
    else:
        context = {"object": object}
        return render(request, "sns/post_confirm_delete.html", context)