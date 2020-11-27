## Django-Blog
A simple blog based on Django
### How to run  in development mode:
1. Install ```python3.8.5```, ```pip```, ```virtualenv``` in your system.
2. Clone the project https://github.com/mohsenhsz/django-blog
3. 
```
git clone https://github.com/mohsenhsz/django-blog && cd AA
virtualenv venv  # Create virtualenv named venv
source venv/bin/activate
pip install -r requirements.txt
mv  AA/settings-sample.py AA/settings.py
python manage.py migrate  # Create database tables
```
4. Run ```AA``` using ```python3 manage.py runserver```
5. Go to [http://localhost:8000](localhost:8000) to see your Blog
