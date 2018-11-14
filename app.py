from flask import Flask, render_template, request, redirect, url_for
from flask_dance.contrib.spotify import make_spotify_blueprint, spotify
from flask_bootstrap import Bootstrap
import requests, json, urllib.parse

app = Flask(__name__)
app.secret_key = 'development'
Bootstrap(app)

blueprint = make_spotify_blueprint(
    client_id='613f80f4035d442ea0b02a78556d7dfa',
    client_secret='e28971afbee14756871d5eb08c5e5a6c',
    scope='playlist-modify-public streaming user-library-read',
)
app.register_blueprint(blueprint, url_prefix='/login')

@app.route('/')
def index():
    if not spotify.authorized:
        return redirect(url_for('spotify.login'))
    search_string = urllib.parse.quote('The Birthday Party')
    resp = spotify.get(f'v1/search?q={search_string}&type=artist')
    return render_template('home.html', data=resp.json())