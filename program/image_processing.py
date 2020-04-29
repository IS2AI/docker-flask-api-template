from PIL import Image
import requests
from io import BytesIO


def im_process(url):
    
    ext = url.split(".")[1].lower()
    response = requests.get(url)
    file_name = BytesIO(response.content)
    
    if (ext == 'dcm'):

	    from pydicom import dcmread
	    im = dcmread(file_name).pixel_array
	    im = Image.fromarray(im)

    else:    
	    im = Image.open(file_name)  

    
    

    return im  
