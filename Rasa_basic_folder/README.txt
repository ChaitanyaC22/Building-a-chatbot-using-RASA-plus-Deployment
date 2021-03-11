
#######################################################################################################
-----------------------------------------------README--------------------------------------------------
#######################################################################################################


ALL THE REQUIRED PACKAGES ALONG WITH THEIR CORRESPONDING VERSIONS ARE AVAILABLE IN 'requirements.txt'
#######################################################################################################

[IMPORTANT: (Post-Installation Step)]: 
File_path: <Conda_Installation_Path>envs\rasa\Lib\site-packages\rasa\core\channels\console.py
File_name: console.py
Make sure to make the following change in line number 24:

DEFAULT_STREAM_READING_TIMEOUT_IN_SECONDS = 3000

#######################################################################################################
------------------------------------------INSTALLATION GUIDE------------------------------------------

#######################################################################################################

#######################################################################################################
STEP 1:
Open Anaconda command prompt and check for virtual environments within the system
Use:
conda info --envs

#######################################################################################################
STEP 2:
Make sure VC++ Build tools are installed. For details on installation
##visit https://visualstudio.microsoft.com/downloads/

#######################################################################################################
STEP 3:
Create a new virtual environment in Anaconda (Creating a Python 3.7.9 virtual environment named rasa)
Use:
conda create -n rasa python=3.7

#######################################################################################################
STEP 4:
Test your environment
Use:
deactivate rasa   							###Redirect to the base(root)

#######################################################################################################
STEP 5:
Activate your virtual environment
Use:
activate rasa

#######################################################################################################
STEP 6: Installing RASA

##Check packages in the environment
Use:
pip freeze

##Install latest version of pip:
Use:
python -m pip install --upgrade pip   				###Upgrade pip

##Check available versions of RASA:
Use:
pip install rasa==   								###Shows all available versions of RASA

##Select RASA version '1.10.14'
(For installation use:)
pip install rasa==1.10.14 							###Installs RASA version 1.10.14

##Check Packages. Necessary packages installed: 
[Note: Refer the requirements.txt file for the list of all packages installed]

pip install tensorflow==tensorflow==2.1.2			###Installs Tensorflow 2.1.2
pip install --upgrade numpy==1.18.5					###Installs Numpy 1.18.5
pip install pandas==1.1.3							###Installs Pandas 1.1.3

#######################################################################################################
STEP 7: Installing Spacy
Use:
pip install rasa[spacy]==1.10.14      				###Specify the version of RASA installed (i.e. '1.10.14')

#######################################################################################################
STEP 8: Installing modules within Spacy
##Modules from spacy (import): Run command prompt as admin [To deal with admin privileges issues, in some cases]

##Run the Anaconda Command Prompt [Run as administrator]
##Activate environment (named rasa)
Use:
activate rasa

Example:
(base) C:\Windows\system32>activate rasa

##Now in your virtual environment 'rasa' install the module
Use:
python -m spacy download en_core_web_md

Example:
(rasa) C:\Windows\system32>python -m spacy download en_core_web_md

##Link the module: 
Use:
python -m spacy link en_core_web_md en  			###Look out for 'Linking successful' message

Example:
(rasa) C:\Windows\system32>python -m spacy link en_core_web_md en	

#######################################################################################################

#######################################################################################################

-------------------------------------INSTALLATION COMPLETE---------------------------------------------

#######################################################################################################

#######################################################################################################

ALL THE REQUIRED PACKAGES ALONG WITH THEIR CORRESPONDING VERSIONS ARE AVAILABLE IN 'requirements.txt'