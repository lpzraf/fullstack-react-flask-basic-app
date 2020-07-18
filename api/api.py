# from time import time, ctime
import time
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    # t = time()
    # return {'time': ctime(t)}
    return {'time': time.time()}