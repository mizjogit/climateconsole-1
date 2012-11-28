from flask import Flask, url_for, make_response, flash, redirect
from flask import render_template
from flask import request

from  sqlalchemy import create_engine, Table, MetaData, select, join
from sqlalchemy.orm import scoped_session, sessionmaker

import sqlalchemy.exc

from flask.ext.bootstrap import Bootstrap

import sys
import json
import time
#import mod_wsgi

import sakidb

sys.stdout = sys.stderr

app = Flask(__name__)
Bootstrap(app)

app.config.from_object(__name__)
app.debug = True

engine = create_engine(u'mysql://root:Schumacher4@localhost/templogger')
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/post', methods=['POST'])
def post():
    for probe,temp in request.form.items():
	session.add(sakidb.data(probe, temp))
    session.commit()
    return " "

@app.route('/report')
def report():
    vals = session.query(sakidb.data).all()
    return render_template('report.html', vals=vals)

@app.route('/graph')
def graph():
    return render_template('graph.html')

@app.route('/jsond/<int:sensor>')
def jsond(sensor=0):
    qry = session.query(sakidb.data).filter(sakidb.data.probe_number == sensor)
    return json.dumps([(time.mktime(ii.timestamp.timetuple()) * 1000, ii.temperature) for ii in qry])

app.secret_key = "\xcc\x1f\xc6O\x04\x18\x0eFN\xf9\x0c,\xfb4{''<\x9b\xfc\x08\x87\xe9\x13"

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
