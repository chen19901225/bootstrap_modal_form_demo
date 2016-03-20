# coding:utf-8
import flask
from flask import Flask
from flask.ext.wtf import CsrfProtect

from forms import AddChannelForm

app = Flask(__name__)
# csrf = CsrfProtect()
# csrf.init_app(app)
# app.config.setdefault('WTF_CSRF_SECRET_KEY', "showmethemoney")
app.config.setdefault('WTF_CSRF_ENABLED', False)


@app.route('/', methods=['GET', 'POST'])
def index():
    return flask.render_template('index.html')


@app.route('/channel/new', methods=['POST', ])
def create_new_channel():
    request = flask.request
    agent_id = request.form.get('agent_id')
    if agent_id == 100:
        return flask.jsonify(status='error', msg=u'agent_id不对')
    form = AddChannelForm()
    if form.validate_on_submit():
        return flask.jsonify(status='success')
    return flask.jsonify(status='error', msg=form.errors)


@app.route('/validate/channel', methods=['POST'])
def unique_channel_name():
    form = AddChannelForm()
    if form.validate_on_submit():
        return "true"
    return "false"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
