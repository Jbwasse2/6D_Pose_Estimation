# 6D_Pose_Estimation
ECE 549/CS 543 Final Project

# Contributions (LOOK HERE IF YOU ARE A TA/PROFESSOR GUPTA)
The major changes per section of project are described below.
It should be noted that this code was just merging the branches we all worked on, and we tended to work on some overlapping things, so git merged all of the code on top of eachother. This was done for the sake of having all of the code in one zip file for submission. If you want to run the code of an individual parts please find the corresponding branch on Github.

This README.md (useful for members of the class as a whole, I also fielded questions on piazza and in the issues tab)
## Semantic Segmentation
DenseFusion/depth_segmentation/*
## Pixel-wise Dense Fusion
DenseFusion/lib/network.py
## Iterative Refinement
DenseFusion/tools/train.py
DenseFusion/lib/network.py
## 6D Object Pose Estimation
DenseFusion/tools/eval_linemod.py
DenseFusion/lib/network.py
DenseFusion/datasets/linemod/dataset.py
# Connecting to the Cluster Through SSH
You can SSH into the cluter through the command line with
```
ssh Your-NetID@cc-login.campuscluster.illinois.edu
```
If you don't have a command line interface available or would prefer to use a graphic interface, you can use [PuTTY](https://putty.org/).  

You should then be prompted for a password which should be your netid password.  

Finally, you will be sent an email for you to agree to terms and services for using the cluster which you should agree to if you want to use the cluster. It will take a few minutes for the servers to update that you have accepted the terms and conditions.

## Quality of Life (optional)
If you'd like to be able to SSH into the cluster without needing to enter your netid password every time you can do the following steps.

### Step 1a - SSH Key
Check if you have an SSH Key generated on your computer already with
```
file ~/.ssh/id_rsa.pub
```
If you get a message about the file not existing, go to step 1b. If you get a message along the lines of "OpenSSH RSA public key" you already have an SSH key and can skip to step 2.

### Step 1b - Generating SSH Key
Run the following, you will be prompted to create a password. You do not have to create a password and can simply press enter twice.
```
ssh-keygen -t rsa -b 4096 -C "Your@Email"
```
### Step 2 - Add SSH Key to Server
Run the following, change "Your-NetID" to your actual netid.
```
cat ~/.ssh/id_rsa.pub | ssh Your-NetID@cc-login.campuscluster.illinois.edu 'cat >> ~/.ssh/authorized_keys'
```
You should now be able to SSH into the cluster without needing to enter your netid password.

# Setting up your environment
If you've never used the cluster before, this part will help you get all of the packages that we are using. 

## A Quick Note About your Environment
There are 2 main directories when you first ssh in. The first one is your home directory where you will enter as soon as you ssh in. This directory can be reached by doing 'cd ~/'. The home directory has a limited amount of space (2 GB) of data that can be stored here and is backed up every night. Your code should be placed in the home directory.

The second important directory is the scratch directory. This directory is where your data should go. This directory has a limit of about 10 TB of data, so go wild. It should be noted that files not used in this directory within 30 days are deleted.

## .bashrc (Run once)
The following code will load various software that you'll likely need into your environment for every time you ssh into the cluster.
```
echo $'module load anaconda/3\nmodule load cuda/9.2\nmodule load python/3\nmodule load texlive/2019\nmodule load curl/7.61.0\nmodule load git/2.19.0' >> ~/.bashrc
```
After doing this, run the following to properly configure anaconda
```
echo ". /usr/local/anaconda/5.2.0/python3/etc/profile.d/conda.sh" >> ~/.bashrc
```
Next, I have had issues where I'd run out of memory in the home directory while using anaconda. Therefore I created a softlink to the scratch directory so that way there would be no memory issues
```
mkdir ~/scratch/conda
ln -s ~/scratch/conda .conda
```
Finally, if you'd like anaconda to run on start up, run the following
```
echo "conda activate" >> ~/.bashrc
```
If you think there are other pieces of software you'd like, try running
```
module avail
```
to see what is available. Modules can be installed for your current session by 
```
module load {Software Name}
```
and modules can be permenantly added by adding the previous line to your .bashrc file as follows
```
echo $'module load {Software Name}' >> ~/.bashrc
```
## Python
Anaconda will be used to manage python packages to ensure everyone is using the same software. Please edit the file "requirements.txt" as needed. 

To create an anaconda environment
```
conda create --name cv python=3.7
```

To activate an anaconda environment
```
conda activate cv
```

To update your anaconda environment with changes to the requirements.txt run
```
conda install --file requirements.txt
```
I had issues getting pip to work so some python packages may have to be downloaded more manually. For example torch can be installed with
```
conda install pytorch torchivsion -c pytorch
```


# Getting the Code
Clone this repo with 
```
git clone --recurse-submodules -j8 git@github.com:Jbwasse2/6D_Pose_Estimation.git
```
or 
```
git clone --recurse-submodules -j8 https://github.com/Jbwasse2/6D_Pose_Estimation.git
```
depending on whether you have ssh key set up and linked with github (Which I highly recommend doing so that way you don't have to keep entering in your username and password when you pull/push. See [this link](https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account) for more info. Follow the steps in the "Quality of Life (optional)" section under "Connecting to the Cluster Through SSH" to generate an SSH key.

# Data
The data for this project is kept in my scratch directory. I have created a soft link to this directory in the repository (the soft link is named data). I have changed the permissions of this directory so anyone can access it. To access this data simply do 'cd data'. It should be noted that this data this raw data can only be read to and not written to (except for me, so if you need something changed feel free to ask). However, if you want to change the data in a significant way, I'd recommend copying it to your scratch directory.

Trained models should not be pushed to github as this makes pushing/pulling a pain. Trained models should be left in the 'final_proj/models' in the scratch directory.

# Running your code

In the file of this repository there is 'src/scripts', this has a few examples for running code. When running code for this project you will need to submit a job to the cluster. This will put the code you want to run into a queue. 

If you are interested in running a bash script look at 'src/scripts/run_hello_world.pbs and if you are interested in running python with a GPU have a look at 'src/scripts/py_script.pbs'.

To run either of these on the cluster do the following
```
qsub {script_name}.pbs
```

When running code on the cluster, it may be beneficial to use the secondary queue rather than the eng-instruction queue. See https://piazza.com/class/k5lnmkwhdjy47r?cid=264 for more info.
