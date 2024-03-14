# Plant Growth Stage Classification

This project was created in the context of the [2024 GIL Hackathon](https://ef-sw.de/hackathon-2024/).  
The objective of our task was to classify the growth stage of a diverse set of plants commonly found in Germany. The dataset used is private and crowd-sourced kindly provided by the DWD (German Weather Institute). It is based on images and data recorded by voluntary workers of the [WetterWarn App](https://www.dwd.de/EN/ourservices/warnwetterapp/warnwetterapp.html).

The repo contains the code used to train a [YOLOv8](https://github.com/ultralytics/ultralytics) model on the above mentioned dataset. It can be used to reproduce the results of the project.

## Model Weights

You can find the trained model on the [Hugging Face Hub](https://huggingface.co/kkmarv/gil44-plant-growth-stage-detection)
