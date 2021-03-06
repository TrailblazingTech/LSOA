# KidViz
Learning Sciences Observation App - Vanderbilt University

## Running Locally

To run locally (on OSX... I can help if you're not on OSX) first install [homebrew](https://brew.sh/) if you
don't already have it. It is a package manager for OSX and is useful for installing all kinds of things.

Next, install python3 using `brew install python`. You can confirm that it worked by opening a new terminal
window and typing `which python` - you should get something like `/usr/local/opt/python/libexec/bin/python`.

Once you've done that, you'll want to install `virtualenv` and `virtualenvwrapper`. Use the command
`pip install virtualenv virtualenvwrapper` to install both of them in your Python3 packages folder. They will
automatically be added to your PATH. You'll want to add the following lines to the end of your `.zshrc` or `.bashrc`
file:

```bash
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

Now when you open a new terminal window, you should be able to use the command `lsvirtualenv` without any errors.

Next, install PostgreSQL, using `brew install postgresql`. Once it finishes, run `brew services start postgresql`
to let homebrew automatically manage its lifecycle for you (it will always just run silently in the background).

(hint: you can also install the GUI program PSequel via `brew cask install psequel` to use a GUI to browse around
your data. I use Postico, but it's a paid program).

Once all this is done, you'll want to type the command `createdb kidviz` to instruct postgres to make a new database
called "kidviz". When this runs successfully, you're ready to dive into the project itself.

Clone the repository to a folder (mine is just ~/Desktop/KidViz). `cd` into the folder, then run `mkvirtualenv KidViz`
to tell Python3 to make a virtual environment specifically for this project called KidViz. Once that's done, you 
should do a `which python` command, which should give you output similar to 
`/Users/yourusername/.virtualenvs/KidViz/bin/python`. This indicates you're correctly in the virtual environment
for this project. While still in the KidViz folder, type `pip install -r requirements.txt` to install into your local
environment all of the dependencies that this project has. This should run without any problems but might take a
minute or two.

Once the dependencies are all installed, type `./manage.py migrate` to run the database migrations - these are a
series of mutating SQL scripts automatically generated by Django based on our models that prime the database with
the correct tables and columns for our project. Next, type `/.manage.py createsuperuser` to create an administrator
user that can log into the admin panel to modify data from there as well.

From here, you're all set. To actually run the entire service, type `./manage.py runserver`. This will run the server
locally at `http://127.0.0.1:8000/` (or alternatively accessible at `http://localhost:8000/`. At this point you 
should be able to use everything in your browser.

If you want allow user to create new users you should set
`kidviz | admin perms | Can Approve or Deny Users` permission.