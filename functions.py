

def get_images(dir):
    IMAGES = []
    LABELS = []
    
    if dir in ['NORMAL']:
        label = 0
    elif dir in ['PNEUMONIA']:
        label = 1
    else: 
        label = 2
    


# Preprocesado: redimensionado 150x150, escala de grises y conversión a array
def preprocess(image): 
    if image is not None:
        image = skimage.transform.resize(image, (150,150,3), mode = 'constant', anti_aliasing=True)
        image = rgb2gray(image)
        image_array = np.asarray(image)
    return image_array
