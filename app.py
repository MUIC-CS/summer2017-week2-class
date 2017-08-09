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

app.run(debug=True)

#
#
#
#
#
#
#
