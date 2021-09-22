# SNVIP dataset  
This is the dataset with synthetic images from [SceneNet RGB-D](https://robotvault.bitbucket.io/scenenet-rgbd.html)  

Files:  

**First version**: 

Procedure:

-Download and extract the original images from [SceneNet RGB-D](https://robotvault.bitbucket.io/scenenet-rgbd.html) to a specific path, using:
      python sceneNet_download --output_dir <my-path>
    
 Note: 268GB are downloaded and extracts to 500GB. Take in consideration your network speed for this task.
 
 -Select the images from [SceneNet RGB-D](https://robotvault.bitbucket.io/scenenet-rgbd.html) to a specific path, using:
      python select_snvip.py --output-dir <mu-path-to-snvip>
 
 Note: 50,073 images are selected. Take in consideration your disk speed for this task.
 
 -Construct the TF Record file, using:
      python create_tf_record.py
  
 -Use one model detector trained to make inference o train your own object detector. You can use TensorFlow Object Detection API.

Note:  

As a derivation from [SceneNet RGB-D](https://robotvault.bitbucket.io/scenenet-rgbd.html), we provide our programs with the [GPLv3 License](http://www.gnu.org/licenses/gpl-3.0.html)
