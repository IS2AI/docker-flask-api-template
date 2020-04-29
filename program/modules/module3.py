




def module3(xray_type, im):
    
    if xray_type == 'Chest':
        from modules.module3_zoo.chest import chest
        model3_path = "models/module3/chest.pth"
        threshold = 0.5
        res, model = chest(model3_path,im, threshold)
        return (res, model)
        