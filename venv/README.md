# VENV - Virtual Environment

Unlike VirtualVenv and PipEnv, **Venv** comes with Python standard library (>3.3).

```bash
$ pip3 list
```

However, this might not be the case for some Python installations - such as the Python that ships with Ubuntu. Therefore, we should install it with:

```bash
$ sudo apt-get update
$ sudo apt-get install python3-venv
```

In order to run a python module we have to run this command:

```python3 -m <main-module> <environment-name>```

Create a new virtual environment.

```bash
$ python3 -m venv pandas_env
$ ls
```

Or, to create it inside a another directory:

```bash
$ python3 -m venv environments/pandas_env
```

### Activate

Next, you have to **activate** the virtual environment.

```bash
$ source pandas_env/bin/activate
```

You should see the name of the environment in parentheses in terminal:

```bash
(pandas_env) eks@Star:~/Projects/Dev$ 
```

Another method to check if you are running inside an environment is to run:

```bash
$ which python
/home/eks/Projects/Dev/pandas_env/bin/python
```

### Output packages

Any package you install, will only be available inside this environment.

```bash
$ pip3 list
Package       Version
------------- -------
pip           20.0.2 
pkg-resources 0.0.0  
setuptools    44.0.0 
```

In rare cases, when you want your environment to have access to all other Python packages installed on machine, you can create your environment with this command:

```bash
$ python3 -m venv pandas_env --system-site-packages
```

Now the ```pip list``` command will display all the packages. <br>
To see only the ones installed inside the environment:

```bash
$ pip list --local
```

### Source control

You probably don't want to store your whole virtual environment into source repository. <br>
A better practice is to use ```pip freeze``` to get the packages into a ```requirements.txt``` file and add that to the repository.

```bash
pip3 list > requirements.txt
```

Normally you add the environment folder to ```.gitignore``` file.

### Import packages list

In case you created a new environment and wanted to install the packages from an earlier environment:

```bash
$ pip install -r requirements.txt
```

### Deactivate

```bash
$ deactivate
```

### Remove
To remove a virtual environment you can delete the directory.

```bash
$ rm -rf pandas_env/
```

### Development with Virtual Environment

Never add the project files inside an environment. Virtual environment is meant to be something  that can be created and deleted.



<br>

### References
* [Python Tutorial: VENV (Mac & Linux) - How to Use Virtual Environments with the Built-In venv Module](https://www.youtube.com/watch?v=Kg1Yvry_Ydk)