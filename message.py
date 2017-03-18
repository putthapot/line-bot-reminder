# -*- coding: utf-8 -*-

import os
import logging

from linebot import LineBotApi
from linebot.models import TextMessage

def send_text_message(user_id, text):
	channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
	line_bot_api = LineBotApi(channel_access_token)
	message = TextMessage("1", text)
	line_bot_api.push_message(user_id, message)