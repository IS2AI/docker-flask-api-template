from flask import Flask
from flask import request
import os,subprocess
import json
import sys

web_service = Flask(__name__)

@web_service.route('/data', methods=['GET', 'POST'])
def mydata():
    #file_url =  "https://www.researchgate.net/publication/51469608/figure/fig1/AS:339688444448772@1457999444671/Chest-X-ray-on-admission-showed-cardiomegaly-with-a-clear-lung.png"
    file_url = request.args.get('file')
    results = subprocess.Popen("python3 main.py " + file_url, shell=True, stdout=subprocess.PIPE).stdout.read()

    x_ray_img_json = results.decode('utf8').replace("'", '"')

    x_ray_img_json = json.loads(x_ray_img_json)

    x_ray_img_json = json.dumps(x_ray_img_json)

    return x_ray_img_json


if __name__ == '__main__':
	web_service.run(debug=True, host='0.0.0.0', port=80)


