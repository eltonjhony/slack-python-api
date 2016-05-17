from flask import Flask
from models import SlackApi
from flask import jsonify

app = Flask(__name__)
slack_api = SlackApi("xoxp-2195292530-15854845845-42615916823-217a7f4771")

@app.route("/nsk/slack/users/list")
def users_list():
    return jsonify(slack_api.users_list())

@app.route("/nsk/slack/channels/list")
def channels_list():
    return jsonify(slack_api.channels_list())

@app.route("/nsk/slack/find/<channel_id>/<count>")
def find_messages(channel_id, count):
    return jsonify(slack_api.find_messages(channel_id, count))

@app.route("/nsk/slack/post/message/<message>/<channel>", methods = ['POST'])
def post_message(message, channel):
    return jsonify(slack_api.post_message(message=message, channel=channel))

if __name__ == "__main__":
   app.run(host='0.0.0.0')
