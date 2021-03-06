Easy Pipeline Runner Scripts
============================
Scripts to make it easy for your non-technical end users to run the pipeline you have developed. This should work for any local Python pipeline on an on-network ONS computer. 


Overview
********

This readme provides all the details first time users will need in order to get set up and run the pipeline. The majority of 
this set up will be done automatically using a ``.bat`` file, however there are some preqrequisites to getting this up and running.

Prerequisites: Users will need to complete the following steps, with details of them in subsequent sections:

#. Install Anaconda and git
#. Download and configure run_pipeline.bat file
#. Run run_pipeline.bat

A lot of what we cover here can also be found in the `Coding Getting Started Guide <http://np2rvlapxx507/BPI/coding-getting-started-guide/-/wikis/home>`_.

Installing Anaconda and git
***************************
Before users can run or interact with the pipeline, they will need to download Anaconda (with Python included) to enable running of the code and git to assist with management of the codebase (and development). On an ONS machine this software needs to be installed via a service desk request.

Details of how to do this can be found `here <http://np2rvlapxx507/BPI/coding-getting-started-guide/-/wikis/Service-desk-requests#software-install>`_
(just the Software intall section).


Download and Configure run_pipeline.bat
***************************************
Most of the usually laborious steps of getting a pipeline set up to run locally have been packaged up into the ``run_pipeline.bat`` batch file. Similar to
a shell script, a batch file is a special text file that when run will execute (in sequence) various actions in the windows Command Prompt.

Once configured, the ``run_pipeline.bat`` will do the following:

#. Configure :code:`conda` by creating a :code:`.condarc` file (if this does not already exist) with user entered Artifactory credentials.
#. Add the python scripts folder to the path environment variable so that the :code:`conda` command can be run in the Command Prompt. [#]_
#. Configure :code:`pip` by creating a :code:`pip.ini` file (if this does not already exist) with user entered Artifactory credentials.
#. Clone the git repository of the specified project (HTTP or SSH depending on user input).
#. Create or select (if it already exists) a named virtual environment.
#. Activate this environment and install the requirements from the repo's :code:`requirements.txt` file.
#. Run the :code:`pipeline.py` file 

**Note that if any of these steps have been done already (i.e. the script is not being run for a first time user) they will be skipped with the exception of running the pipeline.

The ``run_pipeline.bat`` file can be downloaded `here <INSERT SHAREPOINT LINK>`_.

Before running the `.bat` file users need to configure the settings in it, by opening the it in an editor (:code:`right click > Edit` which should open it in Notepad) and update the variables
in lines `5-19 <https://github.com/ONSdigital/easy_pipeline_run/blob/653bacbc72dab950870cdb79dc1f9264ba1147ac/run_pipeline.bat#L5>`_ and saving it. 

These variables should be as follows:

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - Variable Name
     - Value
     - Details
   * - :code:`local-repo-location`
     - Filepath to folder where repo should be cloned.
     - If the repo already exists it won't be cloned again. This should be the folder above where the repo is saved, e.g if the repo is
       :code:`D:\Docs\Repos\your_project`, then this variable should be :code:`D:\Docs\Repos`. 
   * - :code:`remote-repo-url`
     - Url of the remote repository
     - By default this will clone using the http url, and if you haven't set up git before you will be prompted to enter your gitlab or github
       username and password (you will only have to do this once!). This variable can also take the SSH repo url, however you will have
       needed to set up git and gitlab beforehand to make this work (More details can be found `here <http://np2rvlapxx507/BPI/coding-getting-started-guide/-/wikis/Git#setting-up-ssh-for-gitlab-optional>`_ and for github details can be found `here <https://docs.github.com/en/authentication/connecting-to-github-with-ssh>`_.
       If the repo already exists, this variable will not be used so it's value won't matter.
   * - :code:`python-scripts-location`
     - Filepath of the scripts folder in your Python installation.
     - This likely won't need to be changed - if :code:`C:\Python36\Scripts` exists on your local machine you are good to go! (An error would be raised if it didn't.)
       If not you will need to find where your Python/Anaconda installation is and set this variable to the corresponding Scripts folder - another common location for this is ``C:\Users\<username>\Anaconda\Scripts``.
   * - :code:`python-version`
     - Python version to use when creating a new virtual environment.
     - Again this should stay as the default (:code:`3.6.8`), although other versions are available
   * - :code:`virtual-env-name`
     - The name of the virtual environment to be created/activated.
     - If this does not already exist a new conda environment will be created with this name, e.g. ``my_env_368``. More details on conda environments can be found `here <http://np2rvlapxx507/BPI/coding-getting-started-guide/-/wikis/Python#conda>`_.
   * - :code:`repo-name` 
     - The exact name of the repo
     - e.g. for this repository, the name would be ``easy_pipeline_run``
   * - :code:`config_file`
     - The config file to use when running ``pipeline.py``
     - Using ``default_config.ini`` (the default value in the ``.bat`` script) should work for all users. If you do want to use a different config file, it must be saved in the ``config`` folder within the repo (this won't be possible if the repo hasn't been cloned yet).
   * - :code:`pip-config-location`
     - Where the ``pip.ini`` file should be saved.
     - This shouldn't need to be changed


