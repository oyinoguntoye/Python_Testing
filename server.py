import json
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         # BUG Fix: Avoid booking places in past competitions, filters out any competitions that were in the pass
         listOfCompetitions = [c for c in listOfCompetitions if c['date'] >= datetime.today().strftime('%Y-%m-%d-%H:%M:%S')]
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html',club=club,competitions=competitions,clubs=clubs)
    except:
        # ERROR Fix: Entering a unknown email crashes the app, instead it now shows an error message prompting user to try again
        flash("Something went wrong-please try again")
        return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions,clubs=clubs)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    # BUG: Clubs shouldn't be able to book more than 12 places per competition
    if int(request.form['places']) > 12:
        flash("You can book no more than 12 places. Try Again.")
        return render_template('welcome.html', club=club, competitions=competitions,clubs=clubs)
    # BUG: Clubs should not be able to use more than their available points
    elif int(request.form['places']) > int(club['points']):
        flash("You cannot redeem more points than you available. Try Again.")
        return render_template('welcome.html', club=club, competitions=competitions,clubs=clubs)
    else:
        placesRequired = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    # Updated: 3 points per place rather than 1 point per place
    club['points'] = int(club['points'])-3*placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions,clubs=clubs)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
