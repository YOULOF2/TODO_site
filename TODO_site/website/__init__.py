from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from TODO_site.auth import login_required, not_logged_in, current_user
from TODO_site.database import db, User, Cards
from .forms import NewToDo

website = Blueprint('website', __name__, template_folder='templates')


@website.route("/main", methods=["GET"])
@login_required
def main():
    user_id = current_user.get_id()
    cards = User.query.filter_by(id=user_id).first().cards
    print(cards)
    return render_template("index.html", todos=cards)


@website.route("/main/add_card", methods=["GET", "POST"])
@login_required
def new_todo():
    todo_form = NewToDo()
    if request.method == "POST":
        title = todo_form.title.data
        sub_title = todo_form.sub_title.data
        body = todo_form.body.data

        user_id = current_user.get_id()
        card = Cards(
            title=title,
            sub_title=sub_title,
            body=body,
            user_id=user_id
        )

        db.session.add(card)
        db.session.commit()
        return redirect(url_for("website.main"))

    return render_template("create_todo.html", form=todo_form)


@website.route("/main/remove_card/", methods=["GET"])
@login_required
def remove_todo():
    card_id = request.args.get('card_id')
    Cards.query.filter_by(id=card_id).delete()
    db.session.commit()
    return redirect(url_for("website.main"))