.. [#] The environment variable that this step sets will only persist within the batch script - i.e. if you don't already have your python scripts path in your path environment variable, ``conda`` commands in the command prompt won't work. If you want to fix this, you need to manually add your python scripts location to your local path variable. To do this search for ``Edit Environment Variables for Your Account`` in your programs and edit the path variable to include your python scripts folder.
Run run_pipeline.bat
********************
Once the user has updated these variables according to the above table they are ready to run the ``run_pipeline.bat`` script which will run the pipeline. To do this you simply need to find the ``.bat`` script in the file explorer and double click on it to execute. Before they run the batch script for the first time we recommend they delete or archive any existing ``pip.ini`` or ``.condarc`` files so that the correct artifactory urls are used. The ``pip.ini`` file can be found in the ``%appdata%\pip`` folder and the ``.condarc`` file can be found in the ``%userprofile%`` folder. 

When running you may find an security warning about running a batch script, this is to be expected and you can click through this.

As mentioned earlier, the ``run_pipeline.bat`` script will also work for any future pipeline runs and will automatically skip the configuration steps already carried out (steps 1-6 in Download and Configure run_pipeline.bat).

Once this script has been run, you will have set up your conda environment with the packages required to run the pipeline as well as configuring ``pip`` and ``conda`` for general use on your machine.  

Common Issues
*************

- If you execute the batch script by clicking on the documents folder in the left of your file explorer you may encounter an error like this:
      ```\\DATADRIVE\user_name$\My Documents\Repos\my_project' CMD.EXE was started with the above path as the current directory.
      UNC paths are not supported.  Defaulting to Windows directory.``` (where DATADRIVE is an unmapped network drive, e.g. "NXDATA12" or similar)
  To avoid this, make sure you run (double click) the ``.bat`` script from your mapped drive. So in this case I would go ``H:/ > Documents > Repos > my_project``
- You may sometimes get an error saying ``H:/.gitignore`` couldn't be accessed or doesn't exist. This is because it is trying to read this from the H drive which can make files unavailable sometimes. A solution to this is changing the ``HOME`` environment variable - details of which can be found `here <https://github.com/best-practice-and-impact/ons-git-config#1-home-location>`_ - however you can also wait until the files become available again.
- If you already have ``pip.ini`` or ``.condarc`` files before running the ``.bat`` script, they may have the wrong artifactory urls in which could lead to issues downloading some of the requirements. Therefore it is recommended that you delete or archive (rename) these files before running the setup script so that they are created fresh with the correct artifactory paths.
- If you already have git set up with http authentication, but you haven't cloned the repo yet you may encounter a git error similar to ``remote: HTTP Basic: Access denied``. This is likely because your windows github or gitlab credentials are outdated, to change these search for "Credential Manager" in the Windows search bar, click on the "Windows Credentials" section and check your git credentials are up to date. If this does not solve the problem then you may not have the required access to the git repo.
