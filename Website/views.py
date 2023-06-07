from flask import Blueprint, render_template
from flask_login import login_required
from flask_login import current_user
#define views blueprint
views = Blueprint('views', __name__)

#Define route for homepage
@views.route('/', methods=['GET', 'POST'])
@login_required
def home(): #home will run as default
    return render_template("home.html", user=current_user)