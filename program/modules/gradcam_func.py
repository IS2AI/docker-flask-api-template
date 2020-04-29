from gradcam.utils import visualize_cam
from gradcam import GradCAM
import torchvision.transforms as transforms

def grad_cam(model, model_type, layer_name, normed_torch_img, torch_img):
    config =  dict(model_type = model_type, arch = model, layer_name = layer_name)
    config['arch'].eval() #.to(device)
    
    cam = GradCAM.from_config(**config)
    mask, _ = cam(normed_torch_img)
    heatmap, result = visualize_cam(mask, torch_img )
    
    return(transforms.ToPILImage()(result))