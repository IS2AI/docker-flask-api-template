from xapp import app
import json
import sys


#url = sys.argv[1]
#url = "https://www.researchgate.net/publication/51469608/figure/fig1/AS:339688444448772@1457999444671/Chest-X-ray-on-admission-showed-cardiomegaly-with-a-clear-lung.png"
#url = "https://as.ftcdn.net/r/v1/pics/7b11b8176a3611dbfb25406156a6ef50cd3a5009/home/discover_collections/optimized/image-2019-10-11-11-36-27-681.jpg"
#url = "https://www.radiologyinfo.org/gallery-items/images/bone-xray-hands.jpg"
url = "https://ars.els-cdn.com/content/image/1-s2.0-S0378603X1500248X-gr4a.jpg"


if __name__== "__main__":

    url = sys.argv[1]
    json_file = app(url)

    json_dump = json.dumps(str(json_file))
    
    print(json_dump)

