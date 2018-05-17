# VidStitch API

## Installation

This is a python 3.6 flask server with all python dependencies managed by pipenv -- a similar system to npm. So first, to get all of this started we need to install pipenv!

To install the system tools this project uses
1. `brew install pipenv`

To install the dependencies of the project (right now just flask), cd into the repo and then run
1. `pipenv install`

and *bam* you have everything you need and the right versions
(this will probably download python 3.6 for the peasants and also flask)

Now, run the app with
* `pipenv run python run.py`

To break that down for you, `pipenv run` runs the following command in the virtual environment our pipfile creates (a perfect world where all dependencies are met) and then python app.py simply runs the python file! 

## Styleguide
Use [PEP8](https://www.python.org/dev/peps/pep-0008/)
Main takeaways:
* 4 spaces for indentation
* Use spaces not tabs (if you're like me, just set your text editor to convert tabs to spaces)
* use lowercase snake case for function names ex(concatenate_video)
* classes use camel case ex(class ProcessedVideo)
* separate classes with two blank lines
* separate methods with one blank line