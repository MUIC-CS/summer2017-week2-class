from flask import Flask, render_template, request, redirect, url_for
from phonerecord import PhoneRecordRepo, PhoneRecord
from friendship import FriendShip, FriendShipRepo

app = Flask('phonebook')


@app.route('/')
def index():
    prs = PhoneRecordRepo.find_all()
    return render_template('index.html', prs=prs)


@app.route('/', methods=["POST"])
def add():
    name = request.form['name']
    phoneno = request.form['phoneno']
    pr = PhoneRecord(None, name, phoneno)
    PhoneRecordRepo.add(pr)
    return redirect(url_for('index'))


@app.route('/remove', methods=["POST"])
def remove():
    id = request.form['id']
    PhoneRecordRepo.delete_by_id(id)
    return redirect(url_for('index'))


@app.route('/edit/<id>')  # GET
def edit(id):
    obj = PhoneRecordRepo.find_by_id(id)
    return render_template('edit.html', obj=obj)


@app.route('/edit', methods=["POST"])
def edit_phonerecord():
    id = request.form['id']
    name = request.form['name']
    phoneno = request.form['phoneno']

    obj = PhoneRecordRepo.find_by_id(id)
    obj.name = name
    obj.phoneno = phoneno
    PhoneRecordRepo.save(obj)
    return redirect(url_for('index'))


def love_hate(id, love):
    fsh = FriendShipRepo.find_friend(id, love)
    left = [x.left_id for x in fsh]
    right = [x.right_id for x in fsh]
    all_id = filter(lambda x: x != id, left + right)
    all_id = list(set(all_id))  # unique
    people = [PhoneRecordRepo.find_by_id(x) for x in all_id]
    me = PhoneRecordRepo.find_by_id(id)
    return render_template('list_people.html',
                           people=people,
                           me=me,
                           relationship='love' if love else 'hate'
                           )


@app.route('/lovers/<id>')
def lovers(id):
    return love_hate(id, True)


@app.route('/haters/<id>')
def haters(id):
    return love_hate(id, False)


app.run(debug=True)

#
#
#
#
#
#
#
