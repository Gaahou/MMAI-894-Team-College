# MMAI894
## Team College: Hand Gestures Classification

### About The Project
Nowadays, technology has a pivotal role in creating virtual environments with virtual elements. We work collaboratively with real-world intelligent objects on a day-to-day basis. Innovations like the Internet of things (IoT) products, gesture recognition, and teleportation application have certainly made our life "smarter" and more accessible.   

Embracing an "implementing a smarter life" mindset, Team College aims to develop a cool feature in the smart TV that can recognize five different gestures performed by the user to help users control the TV without using a remote. Based on this dataset, Team College wants to develop a well-rounded deep learning gesture recognition model which has applications in a spectrum of different industries beyond smart-TV.

### Data

The training data consists of a few hundred videos categorized into one of the five classes. Each video (typically 2-3 seconds long) is divided into a sequence of 30 frames(images). Various people have recorded these videos performing one of the five gestures in front of a webcam - similar to what the smart TV will use. 
The data file contains a 'train' and a 'val' folder with two CSV files for the two folders. These folders are, in turn, divided into subfolders where each subfolder represents a video of a particular gesture. Each subfolder, i.e., a video, contains 30 frames (or images). Note that all images in a particular video subfolder have the exact dimensions, but different videos may have different dimensions. Specifically, videos have two dimensions - either 360x360 or 120x160 (depending on the webcam used to record the videos). Hence, some pre-processing to standardize the videos will be needed. 
 Each row of the CSV file represents one video and contains three main pieces of information - the name of the subfolder containing the 30 images of the video, the name of the gesture, and the numeric label (between 0-4) of the video.

### To merge data batches in a single file:

Download the data part A-R and put them into a single folder
Open the terminal and move to the specific folder

cat Project_data.tar.bz2.parta* >Data_project.tar.gz.joined

### Usage

Language: python > 3.8

1. Install packages:

    pip install .

2. Open jupyter notebook:

    jupyter notebook

3. Data Preprocessing:

    services/split_data.ipynb

4. Model Training

    gesturecogn_mac_v7.ipynb


### Model Result

#### Model Pipeline
![ModelPerformance](docs/pipeline.jpeg)

#### Model Performance

![ModelPerformance](docs/best_model.png)


### Contact Us

- [Andrew Ng](https://www.linkedin.com/in/andrng/)
- [Deepali Jadhav](https://www.linkedin.com/in/deepalijadhav/)
- [Jiayu Zhang](https://www.linkedin.com/in/jz020/)
- [Mangesh Bodke](https://www.linkedin.com/in/mangesh-b-06a7b222b/)
- [Shuyi Hui](https://www.linkedin.com/in/shelleyshuyi/)
- [Wesley Li](https://www.linkedin.com/in/wesleylifu/)
    
