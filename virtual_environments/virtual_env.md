# Virtual Environments in Python

## Why should we use a virtual environment?

- We will consider the scenario where we have a python project that was developed using an older version of a particular dependencies such as Django.

- When we try to run this project using a newer version of Django or certain dependencies, we will run into an error.

- Hence, to prevent such an error from occuring, we will develop our projects in virtual environments.

## How do we develop a project in a virtual environment?

1. Firstly, we will create project folder using the "mkdir" command.

2. Next, we will go into the folder and run "pip install virtualenv". *virtualenv* is what we will be using to create a virtual environment.(This step is necessary only if you have not installed virtualenv on your system before)

3. Next, we will create the virtualenv by running "virtualenv env".

4. After this command runs, when you list the directories in the current folder using "ls", you will notice that there are some folders -> bin,include,lib.

5. Inside the bin folder, you will see the python executable which is copied from your system's current version of python and other dependencies.

6. To activate this environment, we will use "source env/bin/activate". 

*NOTE: IF YOU RUN "pip freeze", YOU CAN LIST ALL THE CURRENT DEPENDENCIES INSTALLED IN PYTHON*

7. Now, any dependecies you install will only be found within this environment and can be found in the **lib folder**.

8. Now, we need to create a requirements.txt which lists all the dependencies present in this environment. We can do so by running "pip freeze > requirements.txt". This copies the output from pip freeze into requirements.txt.

9. Now, we need to create a runtime.txt which states the **full version** of the python we are currently using.
