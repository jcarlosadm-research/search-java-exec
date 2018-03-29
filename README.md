# **search-java-exec**

This project search executables java files in java projects. To work, this application get a json file with an array of urls, like this:

```json
[
{"url": "https://github.com/aaaaa/bbbbb.git"},
{"url": "https://github.com/fffff/dddddd.git"}
]
```
The results will be a collection of folders, each them a project. For each project folder, there should exists one folder per java file thats compile without errors. Beyond that, each file must have at least a non-empty class with at least a non-empty method.

## Requirements

This project needs a java compiler installed, with a **javac** tool. Make sure to have this on system path.

This works with Python 3. Therefore, install more recent **python 3.x** interpreter. And make sure to have **pip** tool available (in windows, this comes with more recent interpreter; in linux, install **python-pip**). In linux, **python-dev** is recomended.
w
With **pip** tool, install (in ubuntu, use "sudo" before each command):
```terminal
pip install virtualenv --upgrade
pip install freeze --upgrade
```

## First time use

Create virtual environment folder by running the following command in the root project:

**Linux**:
```terminal
virtualenv -p python3 .venv
```
**Windows**:
```terminal
virtualenv -p python .venv
```

This will create a *.venv* folder in the root project. This folder contains python3 interpreter (with *python* name), libraries and tools. This allow to keep libraries in the specific versions, dispite the libraries of the system. To activate this virtual environment, run:

**Linux**:
```terminal
source .venv/bin/activate
```
**Windows**:
```terminal
.venv\Scripts\activate
```

Now, install the project libraries:

```terminal
pip install -r requirements.txt
```

## Activate the virtual environment

If the virtual environment is not yet active, run:

**Linux**:
```terminal
source .venv/bin/activate
```
**Windows**:
```terminal
.venv\Scripts\activate
```

## Use

Configure the **config.py** file:

- RESULT_FOLDER: folder which will receive all results
- TEMP_REPOS_FOLDER: folder which will receive each project on *clone* phase
- INPUT_JSON_FILE: json file with urls of the projects
- PROCESSED_JSON_FILE: path and name of the json file of the processed urls
- MAX_WORKERS: number of threads

With the virtual environment activated, run:

```terminal
python main.py
```

## Tests

Run:

```terminal
python -m unittest discover tests
```

## Install new libraries in the virtual environment

First, activate the virtual environment. After that, install the python library with pip:

```terminal
pip install <package>
```

And update the *requirements.txt*:

```terminal
pip freeze > requirements.txt
```

## Deactivate the virtual environment

Run:
```terminal
deactivate
```
