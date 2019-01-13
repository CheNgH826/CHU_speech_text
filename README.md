# Practice English pronunciation with AI using Azure Cognitive Speech services

## Installation instructions

#### 1. Install Ubuntu and Docker
Install Ubuntu on your computer using dual boot or a VirtualBox VM. Instructions are readily available online.

If you choose to use a VirtualBox VM:
* **If you have Docker for Windows installed, uninstall it**
* **If you have Windows Hyper-V enabled, disable it**
* You need to "Enable Audio Output" and "Enable Audio Input" for the installed Ubuntu VM
* If you wish, you can also adjust the resolution settings inside Ubuntu to better suit your screen
* **AFTER STARTING THE VM, DO NOT CHANGE YOUR MICROPHONE OR AUDIO OUTPUT DEVICE**

After installing:
1. `sudo apt-get update`
2. `sudo apt-get install git-core`
3. `git clone` this repo. Alternatively, you could also download the repo contents as a ZIP file.

#### 2. Install Docker on your Ubuntu OS
Instructions are [available here](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

#### 3. Run our Docker container
1. `cd` into this repo's directory
2. `sudo docker build -t eng-speech .` (this will take a while to run)
3. `sudo docker run -d -v "$(pwd)":/dock --device /dev/snd:/dev/snd --name eng-speech eng-speech`

After running these commands, the Docker container (which runs a MongoDB server) will be alive in the background.

## Setting up the application
* Edit dialogue sentences in `conversation.txt`. For regularization purposes, **all words have to be in lowercase**.
* Provide the API key and resource name in `config.json`

## Running the application
1. `sudo docker exec -it eng-speech bash`
2. `cd dock/` then `python main.py`
If you make any changes to the files inside `dock/`, they will also change in your host environment (the Ubuntu OS).

When you close the shell, the container will still be running in the background. The next time you want to run the application again, just `sudo docker exec -it eng-speech bash` again.

To see examples of querying the MongoDB and SQLite databases, you can `pip3 install pymongo`, then `python3 sqlite_query_sample.py` or `python3 mongodb_query_sample.py`.
Alternatively, `pymongo` is already installed in our Docker container, so you could also `sudo docker exec -it eng-speech bash`, `cd dock/database/`, then `python sqlite_query_sample.py` or `python mongodb_query_sample.py`.

## Architecture design considerations

#### Why do we use Docker? Why do we use a Linux-based Docker container?
Docker installs dependencies in a very convenient and stable way, and the user does not have to waste time debugging annoying installation bugs. We use a Linux-based container because the environment can be set up automatically with scripts, unlike Windows which requires manual configuration with GUIs for some software.

#### Why do we have to install Docker under a Linux host OS? Why not use Docker for Windows or Mac?
Docker containers for Windows actually run on Hyper-V Linux VMs, which are unable to pass through audio. Docker containers for Mac run on xhyve Linux VMs, which are also unable to pass through audio (although an inconvenient pulseaudio hack seems to exist). However, Virtualbox can pass through audio from Linux VMs conveniently, and it is also easy for Linux-based Docker containers to pass audio through to a Linux host OS. Thus, to play audio, a Linux-based container first passes the audio to the Linux host OS, and if the Linux OS is running in a VirtualBox VM, Virtualbox then passes the audio to the “real” host OS (Windows or Mac). The resulting audio output may be crackly, but tolerable for our use case.
