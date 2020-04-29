import torch
from torch import nn
import pretrainedmodels
import torchvision.transforms as transforms
import numpy as np


def chest(model_path, image, threshold,  device = 'cpu'):
    
    #Set the model
    model_name = 'densenet121'
    num_classes = 14
    model_fn = pretrainedmodels.__dict__[model_name]
    model = model_fn(num_classes=1000) #.to(self.device)
    model.last_linear = nn.Linear(1024, num_classes) #.to(self.device)
  
    
    #load = torch.load(model_path)["model_state_dict"]
    load = torch.load(model_path, map_location=torch.device('cpu'))["model_state_dict"]
    load["last_linear.weight"] = load.pop("classifier.weight")
    load["last_linear.bias"] = load.pop("classifier.bias")
    
    model.load_state_dict(load)
    model.eval()
    
    #Set transformations
    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]
    transformations = transforms.Compose([
                transforms.Resize(224),
                transforms.CenterCrop(224),
		    transforms.Grayscale(3),
                transforms.ToTensor(),
                transforms.Normalize(mean, std)])
    
    image = transformations(image) #.to(self.device)
    
    #Make prediction
    
    pred = torch.sigmoid(model.forward(image.unsqueeze(0))).cpu().detach().numpy()[0]

    class_names = [
        'Atelectasis',
        'Cardiomegaly',
        'Effusion',
        'Infiltration',
        'Mass',
        'Nodule',
        'Pneumonia',
        'Pneumothorax',
        'Consolidation',
        'Edema',
        'Emphysema',
        'Fibrosis',
        'Pleural Thickening',
        'Hernia']

        
    xray_dis = np.where(pred > threshold)[0]
    res = [{class_names[i]:pred[i]} for i in xray_dis]
    

    
    return (res, model)
