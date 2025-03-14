import imageio
import matplotlib.pyplot as plt
import numpy as np

# Write your function here!
def edge_detect(duck):
    # Define the kernel
    
    # Apply the kernel
    
    # Normalize the image    
    
    return duck


def main():
    duck = imageio.imread("duck.jpg")
    duck = edge_detect(duck)
    plt.imshow(duck)
    plt.savefig("edge_detect.png")


if __name__ == "__main__":
    main()
