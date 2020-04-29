from flask import Flask
from flask import request
import os,subprocess
import json
import sys



web_service = Flask(__name__)

@web_service.route('/')
def get(self):
    file_url =  "https://www.researchgate.net/publication/51469608/figure/fig1/AS:339688444448772@1457999444671/Chest-X-ray-on-admission-showed-cardiomegaly-with-a-clear-lung.png"
    results = subprocess.Popen("python main.py " + file_url, shell=True, stdout=subprocess.PIPE).stdout.read()
    jr = json.dumps(str(results))
    return jr

if __name__ == '__main__':
	web_service.run(debug=True, host='0.0.0.0', port=80)


