from flask import Flask, render_template, redirect
from blitzdb import FileBackend, Document

app = Flask(__name__)

backend = FileBackend('./compeatup-db')

# Define BlitzDB models.

'''

The User model contains an email, a name, their current city and their age and gender. It will also have links to compeatups
they've liked or said yes to.

'''

class User(Document):
	pass


'''

The CompEatUp model contains a name, a link to the user initiating it, the host, their address, as well as a date and prize details.

'''

