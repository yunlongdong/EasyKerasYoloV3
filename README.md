# Easy Keras Yolo V3

## Test platform

* **Win10**, ```tensorflow-cpu 1.9.0```,```keras 2.1.5```, ```python 3``` 
* **Ubuntu 14.04**, ```tensorflow-gpu 1.10.1```, ```keras 2.2.4```,```python3```, ```cuda-9.0``` on ```GTX1080```

## Introduction
This repo is intended for purely training your own dataset of detection.
And this repo is mainly modified from [qqwweee/keras-yolo3](https://github.com/qqwweee/keras-yolo3).

## Prepare own dataset

Training on own dataset is quite simple, first download (choose one)

* China Jianguoyun [yolo_weights.h5](https://www.jianguoyun.com/p/DfLoST4Qy5yiBxjg8pAB)
* Google Drive [yolo_weights.h5](https://drive.google.com/file/d/12c67Tu3FsseSgXHlCWBJahdLpClHF30c/view?usp=sharing)

into ```model_data/```

And provide ```model_data/own_classes.txt``` which contains the class name of detecting objects, here I provide a example for only one class detection task.

And then all you need is to prepare ```own_train.txt``` in the same directory with ```train.py```, each line of train.txt is of this format: ```/pat/to/img1 xmin,y_min,x_max,y_max,id```, remember no ```<space>``` before/after ```,``` and an ```<space>``` between ```/path/to/img1``` and ```xmin```. Here I provide a example ```own_train.txt```, remember id starts from 0.

like ```imgs/1.jpg 147,30,437,215,0```

##   Training

```python train.py``` will start training, I recommend reading ```train.py``` carefully before starting. If memory out, change batchsize in ```train.py```

The model trained will be stored in ```logs/000/``` , please check.

## Inference

After training, ```yolo_detect.py``` will detect objects on image while you type the image path. 

Usage:

```python yolo_detect.py --model_path \path\to\models```, remember to use the path to models trained stored in ```logs/000/``` mentioned above.



## My Dataset Performance

I trained my model on detecting box of input image. My dataset size is 500. And I got loss of ```10``` after training. The result is shown below. You can download my trained model in (choose one)

* China Jianguoyun [trained_weights_final.h5](https://www.jianguoyun.com/p/DVy4OIYQy5yiBxjf9pAB) 
* Google Drive [trained_weights_final.h5](https://drive.google.com/file/d/1bswm_MAEfwVwoDSRUFo9wWtSGl2UbJQU/view?usp=sharing)

and put it into ```model_data```/

![](https://raw.githubusercontent.com/yunlongdong/EasyKerasYoloV3/master/imgs/result.jpg)

