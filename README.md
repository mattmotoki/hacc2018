# hacc2018

## Stage 0 - Data Collection
Collect data for images and meta for various types of plants. 

Scrape images for Native, Invasive, and Common plants. 
* [Native Plants](https://drive.google.com/file/d/1lIs8638gBxmWgDSTc84gnGSSHgMsyYXs/view)
* [Invasive Plants](http://www.oahuisc.org/target-pests/)
* Common Plants: hibiscus, plumeria, pineapple, ginger, anthurium, heliconia, bougainvillea

Obtain the images from Instagram, Google, and Starr Environmental. 

Upload all data to our shared [images directory](https://drive.google.com/drive/u/1/folders/1lgRqxc8dWflkXn8a2dRB8GBswCe_bZpZ).



## Stage 1 - Training
Train a model on:
* [PlantNet 2017 Dataset](https://www.imageclef.org/lifeclef/2017/plant): Consists of 10,000 species of plants (). 
* [Oxford 17 Category Flower Dataset](http://www.robots.ox.ac.uk/~vgg/data/flowers/17/index.html): Consists of 17 flower categories with ~80 images for each category (1,361 images).
* [Oxford 102 Category Flower Dataset](http://www.robots.ox.ac.uk/~vgg/data/flowers/102/index.html): Consists of 102 flower categories. Each category consists of between 40 and 258 images (8,189 images).



## Stage 2 - Fine Tuning
Fine tune model using the labels images and labels from Stage 0.

## Stage 3 - Production

## Stage 4 - Analysis
Compare performance of different models and techniques.

### Compare Model Architectures
Architecture | Research Paper
-- | -- 
[MobileNet](https://keras.io/applications/#mobilenet) | [MobileNet: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/pdf/1704.04861.pdf)
[MobileNetV2](https://keras.io/applications/#mobilenetv2) | [MobileNetV2: Inverted Residuals and Linear Bottlenecks](https://arxiv.org/abs/1801.04381)
[NASNetMobile](https://keras.io/applications/#nasnet) | [Learning Transferable Architectures for Scalable Image Recognition](https://arxiv.org/abs/1707.07012)


### Data Augmentation
Determine the effectiveness of brightness augmentation.

* Take photos of a single plant at multiple times of the day (different brightness levels)
* Train a model with/without brightness augmentation
* Plot performance vs. brightness level for both models.
* Calculate average percent improvement

