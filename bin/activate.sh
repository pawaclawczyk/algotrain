export VIRTUALENVWRAPPER_PYTHON=`asdf which python`
export VIRTUALENVWRAPPER_VIRTUALENV=`asdf which virtualenv`
source `asdf which virtualenvwrapper.sh`

workon algotrain || mkvirtualenv algotrain
