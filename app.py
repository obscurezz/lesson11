from flask import Flask, render_template, request
from utilities import candidate

CANDIDATES_LIST = candidate.Candidates('candidates.json')

app = Flask(__name__)


@app.route('/')
def master():
    title = 'Candidates'
    return render_template('list.html', title=title, items=CANDIDATES_LIST.get_candidates_by_name())


@app.route('/candidate/<int:uid>')
def card(uid: int):
    user_card = CANDIDATES_LIST.get_candidate_by_id(uid)
    title = user_card['name']
    return render_template('card.html', title=title, user=user_card)


@app.route('/skills/<skill>')
def skills(skill: str):
    cards = CANDIDATES_LIST.get_candidates_by_skill(skill)
    count = len(cards)
    return render_template('skill.html', title=skill, cards=cards, count=count)


@app.route('/search/<candidate_name>')
def search(candidate_name: str):
    title = candidate_name
    users = CANDIDATES_LIST.get_candidates_by_name(candidate_name)
    count = len(users)
    return render_template('search.html', title=title, users=users, count=count)


app.run(port=8080, debug=True)
