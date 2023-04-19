import numpy as np
from skimage import io, img_as_float32, transform
from matplotlib import pyplot as plt

# Load and preprocess data here

def load_data():
    # Return DataLoader? Not sure
    return None


def format_images(img_paths):
    '''
    Takes a set of images and formats them to be read by the descriminator network.
    Formatted images are RGB with dtype float32 and shape (3, img_size, img_size)

    :params:
    imgs_paths: a 1D np.array (or python list) of local directories for the real image set

    :returns:
    formatted_imgs: an np.ndarray of shape [num_imgs, 3, 64, 64]
    '''
    img_size = 64 # number of pixels per side in output images
    num_imgs = len(img_paths)

    # Initialize the output array
    formatted_imgs = np.zeros([num_imgs, 3, img_size, img_size])

    # Loop through images and format it
    for i in range(num_imgs):
        img = io.imread(img_paths[i])
        img = img_as_float32(img)
        if len(img.shape) == 2: # Convert BW images to RGB
            img = np.stack([img, img, img], axis=-1)
        img = transform.resize(img, (3, 64, 64), anti_aliasing=True)
        formatted_imgs[i] = img

    return formatted_imgs



def shuffle_real_and_fake(real_imgs, fake_imgs):
    '''
    Creates a single, randomly ordered array of images from two arrays of real and fake images, respectively.

    :params:
    real_imgs: a np.ndarray of shape [n, 3, img_size, img_size] composed of real images from the data set
    fake_imgs: a np.ndarray of shape [m, 3, img_size, img_size] produced by the generator network

    :returns:
    random_img_shuffle: a np.ndarray of shape [n+m, img_size, img_size, 3] of randomly ordered real and fake images
    '''

    random_img_shuffle = np.append(real_imgs, fake_imgs, axis=0)
    np.random.shuffle(random_img_shuffle)
    
    return random_img_shuffle



def standardize(imgs):
    '''
    Standarizes a sets of images in place before they are read by the descriminator.

    :params:
    imgs: an np.ndarray of shape [num_imgs, 3, img_size, img_size]

    :returns:
    None
    '''
    mean = np.sum(imgs, axis=0)/len(imgs)
    std = np.std(imgs, axis=0)
    imgs = (imgs-mean)/std 
    return


def create_generator_seeds(batch_size):
    '''
    Creates a new set of random seed vectors for the generator

    :params:
    batch_size: the number of seeds to generate for each training iteration

    :returns:
    generator_seeds: an np.ndarray of shape [batch_size, 1, 100] with random entries on [0,1]
    '''
    generator_seeds = np.random.rand(batch_size, 1, 100)

    return generator_seeds
