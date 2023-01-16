#!/usr/bin/python3
"""
a script that starts a Flask web application
and must be listening on 0.0.0.0, port 5000
routes:
		/states_list -   display HTML and state info from storage;
"""

from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def html_fetch_states():
    """display html page
       fetch sorted states to insert into html in UL tag
    """
    state_objs = [s for s in storage.all("State").values()]
    return render_template('7-states_list.html',
                           state_objs=state_objs)


@app.teardown_appcontext
def teardown_app(e):
    '''
    teardown app context
    '''
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    '''
    Lists cities by the state
    it is in
    '''
    state_dict = storage.all('State')
    state_list = []
    for state in state_dict.values():
        state_list.append(state)
    return render_template('8-cities_by_states.html', state_list=state_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
