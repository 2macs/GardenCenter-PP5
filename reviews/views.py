from django.shortcuts import render, redirect
from .models import SiteReview
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
