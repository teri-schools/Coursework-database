from flask import Blueprint, render_template, request, redirect, url_for
from db.repository import LabelRepository

bp = Blueprint("label", __name__)
label_repo = LabelRepository()

@bp.route("/labels")
def catalog():
    labels = label_repo.get_all_labels()
    return render_template("label/list.html", labels=labels)

@bp.route("/label/new", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        country_id = request.form["country_id"]
        label_repo.add_label(name=name, country_id=country_id)
        return redirect(url_for("label.catalog"))

    return render_template("label/create.html")

@bp.route("/label/edit/<int:label_id>", methods=["GET", "POST"])
def edit(label_id):
    label = label_repo.get(label_id)
    if request.method == "POST":
        label_repo.update_label(label_id, request.form["name"], request.form["country_id"])
        return redirect(url_for("label.catalog"))
    return render_template("label/edit.html", label=label)

@bp.route("/label/delete/<int:label_id>", methods=["POST"])
def delete(label_id):
    label_repo.delete_label(label_id)
    return redirect(url_for("label.catalog"))

# Add other routes for edit and delete as needed
