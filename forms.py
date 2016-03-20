# coding:utf-8
from flask.ext.wtf import Form
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired
from wtforms import validators


class AddChannelForm(Form):
    agent_id = IntegerField(validators=[DataRequired("A agent_id is required")])
    channel_name = StringField(validators=[DataRequired(), validators.Length(max=255, message=u'最大长度为255')])

    def clean_channel_name(self):
        channel_name = self.cleaned_data['channel_name']
        agent_id = self.cleaned_data['agent_id']
        if agent_id == 0 and channel_name == 'baidu':
            raise validators.ValidationError(u'渠道名已被注册')

        return channel_name

