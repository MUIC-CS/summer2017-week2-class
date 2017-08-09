from flask import Flask, render_template, request, redirect, url_for
from phonerecord import PhoneRecordRepo, PhoneRecord

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


@app.route('/edit/<id>')
def edit():
    obj = PhoneRecordRepo


app.run(debug=True)

#
#
#
#
#
#
#
