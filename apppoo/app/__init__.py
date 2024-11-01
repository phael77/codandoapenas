from flask import Flask, render_template
app = Flask(__name__, template_folder='view')
from app import app
from app import cliente
