# 6D_Pose_Estimation
ECE 549/CS 543 Final Project

# Getting the Code
Clone this repo with 
```
git clone --recurse-submodules -j8 git@github.com:Jbwasse2/6D_Pose_Estimation.git
```
or 
```
git clone --recurse-submodules -j8 https://github.com/Jbwasse2/6D_Pose_Estimation.git
```
depending on whether you have ssh key set up and linked with github (Which I highly recommend doing so that way you don't have to keep entering in your username and password when you pull/push. See [this link](https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) for more info.

# Setting up your environment
If you've never used the cluster before, this part will help you get all of the packages that we are using. 

## .bashrc (Run once)
The following code will load various software that you'll likely need into your environment for every time you ssh into the cluster. The following only needs to be ran once.
```
echo $'module load anaconda/3\nmodule load cuda/10.0\nmodule load python/3\nmodule load texlive/2019\nmodule load curl/7.61.0\nmodule load git/2.19.0' >> ~/.bashrc
```
If you think there are other pieces of software you'd like, try running
```
module avail
```
to see what is available.

## Python
Anaconda will be used to manage python packages to ensure everyone is using the same software. Please edit the file "requirements.txt" as needed. 

To create an anaconda environment
```
conda create --name cv python=3.6
```

To activate an anaconda environment
```
conda activate cv
```

To update your anaconda environment with changes to the requirements.txt run
```
pip install -r requirements.txt
```

## Data
All data should be placed in the scratch folder in your $HOME directory (aka ~/). I am working out the details of having everyone use the same data. So I will update this soon.

Trained models should not be pushed to github as this makes pushing/pulling a pain. Trained models should be left in the 'final_proj/models' in the scratch directory.
