#!/usr/bin/python3
"""
a script that starts a Flask web application
and must be listening on 0.0.0.0, port 5000
routes:
		/states_list -   display HTML and state info from storage;
		/cities_by_state - displays the states and cities in them
		/states/<id> - displays a particular city based on the id
		/hbnb_filters - display a HTML page like 6-index.html,
  		which was done during the project 0x01. AirBnB clone - Web static
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


@app.route('/states/<id>', strict_slashes=False)
def html_if_stateID(id):
    """display html page; customize heading with state.name
       fetch sorted cities for this state ID into LI tag ->in HTML file
    """
    state_obj = None
    for state in storage.all("State").values():
        if state.id == id:
            state_obj = state
    return render_template('9-states.html',
                           state_obj=state_obj)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filter():
    """
    make a static page dynamic
    """
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()

    return render_template('10-hbnb_filters.html', 
                           states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
