# CHU_speech_text

## Installation instructions

#### 1. Install Linux Ubuntu VM using VirtualBox
After installing:
1. Run `sudo apt-get update`
2. Run`sudo apt-get install git-core`

#### 2. Install [conda](https://conda.io/docs/user-guide/getting-started.html):
1. Run `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`
2. Run `bash Miniconda3-latest-Linux-x86_64.sh`

#### 3. Install MongoDB and SQLite:
1. Run `chmod +x setup/db_install.sh`
2. Run `sudo setup/db_install.sh`

	
#### 4. Create a new `conda` environment
1. Run `conda create -n eng_speech python=3.5.2`
2. Run `source activate eng_speech`
3. Run `pip install -r setup/requirements.txt`

#### 5. Initialize MongoDB and SQLite databases
1. Run `cd setup/`
2. Run `python db_init.py`
3. Run `cd ../`

#### 6. Start local MongoDB server
In a separate tab, run `mongod --dbpath ./database/mongodb`

## Setting up the application
* Edit dialogue sentences in `conversation.txt`
* Provide the API key and resource name in `config.json`

## Running the application
Simply run `python main.py` in the `eng_speech` conda environment. To deactivate the conda environment, run `source deactivate`.

To see examples of querying the MongoDB and SQLite databases, `cd database/` and run `python sqlite_query_sample.py` or `python mongodb_query_sample.py`

## Architecture design considerations

#### Why we used Linux
* Windows has annoying problems with `pip install`, and not everyone has a Mac

#### Why we used a Linux VM instead of a Docker image
* Playing audio is platform-dependent, and configuring a VM is easier than configuring a Docker container when dealing with audio input/output

#### Why we used `conda`
Easy to control Python versioning and package dependency

#### Why we wrote installation scripts
To save you time ;)

