from flask import Flask, render_template, redirect, request, url_for
from flask import Blueprint
from project_work.models.member import Member
import project_work.repositories.member_repository as member_repository


members_blueprint = Blueprint("members", __name__)


@members_blueprint.route("/members", methods=['GET', 'POST'])
def members():
    members = member_repository.select_all()
    return render_template("members/show_members.html", members = members)

# @members_blueprint.route("/members/<id>")
# def show(id):
#     member = member_repository.select(id)

#     render_template("members/show.html", member = member)

@members_blueprint.route("/show_new_member_form", methods=['GET', 'POST'])
def show_new_member_form():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        newmember = Member(first_name=first_name.title(), last_name=last_name.title())
        member_repository.save(newmember)
        return redirect(url_for('members.members'))
    return render_template("members/add_member.html")


@members_blueprint.route("/edit_member/<int:member_id>", methods=['GET'])
@members_blueprint.route("/edit_member", methods=['POST'])
def edit_member(member_id=None):
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        member_id = request.form['member_id']
        editmember = Member(first_name=first_name.title(), last_name=last_name.title(), id=int(member_id))
        member_repository.update(editmember)
        return redirect(url_for('members.members'))
    member = member_repository.select(member_id)
    return render_template("members/edit_member.html", member=member)



