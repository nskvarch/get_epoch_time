"""get unix time via https://safe-hollows-03074.herokuapp.com/get_time"""
import os
import time
from flask import Flask

app = Flask(__name__)


@app.route('/get_time/')
def get_time():
    return str(time.time())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
