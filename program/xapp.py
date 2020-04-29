from modules.module1 import module1
from modules.module2 import module2
from modules.module3 import module3
from modules.gradcam_func import grad_cam
import matplotlib.pyplot as plt 
import numpy as np
import base64
import torchvision.transforms as transforms
from image_processing import im_process

import io

def app(url):
    #    file_name = "test_images/123.dcm" # input file
    return_json = {}          # output dictionary that we should convert to json

    im = im_process(url)

    model1_path = "models/1.pth"
    ans1 = module1(model1_path, im)
    
    if (ans1[0] != 'X-Ray'): 
        return_json['img_type'] = 'Not X-Ray'
        
        return return_json
       
        
    return_json['img_type'] = 'X-Ray'
    
    model2_path = "models/2.pth"
    ans2 = module2(model2_path, im)
    return_json['xray_type'] = ans2[0]

    #try:
    res, model = module3(ans2[0], im)
    return_json['disease'] = res
    #except:
    #    print ("Development of prediction for X-ray type of ",ans2[0], 'is still in progress' )
    #    return return_json
    
    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]
    transformations = transforms.Compose([
                        transforms.Resize(224),
                        transforms.CenterCrop(224),
                        transforms.Grayscale(3),
                        transforms.ToTensor()])
            
    torch_img = transformations(im)
    normed_torch_img = transforms.Normalize(mean, std)(torch_img).unsqueeze(0)
    
    heatmap_image = grad_cam(model= model, model_type ='densenet', layer_name='features_norm5', normed_torch_img=normed_torch_img, torch_img=torch_img)   #output image
    
    #plt.imshow(heatmap_image)

    imgByteArr = io.BytesIO()
    heatmap_image.save(imgByteArr, format='PNG')
    imgByteArr = imgByteArr.getvalue()

    b64string = base64.b64encode(imgByteArr)

    return_json['image'] = b64string #np.array(heatmap_image).tolist()
    
    
    return (return_json)



