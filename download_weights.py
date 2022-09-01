import segmentation_models as sm
import os

def delete_folder(path="~/.keras/models"):
    os.system("rm -rf " + path)


def download():
    sm.get_available_backbone_names()
    for backbone in sm.get_available_backbone_names():
        print("Downloading:", backbone)
        sm.Unet(backbone_name=backbone, encoder_weights='imagenet')


def move_to_local():
    os.system("mv ~/.keras/models/* ./dataset/")

if __name__ == "__main__":
    delete_folder()
    download()
    move_to_local()