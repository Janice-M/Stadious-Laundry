from flask import Flask,render_template, request,redirect,url_for, abort
from . import main
from flask_login import login_required
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map


app = Flask(__name__, template_folder="")
GoogleMaps(app)

@main.route('/')
def index():
    title = "Home"
    return render_template('index.html', title=title)

def mapview():
# creating a map in the view
    mymap = Map(
    identifier="view-side",
    lat=37.4419,
    lng=-122.1419,
    markers=[(37.4419, -122.1419)]
    )   
    sndmap = Map(
    identifier="sndmap",
    lat=37.4419,
    lng=-122.1419,
    markers=[
    {
    'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
    'lat': 37.4419,
    'lng': -122.1419,
    'infobox': "<b>Hello World</b>"
    },
    {
    'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
    'lat': 37.4300,
    'lng': -122.1400,
    'infobox': "<b>Hello World from other place</b>"
    }
    ]
    )
    return render_template('index.html', mymap=mymap, sndmap=sndmap)

    if __name__ == "__main__":
    app.run(debug=True)



@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)