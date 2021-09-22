# SNVIP Dataset
Synthetic  Dataset  of  Objects  Commonly  Used  by Visually-Impaired People in their Everyday Life  
This is the dataset used for a research paper "Object Detection for Assisting Visually ImpairedPeople: Synthetic Dataset and Benchmarking"

    
[//]: # (Alejandro Gomez-Garay, Bogdan Raducanu, Joaquín Salas)  

The paper addresses the problem of finding objects in their environments, and we construct a synthetic objects dataset based on a survey applied to visually-impaired people.  

<table>
    <tr>
        <td> <img src="frrcnn_detect_basket.png"> </td>
        <td> <img src="frrcnn_detect_bag2.png"> </td>
    </tr>
</table>

We provide:  

    A program to download the dataset of synthetic images with bounding box, and a program to construct the dataset:  
        version 1 with dictionary of 50,743 images and 76,690 object instances

        See the data folder for a script to download the files and construct the dataset.
    
    Four trained models on the first version of the dataset (TF format)  
        SSD ResNet-50 FPN  
        EfficientDet D0
        Faster R-CNN Inception v2  
        Faster R-CNN ResNet-50  
        SSD Inception v2  
        See the model folder to download the files  

If you find this dataset useful in your research, please cite us:  


As a derivation from [SceneNet RGB-D](https://robotvault.bitbucket.io/scenenet-rgbd.html), we provide our programs with the [GPLv3 License](http://www.gnu.org/licenses/gpl-3.0.html)
