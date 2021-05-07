from flask import Blueprint, render_template

from app.auth.views import login_required
from app.model.review_model import ReviewModel
from app.model.user_model import UserModel

user = Blueprint('user', __name__, template_folder='templates')


@user.route("/profile/<user>", methods=["GET", "POST"])
@login_required
def profile(user):
    logged_user = UserModel().find_user_by_name(user)
    reviews = ReviewModel().find_all_user_reviews(logged_user.get_username())
    books = logged_user.get_favorite_books()
    return render_template("profile.html", user=logged_user, reviews=reviews, books=books)
