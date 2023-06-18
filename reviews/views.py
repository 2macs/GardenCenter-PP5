from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import SiteReview, Comments
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# View all site reviews


def all_reviews(request):
    reviews = SiteReview.objects.all()
    return render(request, "reviews/reviews.html", {"reviews": reviews})


@login_required
def create_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user  # Assign the current signed-in user
            review.save()
            messages.info(request, f"Thank you for your review!")
            return redirect("all_reviews")

    else:
        form = ReviewForm()
    return render(request, "reviews/create_review.html", {"form": form})


@login_required
def get_user_review(request):
    author = request.user
    user_reviews = SiteReview.objects.filter(author=author)
    review_author = author
    context = {"user_reviews": user_reviews, "review_author": review_author}
    return render(request, "reviews/get_user_review.html", context)


@login_required
def delete_review(request, user_review_id):
    """Delete a review, only review owner can delete"""
    my_review = get_object_or_404(SiteReview, pk=user_review_id)
    my_review.delete()
    messages.success(request, "Review deleted!")
    return redirect(reverse("get_user_review"))


@login_required
def edit_review(request, user_review_id):
    """Edit a review, only review owner can edit"""
    my_review = get_object_or_404(SiteReview, pk=user_review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=my_review)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated your review!")
            return redirect(reverse("get_user_review"))

        else:
            messages.error(
                request, "Failed to update review. Please ensure the form is valid."
            )
    else:
        form = ReviewForm(instance=my_review)
        messages.info(request, f"You are editing {my_review.heading}")

    template = "reviews/edit_review.html"
    context = {
        "form": form,
        "my_review": my_review,
    }

    return render(request, template, context)


@login_required
def add_comment(request, user_review_id):
    review = get_object_or_404(Review, pk=user_review_id)

    if request.method == "POST":
        content = request.POST.get("body")
        comment = Comment.objects.create(
            content=content, user=request.user, review=review
        )
        return redirect("review_detail", user_review_id=user_review.id)

    return render(request, "add_comment.html")
