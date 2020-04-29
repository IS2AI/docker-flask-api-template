import torch
from torch import nn
import pretrainedmodels
import torchvision.transforms as transforms
import numpy as np


        
def module1( model_path, image, device = 'cpu'):

    #Set the model
    model_name = 'densenet121'
    num_classes = 2
    model_fn = pretrainedmodels.__dict__[model_name]
    model = model_fn(num_classes=1000).to(device)#.to('cuda') #.to(self.device)
    model.last_linear = nn.Linear(1024, num_classes).to(device)#.to('cuda')  #.to(self.device)
    #load = torch.load(model_path)["model_state_dict"]
    load = torch.load(model_path, map_location=torch.device('cpu'))["model_state_dict"]
    model.load_state_dict(load)
    model.eval()
    
    #Set transformations
    transformations = transforms.Compose([
                transforms.Resize(224),
                transforms.CenterCrop(224),
                transforms.Grayscale(3),
                transforms.ToTensor()])
    
    
    image = transformations(image)#.to('cuda') #.to(self.device)
    
    #Make prediction
    
    pred = torch.sigmoid(model.forward(image.unsqueeze(0))).cpu().detach().numpy()[0]
    maxpred = round(np.amax(pred), 3)      
 
    class_names = ["Not X-ray","X-Ray"]
    ind = (np.where(pred == np.amax(pred))[0]).item()
    res = class_names[ind]
        

    return (res,maxpred)
    
