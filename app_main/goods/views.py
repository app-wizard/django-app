from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from goods.forms import CommentForm
from goods.models import Products, Comment
from goods.utils import q_search


# Create your views here.
def catalog(request, category_slug=None):
    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None)

    if category_slug == "all":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    curent_page = paginator.page(int(page))

    context = {
        "title": "Restaurant menu",
        "goods": curent_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product_item = Products.objects.get(slug=product_slug)
    comments = product_item.comments.all().order_by("-created_on")
    comment_count = product_item.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.dish = product_item
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, "Comment submitted and awaiting approval"
            )

    comment_form = CommentForm()

    context = {
        "product": product_item,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    }
    return render(request, "goods/product.html", context)


def comment_edit(request, product_slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":
        product_item = Products.objects.get(slug=product_slug)
        comment = get_object_or_404(Comment, pk=comment_id)

        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.dish = product_item
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment!")

    return HttpResponseRedirect(reverse("goods:product", args=[product_slug]))


def comment_delete(request, product_slug, comment_id):
    """
    view to delete comment
    """
    # product_item = Products.objects.get(slug=product_slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("goods:product", args=[product_slug]))
