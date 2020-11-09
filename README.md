# MP3 PLAYER

This repository has been created to store the MP3 Player project source code in terms of Python-Django course organized by Regex Software Solutions.

## Installation

Make sure you have Python installed on your machine. (version 3.7.0 or higher)

Version check on Windows:
```bash
python --version
```

Clone the project to your local.
```bash
git clone https://github.com/altughan09/mp3player.git
```
Inside the root project folder, you must create a virtual environment.\
[What is virtual environment?](https://docs.python.org/3/tutorial/venv.html)

On Windows:
```bash
python -m venv ./venv
```

Once virtual environment is ready, enter the following command to activate it:
```bash
./venv/Scripts/activate
```

Next install all the required packages using pip according to the requirements.txt file.

[What is the python requirements.txt?](https://www.idkrtm.com/what-is-the-python-requirements-txt/)

```bash
pip install -r requirements.txt
```
https://blog.usejournal.com/why-and-how-to-make-a-requirements-txt-f329c685181e

Create a file named .env in the root. The reason we use .env is to hide important keys from public.\
Your .env file should include the following fields:

SECRET_KEY=''\
NAME=''\
USER=''\
PASSWORD=''\
HOST=''\
PORT=''

**We never push this file to github!**

For SECRET_KEY area you can use [DJANGO SECRET KEY GENERATOR](https://djecrety.ir/) Other fields are for PostgreSQL db credentials. Install PostgreSQL to your machine [here](https://www.postgresql.org/download/). Create a db for this project and enter its credentials in your .env file.

Once all the steps are done, check whether app is running locally by using the following command:

```bash
python manage.py runserver
```

If running properly with no error, it means installation was successful.

## Contribution

We should not touch the **master(main)** branch at all. We have a rc (release candidate) branch and 2 sub-branches.

**For frontend tasks you should work on the dev-frontend branch. (You should checkout to this branch name in Visual Studio Code)**

**For backend tasks you should work on the dev-backend branch. (You should checkout to this branch name in Visual Studio Code)**

Once you are ready to push your work, rise a pull request to the **rc branch**.