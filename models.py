from slackclient import SlackClient

class SlackApi(object):

	def __init__(self, token):
		self.sc = SlackClient(token)

	def users_list(self):
		return self.sc.api_call("users.list")

	def channels_list(self):
		return self.sc.api_call("channels.list")

	def find_messages(self, channel_id, count):
		return self.sc.api_call("channels.history", 
			channel=channel_id,
			count=count, 
			unreads=1, 
			inclusive=1)

	def post_message(self, message, channel):
		return self.sc.api_call("chat.postMessage", 
			channel=channel, 
			text=message, 
			username="pybot", 
			icon_emoji=":robot_face:")
