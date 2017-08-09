from flask import Flask, render_template
from phonerecord import PhoneRecordRepo

app = Flask('phonebook')


@app.route('/')
def index():
    prs = PhoneRecordRepo.find_all()
    return render_template('index.html', prs=prs)


app.run(debug=True)
