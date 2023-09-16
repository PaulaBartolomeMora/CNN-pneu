
# 
def get_images(dir): #dir = chest_xray/train/ o chest_xray/test/
    IMAGES = []
    LABELS = []
    
    for subdir in os.listdir(dir): #lista de subdirectorios en train/ o test/ -> ['NORMAL', 'PNEUMONIA']
        if dir in ['NORMAL']:
            label = 0
        elif dir in ['PNEUMONIA']:
            label = 1
        else: 
            label = 2
    
    for image_name in tqdm(os.listdir(dir+subdir)): #barra de progreso
        image = cv2.imread(dir + subdir + '/' + image_name) #lectura
        image_array = preprocess(image)
        
        IMAGES.append(image_array)
        LABELS.append(label)
        
    IMAGES = np.asarray(IMAGES)
    LABELS = np.asarray(LABELS)
    


# Preprocesado: redimensionado 150x150, escala de grises y conversión a array
def preprocess(image): 
    if image is not None:
        image = skimage.transform.resize(image, (150,150,3), mode = 'constant', anti_aliasing=True)
        image = rgb2gray(image)
        image_array = np.asarray(image)
    return image_array
