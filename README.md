# README #

Required packages and instructions
For this project we will use python3

python -m venv .api_env\
source .api_env/bin/activate\
pip install pip\
pip install -r requirements.txt
### DB Migrations ###
python manage.py makemigrations\
python manage.py migrate\
python manage.py createsuperuser

### RUN Dev Server ###
python manage.py runserver